from django.shortcuts import render

def clients_index(request):
    return render(request, 'clients/index.html')