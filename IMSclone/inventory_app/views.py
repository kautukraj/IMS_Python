from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
# A view function takes a Web request and returns a Web response.
# The view itself contains whatever arbitrary logic is necessary to return that response.
def index(request):
    return render(request, 'index.html')
# Django uses request and response objects to pass state through the system.
# render combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.

def admin_module(request):
    return render(request, 'admin_module.html')

def manager_module(request):
    return render(request, 'manager_module.html')

def login(request):
    return render(request, '/registration/login.html')

def display_hatchbacks(request):
    
    items = hatchback.objects.all()
    context = { # A context is a variable name -> variable value mapping that is passed to a template.
        'items': items,
        'header' : 'Hatchbacks',
    }
    return render(request, 'admin_module.html', context)


def display_sedans(request):
    items = sedan.objects.all()
    context = {
        'items': items,
        'header' : 'Sedans'
    }
    return render(request, 'admin_module.html', context)


def display_SUVsMUVs(request):
    items = SUVMUV.objects.all()
    context = {
        'items': items,
        'header' : 'SUVs/MUVs'
    }
    return render(request, 'admin_module.html', context)


def display_vans(request):
    items = van.objects.all()
    context = {
        'items': items,
        'header' : 'Vans'
    }
    return render(request, 'admin_module.html', context)

def add_car(request, cls): # creating an object of type add_car
    if request.method == "POST": # POST is a request method
    # if this is a POST request we need to process the form data        
    #  a request that makes changes in the database - should use POST        
        form = cls(request.POST) # getting all the form fields of the class
        # create a form instance and populate it with data from the request:

        if form.is_valid():
        # process the data in form.cleaned_data as required

            form.save()
            return redirect('admin_module') 

    else: # GET is the request method when it is being called for the first time
    # GET should be used only for requests that do not affect the state of the system.        
        form = cls() # blank form
        return render(request, 'add_new.html', {'form' : form}) # form is the context here


def add_hatchback(request): 
    return add_car(request, hatchbackForm)


def add_sedan(request):
    return add_car(request, sedanForm)


def add_SUVMUV(request):
    return add_car(request, SUVMUVForm)

def add_van(request):
    return add_car(request, vanForm)

def edit_car(request, pk, model, cls): # PK stands for Primary Key. All Django models have this attribute.
    item = get_object_or_404(model, pk=pk)
# The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, 
# which it passes to the get() function of the model’s manager.
# It raises Http404 if the object doesn’t exist.

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('admin_module') 
    else:
        form = cls(instance=item)

        return render(request, 'edit_car.html', {'form': form}) # form is context



def edit_hatchback(request, pk):
    return edit_car(request, pk, hatchback, hatchbackForm)


def edit_sedan(request, pk):
    return edit_car(request, pk, sedan, sedanForm)


def edit_SUVMUV(request, pk):
    return edit_car(request, pk, SUVMUV, SUVMUVForm)

def edit_van(request, pk):
    return edit_car(request, pk, van, vanForm)


def delete_hatchback(request, pk): # similar to edit

    template = 'admin_module.html'
    hatchback.objects.filter(id=pk).delete() # filter (select) that particular field

    items = hatchback.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_sedan(request, pk):

    template = 'admin_module.html'
    sedan.objects.filter(id=pk).delete()

    items = sedan.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_SUVMUV(request, pk):

    template = 'admin_module.html'
    SUVMUV.objects.filter(id=pk).delete()

    items = SUVMUV.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_van(request, pk):

    template = 'admin_module.html'
    van.objects.filter(id=pk).delete()

    items = van.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)    





def display_hatchbacks_manager(request):
    
    items = hatchback.objects.all()
    context = { # A context is a variable name -> variable value mapping that is passed to a template.
        'items': items,
        'header' : 'Hatchbacks',
    }
    return render(request, 'manager_module.html', context)


def display_sedans_manager(request):
    items = sedan.objects.all()
    context = {
        'items': items,
        'header' : 'Sedans'
    }
    return render(request, 'manager_module.html', context)


def display_SUVsMUVs_manager(request):
    items = SUVMUV.objects.all()
    context = {
        'items': items,
        'header' : 'SUVs/MUVs'
    }
    return render(request, 'manager_module.html', context)


def display_vans_manager(request):
    items = van.objects.all()
    context = {
        'items': items,
        'header' : 'Vans'
    }
    return render(request, 'manager_module.html', context)


def edit_car_manager(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('manager_module') 
    else:
        form = cls(instance=item)

        return render(request, 'edit_car.html', {'form': form})



def edit_hatchback_manager(request, pk):
    return edit_car_manager(request, pk, hatchback, hatchbackForm)


def edit_sedan_manager(request, pk):
    return edit_car_manager(request, pk, sedan, sedanForm)


def edit_SUVMUV_manager(request, pk):
    return edit_car_manager(request, pk, SUVMUV, SUVMUVForm)

def edit_van_manager(request, pk):
    return edit_car_manager(request, pk, van, vanForm)