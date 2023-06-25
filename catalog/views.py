from django.shortcuts import render

from catalog.models import Product, Category, Contacts


def home(request):
    # category = Category.objects.all()
    # for category_item in category.reverse():
    #     print(category_item)
    products = Product.objects.all()
    for products_item in products.reverse():
        print(products_item)
    return render(request, 'catalog/home.html')


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
