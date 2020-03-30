from django.shortcuts import render

def electronics(request):
    products_dic = {
    'product1':'Mac',
    'product2':'IPhone',
    'product3': 'Dell'
    }
    return render(request, 'productApp/products.html', products_dic)

def toys(request):
    products_dic = {
    'product1':'BigMan',
    'product2':'Drone',
    'product3': 'Shuuter Mouse'
    }
    return render(request, 'productApp/products.html',products_dic)

def shoes(request):
    products_dic = {
    'product1':'Nike',
    'product2':'Advas',
    'product3': 'No Name'
    }
    return render(request, 'productApp/products.html', products_dic)

def index(request):
    return render(request, 'productApp/index.html')
