from django.shortcuts import render

from catalog.models import Product, Category, Contacts


def home(request):
    # category = Category.objects.all()
    # for category_item in category.reverse():
    #     print(category_item)
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        with open('text.txt', 'a') as f:
            f.write(f'{name}, {phone}, {message}; ')
        print(f'{name}, {phone}, {message}')
        Contacts.objects.create(name=name, phone=phone, message=message)
    return render(request, 'catalog/contacts.html')


def product(request, pk: int):
    # category = Category.objects.all()
    # for category_item in category.reverse():
    #     print(category_item)
    products = Product.objects.get(pk=pk)
    context = {
        'object': products
    }
    return render(request, 'catalog/product.html', context)