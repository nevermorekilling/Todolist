from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    # Django will automatically search folders called templates
    # inside any of your apps' directories
    return render(request, 'home.html')
