from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.
# A view function takes a Web request and returns a Web response.
# The view itself contains whatever arbitrary logic is necessary to return that response.
def index(request):
    return render(request, 'index.html')
# Django uses request and response objects to pass state through the system.
# render combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.

def display_hatchbacks(request):
    items = hatchback.objects.all()
    path=request.path
    context = { # A context is a variable name -> variable value mapping that is passed to a template.
        'items': items,
        'header' : 'Hatchbacks',
        'path' : path
    }
    return render(request, 'index.html', context)


def display_sedans(request):
    items = sedan.objects.all()
    context = {
        'items': items,
        'header' : 'Sedans'
    }
    return render(request, 'index.html', context)


def display_SUVsMUVs(request):
    items = SUVMUV.objects.all()
    context = {
        'items': items,
        'header' : 'SUVs/MUVs'
    }
    return render(request, 'index.html', context)


def display_vans(request):
    items = van.objects.all()
    context = {
        'items': items,
        'header' : 'Vans'
    }
    return render(request, 'index.html', context)

def add_car(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})


def add_hatchback(request):
    return add_car(request, hatchbackForm)


def add_sedan(request):
    return add_car(request, sedanForm)


def add_SUVMUV(request):
    return add_car(request, SUVMUVForm)

def add_van(request):
    return add_car(request, vanForm)

def edit_car(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_car.html', {'form': form})



def edit_hatchback(request, pk):
    return edit_car(request, pk, hatchback, hatchbackForm)


def edit_sedan(request, pk):
    return edit_car(request, pk, sedan, sedanForm)


def edit_SUVMUV(request, pk):
    return edit_car(request, pk, SUVMUV, SUVMUVForm)

def edit_van(request, pk):
    return edit_car(request, pk, van, vanForm)



def delete_hatchback(request, pk):

    template = 'index.html'
    hatchback.objects.filter(id=pk).delete()

    items = hatchback.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_sedan(request, pk):

    template = 'index.html'
    sedan.objects.filter(id=pk).delete()

    items = sedan.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_SUVMUV(request, pk):

    template = 'index.html'
    SUVMUV.objects.filter(id=pk).delete()

    items = SUVMUV.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_van(request, pk):

    template = 'index.html'
    van.objects.filter(id=pk).delete()

    items = van.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)