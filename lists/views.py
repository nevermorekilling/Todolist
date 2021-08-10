# from django.http import response
from lists.forms import ExistingListItemForm, ItemForm
# from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from lists.models import Item
from lists.models import List

# Create your views here.


def home_page(request):
    # Django will automatically search folders called templates
    # inside any of your apps' directories
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['text'])
    # print('request content is :\n', request)
    # return render(request, 'home.html')

    # item = Item()
    # item.text = request.POST.get('text', '')
    # item.save()

    # if request.method == 'POST':
    #     new_text = request.POST['text']
    #     Item.objects.create(text=new_text)
    # else:
    #     new_text = ''

    # if request.method == 'POST':
    # Item.objects.create(text=request.POST['text'])
    # return redirect('/')
    # return redirect('/lists/the-only-list-in-the-world/')

    # return render(request, 'home.html', {'new_text':
    #  request.POST['text']})
    # return render(request, 'home.html', {'new_text':
    #  request.POST.get('text', '')})
    # return render(request, 'home.html', {'new_text': new_text})

    # for debug
    # print(request.POST.get('text', 'no set yet'))
    # print(request.__dict__)

    return render(request, 'home.html', {'form': ItemForm()})
    # return render(
    #     request, 'home.html', {
    #         'text': request.POST.get(
    #             'text', 'no set yet')})
    # items = Item.objects.all()
    # return render(request, 'home.html', {'items': items})
    # return render(request, 'home.html', {'new_text':
    # request.POST.get('id_text', '')})


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    # form = ItemForm()
    form = ExistingListItemForm(for_list=list_)
    if request.method == 'POST':
        # form = ItemForm(data=request.POST)
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save(for_list=list_)
            # Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {'form': form})
    # list_ = List.objects.create()
    # item = Item.objects.create(text=request.POST['text'], list=list_)
    # try:
    #     item.full_clean()
    #     item.save()
    # except ValidationError:
    #     list_.delete()
    #     error = "You can't have an empty list item"
    #     return render(request, 'home.html', {"error": error})
    # when passed a model , the model's get_absolute_url method will be
    # called


# def add_item(request, list_id):
#     list_ = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST['text'], list=list_)
#     return redirect(f'/lists/{list_.id}/')
