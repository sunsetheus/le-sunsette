from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    items = Item.objects.all()

    context = {
        'nama_mahasiswa': 'William',
        'kelas_mahasiswa': 'PBP D', 
        'nama_aplikasi': 'Le Sunsette',
        'menus': items
    }
    return render(request, "main.html", context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
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