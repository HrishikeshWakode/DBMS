
from django.shortcuts import render, redirect
from .models import Hospital, User, Inventory
from .forms import HospitalForm, UserForm, InventoryForm
from django.http import HttpResponse, JsonResponse


def add_hospital(request):
    if request.method == "POST":
        name = request.POST.get("name")
        location = request.POST.get("location")
        contact_number = request.POST.get("contact_number")
        email = request.POST.get("email")

       
        hospital = Hospital(name=name, location=location, contact_number=contact_number, email=email)
        hospital.save()

        return HttpResponse("<h3>Hospital added successfully! <a href='/bloodlife/add_hospital/'>Add another</a></h3>")
    
    return render(request, "add_hospital.html")


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_user')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def add_inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_inventory')
    else:
        form = InventoryForm()
    return render(request, 'view_inventory.html', {'form': form})
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')

def view_inventory(request):
    inventory = Inventory.objects.all().values('blood_group', 'units_available')
    return JsonResponse(list(inventory), safe=False)