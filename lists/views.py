from django.shortcuts import redirect, render
# from django.http import HttpResponse
from lists.models import Item

# Create your views here.


def home_page(request):
    # Django will automatically search folders called templates
    # inside any of your apps' directories
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # print('request content is :\n', request)
    # return render(request, 'home.html')

    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    # if request.method == 'POST':
    #     new_item_text = request.POST['item_text']
    #     Item.objects.create(text=new_item_text)
    # else:
    #     new_item_text = ''

    # if request.method == 'POST':
    # Item.objects.create(text=request.POST['item_text'])
    # return redirect('/')
    # return redirect('/lists/the-only-list-in-the-world/')

    # return render(request, 'home.html', {'new_item_text':
    #  request.POST['item_text']})
    # return render(request, 'home.html', {'new_item_text':
    #  request.POST.get('item_text', '')})
    # return render(request, 'home.html', {'new_item_text': new_item_text})

    return render(request, 'home.html')
    # items = Item.objects.all()
    # return render(request, 'home.html', {'items': items})
    # return render(request, 'home.html', {'new_item_text':
    # request.POST.get('id_item_text', '')})


def view_list(request):
    # handle url /lists/the-only-list-in-the-world/

    items = Item.objects.all()
    # return render(request, 'home.html', {'items': items})
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
