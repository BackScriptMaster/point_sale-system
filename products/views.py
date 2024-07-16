from django.shortcuts import render

# Create your views here.

def products_index(request):
    return render(request, 'products/index.html')