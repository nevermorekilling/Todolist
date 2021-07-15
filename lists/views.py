from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request):
    # Django will automatically search folders called templates
    # inside any of your apps' directories
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # print('request content is :\n', request)
    # return render(request, 'home.html')

    # return render(request, 'home.html', {'new_item_text': request.POST['item_text']})
    return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', '')})
    # return render(request, 'home.html', {'new_item_text': request.POST.get('id_item_text', '')})
