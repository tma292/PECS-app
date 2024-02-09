from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from . import forms, models
from django.contrib import messages
from json import dumps

from .application import play_sound


def call_play_sound(req):
    if req.method == 'GET':
        # write_data.py write_csv()Call the method.
        #Of the data sent by ajax"input_data"To get by specifying.
        voice = models.Board.objects.filter(name="PECS Board").values('voice_choice')
        voice = voice[0]['voice_choice']
        play_sound.playtext(req.GET.get("input_data"), voice)
        return HttpResponse()
# Create your views here.
def board(request):
    board = models.Board.objects.filter(name="PECS Board").values('name', 'id').distinct()
    tabs = models.Tab.objects.filter(board=board[0]['id'])
    tabs_img = models.Tab.objects.filter(board=board[0]['id']).values('id', 'images')
    l = []
    apple = models.Image.objects.get(id=3)
    for i in tabs_img:
        l.append(i['images'])
    imgs = models.Image.objects.filter(id__in=l)
    # if request.method == 'POST' and 'run_script' in request.POST:
    #     playtext()
    dict = {'board': board,
            'tabs': tabs,
            'tabs_img': tabs_img,
            'imgs': imgs,
            'audios': apple.audio,
            'current_path': request.path}
    return render(request, 'board.html', dict)

def tab_content(request, id):
    dict = {}
    return render(request, 'tab_content.html', dict)

def add_folder_form(request, mydict):
    folderForm = forms.FolderForm()
    if request.method == 'POST':
        folderForm = forms.FolderForm(request.POST)
        if folderForm.is_valid():
            folder = folderForm.save(commit=False)
            folder.save()
            # messages.success(request, 'Card is successfully added!')
    return HttpResponseRedirect('library')
    # return mydict

def add_image_form(request, dict):
    imageForm = forms.ImageForm()
    if request.method == 'POST':
        imageForm = forms.ImageForm(request.POST, request.FILES)
        if imageForm.is_valid():
            image = imageForm.save(commit=False)
            image.save()
        # else:
            # dict['imageForm'] = forms.ImageForm(request.POST, request.FILES)
    return HttpResponseRedirect('library')
    # return dict

def library(request):
    folderForm = forms.FolderForm()
    imageForm = forms.ImageForm()
    categories = models.Category.objects.all().order_by('name')
    images = {}
    for category in categories:
        images[category] = models.Image.objects.filter(category=category).values('image').distinct()[:1]
    dict = {'current_path': request.path,
            'categories': categories,
            'images': images,
            'imageForm': imageForm,
            'folderForm': folderForm}
    if request.method == 'POST':
        imageForm = forms.ImageForm(request.POST, request.FILES)
        folderForm = forms.FolderForm(request.POST)
        if imageForm.is_valid():
            image = imageForm.save(commit=False)
            image.save()
        if folderForm.is_valid():
            folder = folderForm.save(commit=False)
            folder.save()
        return HttpResponseRedirect('library')
    return render(request, 'library.html', dict)

def category_image(request, name, id):
    addimageForm = forms.AddForm()
    category = models.Category.objects.get(id=id)
    images = models.Image.objects.filter(category=category).values('id', 'label', 'image').distinct()
    dict = {'images': images,
            'addimageForm': addimageForm,
            'category': category}
    if request.method == 'POST':
        addimageForm = forms.AddForm(request.POST)
        if addimageForm.is_valid():
            image_id = request.POST.get('image_id')
            tab_id = request.POST.get('tab')
            image = models.Image.objects.get(id=image_id)
            tab = models.Tab.objects.get(id=tab_id)
            tab.images.add(image)
            tab.save()
        return HttpResponseRedirect(str(id))
    return render(request, 'category_images.html', dict)

def search(request):
    addimageForm = forms.AddForm()
    if request.method == 'POST':
        searched = request.POST.get('searched')
        result = models.Image.objects.filter(label__icontains=searched)
    dict = {'searched': searched,
            'result': result,
            'addimageForm': addimageForm}
    return render(request, 'search_list.html', dict)

def settings(request):
    if request.method == 'GET':
        voice_choice = request.GET.get('voice_choice')
        models.Board.objects.filter(name="PECS Board").update(voice_choice=voice_choice)
    dict = {}
    return render(request, 'settings.html', dict)