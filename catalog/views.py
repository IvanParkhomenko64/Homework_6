from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.mixins import OwnerCheckMixin, CacheViewMixin
from catalog.models import Product, Category, Contacts, Version
from catalog.services import cache_category, category_selection
from config.settings import CACHE_ENABLED


# def home(request):
#     # category = Category.objects.all()
#     # for category_item in category.reverse():
#     #     print(category_item)
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list
#     }
#     return render(request, 'catalog/home.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


    def get_queryset(self):
        queryset = super().get_queryset()

        for product in queryset:
            version = product.version_set.all().filter(version_is_active=True).first()
            product.version = version
        if self.request.user.is_anonymous:
            queryset = []
        return queryset


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.add_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context['formset'] = ProductFormset(
                self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)

        return context

    def form_valid(self, form):

        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            self.object.owner = self.request.user
            formset.save()

        return super().form_valid(form)


class ProductUpdateView(PermissionRequiredMixin, OwnerCheckMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.change_product'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(
            Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context['formset'] = ProductFormset(
                self.request.POST, instance=self.object)
        else:
            context['formset'] = ProductFormset(instance=self.object)

        return context

    def form_valid(self, form):

        formset = self.get_context_data()['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         with open('text.txt', 'a') as f:
#             f.write(f'{name}, {phone}, {message}; ')
#         print(f'{name}, {phone}, {message}')
#         Contacts.objects.create(name=name, phone=phone, message=message)
#     return render(request, 'catalog/contacts.html')

class ContactsCreateView(CreateView):
    model = Contacts
    fields = ('name', 'phone', 'message',)
    success_url = '/contacts/'
    template_name = 'catalog/contacts.html'


class ProductDetailView(CacheViewMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'
    permission_required = 'catalog.view_product'


# def product(request, pk: int):
#     # category = Category.objects.all()
#     # for category_item in category.reverse():
#     #     print(category_item)
#     # products = Product.objects.get(pk=pk)
#     products = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': products
#     }
#     return render(request, 'catalog/product.html', context)

class ProductDeleteView(PermissionRequiredMixin, OwnerCheckMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.delete_product'


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'is_active_categories': 'active'
    }

    def get_queryset(self):
        return cache_category()
