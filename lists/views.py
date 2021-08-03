# from django.http import response
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
# from django.http import HttpResponse
from lists.models import Item, List

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

    # for debug
    # print(request.POST.get('item_text', 'no set yet'))
    # print(request.__dict__)

    return render(request, 'home.html')
    # return render(
    #     request, 'home.html', {
    #         'item_text': request.POST.get(
    #             'item_text', 'no set yet')})
    # items = Item.objects.all()
    # return render(request, 'home.html', {'items': items})
    # return render(request, 'home.html', {'new_item_text':
    # request.POST.get('id_item_text', '')})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None
    # items = Item.objects.filter(list=list_)
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"
    return render(request, 'list.html', {'list': list_, 'error': error})


def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
        # when passed a model , the model's get_absolute_url method will be
        # called
    return redirect(list_)


# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['item_text'], list=list_)
#     return redirect(f'/lists/{list_.id}/')
