from django.shortcuts import render

def sales_index(request):
    return render(request, 'sales/index.html')