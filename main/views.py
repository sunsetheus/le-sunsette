from django.shortcuts import render

# Create your views here.
def show_main(request):
  context = {
     'nama_mahasiswa': 'William',
     'kelas_mahasiswa': 'PBP D',
     'nama_aplikasi': 'Le Sunsette',
     'name': 'Plain croissant',
     'amount': 6,
     'description': 'Classic type croissant with layers of buttery dough, each bite reveals a harmony of flaky and melted buttery. Savor the simplicity of pure delight – the perfect companion to your morning coffee or a snack',
     'price': 2.2
  }

  return render(request, "main.html", context)