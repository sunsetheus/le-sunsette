from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

from main.forms import ItemForm
from main.models import Item

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'nama_mahasiswa': 'William',
        'kelas_mahasiswa': 'PBP D', 
        'nama_aplikasi': 'Le Sunsette',
        'menus': items,
        "user": request.user,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, "main.html", context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {
      'form': form,
      'nama_mahasiswa': 'William', #add additional context for add_item.html
      'kelas_mahasiswa': 'PBP D', #add additional context for add_item.html
      'nama_aplikasi': 'Le Sunsette', #add additional context for add_item.html

      }
    return render(request, "add_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='main:login')
def increment_item(request, id):
    item = Item.objects.get(id=id)
    item.amount += 1
    item.save()
    return redirect('main:show_main')

@login_required(login_url='main:login')
def decrement_item(request, id):
    item = Item.objects.get(id=id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    return redirect('main:show_main')

@login_required(login_url='main:login')
def delete_item(request, id):
    item  = Item.objects.get(id=id)
    if item.user == request.user:
        item.delete()
        return redirect('main:show_main')
    
#TUGAS 6
def get_item_json(request):
  print("yay")
  items = Item.objects.all()
  return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def add_item_ajax(request):
  if request.method == 'POST':
    name = request.POST.get("name")
    amount = request.POST.get("amount")
    description = request.POST.get("description")
    price = request.POST.get("price")
    user = request.user

    new_item = Item(name=name, amount=amount, description=description, user=user, price=price)
    new_item.save()

    return HttpResponse(b"CREATED", STATUS=201)
  
  return HttpResponseNotFound()

@csrf_exempt
def increment_item_ajax(request):
  if request.method == 'POST':
    id = request.POST.get("id")
    updated = Item.objects.get(pk=id)
    updated.amount += 1
    updated.save()
    return HttpResponse(b"UPDATED", status=201)
  return HttpResponseNotFound()

@csrf_exempt
def decrement_item_ajax(request):
  if request.method == 'POST':
    id = request.POST.get("id")
    updated = Item.objects.get(pk=id)
    if updated.amount > 0:
      updated.amount -= 1
    updated.save()
    return HttpResponse(b"UPDATED", status=201)
  return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request):
  if request.method == 'POST':
    id = request.POST.get("id")
    item = (Item.objects.get(pk=id))
    item.delete()
    return HttpResponse(b"DELETED", STATUS=201)
  return HttpResponseNotFound()