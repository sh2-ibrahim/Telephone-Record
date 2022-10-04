from django.shortcuts import render, redirect
from directory.models import Directory
from django.urls import reverse
from .forms import DirectoryForm
from django.contrib import messages
# Create your views here.


def index(request):
    contacts = Directory.objects.all()
    context = {
        'phonebooks': contacts
    }
    return render(request, 'directory/index.html', context)


def insert(request):
    form = DirectoryForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('insert'))
    return render(request, 'directory/insert.html', context)


def remove(request, id):
    contact = Directory.objects.get(id=id)
    contact.delete()
    messages.success(request, 'Contact deleted')
    return redirect(reverse('index'))


def amend(request, id):
    instance = Directory.objects.get(id=id)
    form = DirectoryForm(request.POST or None,
                         request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
    return render(request, 'directory/insert.html', context)