from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.


def home(request):
    url = "https://fakestoreapi.com/products"

    response = requests.get(url)

    if response.status_code == 200:
        data = {
            'products': response.json()
        }
        return render(request, 'example/catalog.html', data)

    else:
        return HttpResponse('Error')
