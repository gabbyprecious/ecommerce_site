from django.http import HttpResponse

def home(request):
    return HttpResponse("This is a shopping site for products")

def order(request):
    return HttpResponse("Hello, welcome to our store, browse to our products and order!")
