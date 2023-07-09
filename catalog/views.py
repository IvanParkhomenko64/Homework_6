from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Category, Contacts


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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

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
