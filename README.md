# Le-Sunsette
[Preview Website]()

### Navigator Tugas
1. [Tugas 2](#2)
2. [Tugas 3](#3)
3. [Tugas 4](#4)

# <a id="2">Tugas 2</a>
## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial) 
<details>
  <summary>Set up repo</summary>

  1) Buat repository Github bernama `le-sunsette` dengan visibilitas public dan pilih penambahan file Readme.md
  2) Buat file bernama `.gitignore` yang berisi:
     ```python
     # Django
     *.log
     *.pot
     *.pyc
     __pycache__
     db.sqlite3
     media
     
     # Backup files
     *.bak 
    
     # If you are using PyCharm
     # User-specific stuff
     .idea/**/workspace.xml
     .idea/**/tasks.xml
     .idea/**/usage.statistics.xml
     .idea/**/dictionaries
     .idea/**/shelf
     
     # AWS User-specific
     .idea/**/aws.xml
    
     # Generated files
     .idea/**/contentModel.xml
    
     # Sensitive or high-churn files
     .idea/**/dataSources/
     .idea/**/dataSources.ids
     .idea/**/dataSources.local.xml
     .idea/**/sqlDataSources.xml
     .idea/**/dynamic.xml
     .idea/**/uiDesigner.xml
     .idea/**/dbnavigator.xml
     
     # Gradle
     .idea/**/gradle.xml
     .idea/**/libraries
    
     # File-based project format
     *.iws
    
     # IntelliJ
     out/
    
     # JIRA plugin
     atlassian-ide-plugin.xml
    
     # Python
     *.py[cod] 
     *$py.class 
    
     # Distribution / packaging 
     .Python build/ 
     develop-eggs/ 
     dist/ 
     downloads/ 
     eggs/ 
     .eggs/ 
     lib/ 
     lib64/ 
     parts/ 
     sdist/ 
     var/ 
     wheels/ 
     *.egg-info/ 
     .installed.cfg 
     *.egg 
     *.manifest 
     *.spec 
    
     # Installer logs 
     pip-log.txt 
     pip-delete-this-directory.txt 
     
     # Unit test / coverage reports 
     htmlcov/ 
     .tox/ 
     .coverage 
     .coverage.* 
     .cache 
     .pytest_cache/ 
     nosetests.xml 
     coverage.xml 
     *.cover 
     .hypothesis/ 
     
     # Jupyter Notebook 
     .ipynb_checkpoints 
    
     # pyenv 
     .python-version 
    
     # celery 
     celerybeat-schedule.* 
    
     # SageMath parsed files 
     *.sage.py 
    
     # Environments 
     .env 
     .venv 
     env/ 
     venv/ 
     ENV/ 
     env.bak/ 
     venv.bak/ 
    
     # mkdocs documentation 
     /site 
    
     # mypy 
     .mypy_cache/ 
    
     # Sublime Text
     *.tmlanguage.cache 
     *.tmPreferences.cache 
     *.stTheme.cache 
     *.sublime-workspace 
     *.sublime-project 
    
     # sftp configuration file 
     sftp-config.json 
    
     # Package control specific files Package 
     Control.last-run 
     Control.ca-list 
     Control.ca-bundle 
     Control.system-ca-bundle 
     GitHub.sublime-settings 
    
     # Visual Studio Code
     .vscode/* 
     !.vscode/settings.json 
     !.vscode/tasks.json 
     !.vscode/launch.json 
     !.vscode/extensions.json 
     .history
     ```
  3) Lakukan command `git clone` dengan url repository tersebut, pastikan sudah berada di direktori lokal yang diinginkan
  
</details>

<details>
  <summary>Membuat sebuah proyek Django baru. (pov pengguna Windows)</summary>
  1) Masuk ke dalam direktori yang sudah di-clone

  2) Di dalam direktori tersebut, buka command prompt dan buat virtual environemnt baru dengan menjalankan:
     ```
     python -m venv env
     ```
  3) Aktifkan virtual environtment
     ```
     env\Scripts\activate.bat
     ```
  4) Virtual environment berhasil diaktifkan ditandai dengan `(env)` pada bagian awal input command line. Pastikan virtual environment tetap berjalan.
  5) Di direktori yang sama, buat berkas `requirements.txt` yang berisi:
     ```
     django
     gunicorn
     whitenoise
     psycopg2-binary
     requests
     urllib3
     ```
  6) Unduh depedencies dengan menjalankan kode di command prompt
     ```
     pip install -r requirements.txt
     ```
  7) Pada direktori yang sama, buat direktori project Django bernama `le_sunsette` dengan menjalankan perintah (pastikan terdapat `.` pada akhir kode):
     ```
     django-admin startproject le_sunsette .
     ```
  8) Untuk keperluan deployment, tambahkan `"*"` untuk variabel `ALLOWED_HOSTS` pada file `settings.py`, seperti:
     ```python
     ...
     ALLOWED_HOSTS = ["*"]
     ...
     ```
  9) Jalankan server Django dengan perintah:
     ```
     python manage.py runserver
     ```
</details>

<details>
  <summary>Membuat aplikasi dengan nama main pada proyek tersebut.</summary>
  
  1) Buat direktori `main` untuk membuat aplikasi baru dengan menjalankan:
     ```
     python manage.py startapp main
     ```
  2) Tambahkan `'main'` untuk variabel `INSTALLED_APPS` pada file `settings.py`, seperti:
     ```python
     INSTALLED_APPS = [
       ...,
       'main',
       ...
     ]
     ```
  3) Buat direktori `templates` di dalam direktor `main`
  4) Buat berkas `main.html` di dalam direktor `templates` yang isinya disesuaikan dengan tampilan yang ingin dilihat client (bagian ini nantinya akan diubah pada tahap selanjutnya)
</details>

<details>
  <summary>Membuat model pada aplikasi main.</summary>
  
  1) Buka berkas `models.py` pada direktori `main` dan isi dengan kode:
     ```python
     from django.db import models

     class Item(models.Model):
       name = models.CharField(max_length=255)
       amount = models.IntegerField()
       description = models.TextField()
       price = models.IntegerField()
       type = models.CharField(max_length=255)
     ```

  3) Buat dan terapkan migrasi model dengan menjalankan kode:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```
</details>

<details>
  <summary>Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.</summary>

  1) Tambahkan baris impor berikut pada berkas `views.py` di direktori aplikasi `main`:
     ```python
     from django.shortcuts import render
     ```
 
  2) Tambahkan fungsi `show-main` yang menampilkan nama aplikasi, serta nama dan kelas mahasiswa
     ```python
     def show_main(request):
       context = {
          'nama_mahasiswa': 'William',
          'kelas_mahasiswa': 'PBP D',
          'nama_aplikasi': 'le-sunsette',
          'name': 'Plain croissant',
          'amount': 6,
          'description': 'Classic type croissant with layers of buttery dough, each bite reveals a harmony of flaky and melted buttery. Savor the simplicity of pure delight – the perfect companion to your morning coffee or a snack',
          'price': 35000
       }

       return render(request, "main.html", context)
     ```

3) Buka berkas `main.html` yang dibuat sebelumnya, ubah tampilannya dengan penambahan context (kreasikan bentuk layouting yang diinginkan)
</details>

<details>
  <summary>Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.</summary>

  1) Buat berkas `urls.py` di dalam direktori `main` dan isi dengan kode berikut:
     ```python
     from django.urls import path
     from main.views import show_main

     app_name = 'main'
     urlpatterns = [
       path('', show_main, name='show_main'),
     ]
     ```
</details>

<details>
  <summary>Melakukan routing pada proyek agar dapat menjalankan aplikasi main.</summary>
  
  1) Buka berkas `urls.py` di dalam direktori `le_sunsette` dan impor fungsi `include`:
     ```python
     ...
     from django.urls import path, include
     ...
     ```
  2) Tambahkan rute URL untuk ke `main` dengan menambahkan `from django.urls import path, include` untuk variabel `urlpatterns`, seperti:
     ```python
     urlpatterns = [
       ...
       path('main/', include('main.urls')),
       ...
     ]
     ```
  3) Buka [http://localhost:8000/main/](http://localhost:8000/main/) untuk mengakses hasil pekerjaan (pastikan project sudah di-run)
</details>

<details>
  <summary>Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.</summary>

  1) Buat akun Adaptable.io menggunakan akun Github yang membuat repository pada tahap awal
  2) Setelah login, klik `New App` dan pilih `Connect an Existing Repository`
  3) Pilih repository `le-sunsette` dan klik pilihan branch `main`
  4) Kemudian, pilih template template deployment `Python App Template`
  5) Pilih database type `PostgreSQL`
  6) Pilih versi python sesuai dengan spesifikasi aplikasi, jalankan `python --version` untuk mengecek versi python. (Saya menggunakan versi `3.11`)
  7) Pada bagian start command, masukkan `python manage.py migrate && gunicorn le_sunsette.wsgi`
  8) Masukkan nama aplikasi (nama aplikasi juga sekaligus menjadi nama domain website proyek ini)
  9) Centang bagian `HTTP Listener on PORT`, lalu klik `DEPLOY APP`
</details>

<details>
  <summary>Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.</summary>

  1) Update `README.md` dengan tautan hasil deploy dan jawab pertanyaan yang diberikan
</details>


## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![bagan](https://cdn.discordapp.com/attachments/811595942159056919/1151334804097347604/image.png)
Ketika client mengakses aplikasi Django melalui browser, browser menerima HTTP Request yang akan diteruskan oleh Django ke `urls.py` untuk dicocokan pattern url-nya. Setelah ditemukan url yang cocok, request akan diteruskan ke `views.py` yang sesuai. Views.py akan melakukan rendering berdasarkan request sekaligus mengambil data dari database melalui `models.py` dan mengembalikan response berupa `<filename>.html (berkas html).`


## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Penggunaan virtual environmemt pada proyek Django sangat direkomendasikan karena virtual environment membuat lingkungan atau modul yang spesifik dan terisolasi. Artinya, setiap proyek memiliki virtual environment-nya masing-masing sehingga depedensi yang sudah dibuat tidak akan terpengaruh faktor luar (contohnya terjadi perubahan versi yang menyebabkan ketidakcocokan versi jika terjadi perubahan kode). 

Sebenarnya pembuatan aplikasi web berbasis Django tanpa menggunakan virtual environment bisa-bisa saja (tetapi sangat tidak direkomendasikan) dan memungkinkan terjadi konflik versi (perlu mengunduh lagi versi Django yang sesuai). Virtual environment hanya berperan "membantu" dalam pengerjaan berbagai proyek Django, bukan sebagai keharusan.


## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model, View, Data) merupakan konsep arsitektur dalam pembuatan aplikasi yang memisahkan kode menjadi tiga bagian, yaitu:
1. Model: Bagian yang berperan untuk mengelola data (berhubungan langsung dengan database)
2. View: Bagian yang berperan untuk menampilkan informasi dan tampilan kepada pengguna
3. Controller: Bagian yang berperan untuk menghubungkan model dan view untuk memproses logic dan proses request 

MVT (Model, View, Template) merupakan konsep arsitektur dalam pembuatan aplikasi yang memisahkan kode menjadi tiga bagian, yaitu:
1. Model: Bagian yang berperan untuk mengelola data (berhubungan langsung dengan database)
2. View: Bagian yang berperan untuk mengontrol logic yang berhubungan dengan menerima request dan mengembalikan response (rendering template berdasarkan request)
3. Template: Bagian yang berperan untuk menampilkan tampilan kepada pengguna 

MVVM (Model, View, ViewModel) merupakan konsep arsitektur dalam pembuatan aplikasi yang memisahkan kode menjadi tiga bagian, yaitu:
1. Model: Bagian yang berperan untuk mengelola data
2. View: Berperan sebagai pengatur bagian informasi akan ditampilkan kepada penggunana
3. ViewModel: Bagian yang berperan sebagai perantara model dan view, spesifiknya adalah mengelola data pada model sehingga dapat ditampilkan pada view.



# <a id="3">Tugas 3</a>
## 1. Apa perbedaan antara form POST dan form GET dalam Django?
Form `POST` umumnya digunakan untuk menambahkan data dari suatu database melalui pengiriman data input (berbentuk request), jika request valid, maka database akan menambahkan data baru sesuai input. 

Form `GET` umumnya digunakan untuk mengambil data dari database (server) ke user tanpa mengubah apapun yang ada di database 


## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML (Extensible Markup Language) merupakan salah satu format data delivery yang membentuk struktur seperti tree yang dimulai dari root (sebagai parent), kemudian branch, sampai akhirnya pada leaves. XML dibuat sedemikian sepf-descriptive yang informasinya dibungkus di dalam tag. 

JSON (JavaScript Object Notation) merupakan salah satu format data delivery yang membentuk struktur seperti dictionary yang juga dibuat sedemikan rupa agar self-describing. Data JSON disimpan pada key-value pair sehingga data delivery menggunakan JSON lebih ringan daripada bentuk tag pada XML. 

HTML umumnya tidak digunakan untuk menyajikan data informatif, melainkan untuk menampilkan kerangka atau struktur dari halaman website dan data yang akan disajikan ke dan web tersebut. Maka dari itu, HTML lebih sering digunakan untuk menyajikan data yang akan dilihat langsung oleh client.


## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON lebih sering digunakan dalam pertukaran data antara aplikasi web modern adalah karena struktur dictionary pada JSON lebih sederhana oleh mesin karena menggunakan key-value pair. Selain itu, format JSON yang menggunakan text lebih mudah di-parsing daripada XML yang perlu menggunakan tag. Ditambah lagi, strukturnya yang sederhana membuat ukuran file JSON lebih kecil sehingga sering kali menjadi pilihan dalam format data delivery pada suatu aplikasi web.


## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
<details>
  <summary>Persiapan awal sebelum membuat form: membuat kerangka base.html</summary>

  1) Pastikan program sudah menjalankan environment, jika belum jalankan dengan command
     ```
     env\Scripts\activate.bat
     ```
  2) Buka berkas `urls.py` pada direktori `le_sunsette`, kemudian ubah path `main/` menjadi `''`
      ```python
      urlpatterns = [
         path('', include('main.urls')),
         path('admin/', admin.site.urls),
      ]
      ```
   3) Buat direktori `templates` pada root folder, di dalamnya buat berkas bernama `base.html` dan isi dengan
      ```html
      {% load static %}
      <!DOCTYPE html>
      <html lang="en">
         <head>
            <meta charset="UTF-8" />
            <meta
               name="viewport"
               content="width=device-width, initial-scale=1.0"
            />
               <script src="https://cdn.tailwindcss.com"></script>
         
               <!-- font download -->
               <link rel="preconnect" href="https://fonts.googleapis.com">
               <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
               <link href="https://fonts.googleapis.com/css2?family=Lora&family=Montserrat&family=Poppins:wght@500&display=swap" rel="stylesheet">

               {% block meta %}
               {% endblock meta %}
         </head>

         <body>
            <header class="flex flex-col justify-center px-5 py-[100px] bg-gradient-to-r from-[#010413] to-[#0a1f2b] text-center align-center text-[#f5f5f5] gap-2" style="font-family: Lora, serif">
               <h1 class="text-4xl font-semibold" >{{nama_aplikasi}}</h1>
               <h1 class="text-[18px] text-gray-300 font-normal">Only serves authentic french cousine</h1>
            </header>
            
            {% block content %}
            {% endblock content %}

            <footer class="flex flex-col px-[80px] font-semibold">
               <p>Nama: {{nama_mahasiswa}}</p>
               <p>Kelas: {{kelas_mahasiswa}}</p>
            </footer>
         </body>
      </html>
      ```
   4) Hapus tag `header`, `footer`, dan `script` (yang menambahkan play CDN tailwind) pada `main.html` karena sudah dipindahkan ke base.html

   5) Buka berkas `settings.py` pada direktori `le_sunsette`, tambahkan kode pada variabel `TEMPLATES`
      ```python
      ...
      TEMPLATES = [
         {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
            'APP_DIRS': True,
            ...
         }
      ]
      ...
      ```
</details>

<details>
  <summary>Membuat input form untuk menambahkan objek model pada app sebelumnya</summary>

   1) Buat berkas `forms.py` pada direktori `main`, isi dengan kode berikut
      ```python
      from django.forms import ModelForm
      from main.models import Item

      class ProductForm(ModelForm):
         class Meta:
         model = Item
         fields = ["name", "amount", "description", "price"]
      ```
   2) Pada tahap ini saya juga menambahkan styling pada form menggunakan widgets (dapat ditambahkan di bawah line fields)
      ```python
      ...
      widgets = {
            "name": TextInput(attrs={
                'class': 'min-w-[370px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
            }),
            "amount": NumberInput(attrs={
                'class': 'min-w-[370px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
                'min': 1
            }),
            "description": Textarea(attrs={
                'class': 'min-w-[370px] max-h-[150px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
            }),
            "price": NumberInput(attrs={
                'class': 'min-w-[370px] border-2 focus:bg-gray-100 px-[12px] py-[6px]',
                'min': 0.01
            })
        }
      ```
   3) Buka berkas `views.py` pada direktori `main`, import kode berikut
      ```python
      from django.http import HttpResponseRedirect
      from main.forms import ProductForm
      from django.urls import reverse
      ```
   4) Buat fungsi baru bernama add_item sebagai berikut
      ```python
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
      ```
   5) Buat berkas `add_item.html` pada subdirektori `main/templates` (routing akan diurus nanti), tambahkan kode berikut
      ```html
      {% extends 'base.html' %}

      {% block content %}

      <section class="flex flex-col px-[60px] py-[30px] gap-[20px] items-center">
         <h1 class="text-2xl font-semibold justify-center">Add New Menu</h1>

         <form method="POST">
            {% csrf_token %}
            <table class="'flex w-full">
                  <tbody class="flex flex-col w-full">
                     <tr>
                        <td>
                              <h1 class="font-medium">Name</h1>
                        </td>
                     </tr>
            
                     <tr class="mb-5">
                        <td>
                              {{form.name}}
                        </td>
                     </tr>
            
                     <tr>
                        <td>
                              <h1 class="font-medium">Amount</h1>
                        </td>
                     </tr>
            
                     <tr class="mb-5">
                        <td>
                              {{form.amount}}
                        </td>
                     </tr>

                     <tr>
                        <td>
                              <h1 class="font-medium">Description</h1>
                        </td>
                     </tr>
            
                     <tr class="mb-5">
                        <td>
                              {{form.description}}
                        </td>
                     </tr>

                     <tr>
                        <td>
                              <h1 class="font-medium">Price</h1>
                        </td>
                     </tr>
            
                     <tr class="mb-5">
                        <td>
                              {{form.price}}
                        </td>
                     </tr>
                     
                     <tr class="flex justify-center w-full bg-[#010413] text-[#f5f5f5] h-[35px] items-center rounded-[6px]">
                        <td>
                              <input type="submit" value="Add Menu"/>
                        </td>
                     </tr>
                  </tbody>
            </table>
         </form>
      </section>

      {% endblock %}
      ```
   6) Ubah isi berkas `main.html` sehingga menyajikan tabel (pada tugas sebelumnya menyajikan card) serta tombol untuk menambahkan Item (styling bersifat opsional)
      ```html
      {% extends 'base.html' %}

      {% block content %}

      <main class="flex flex-col px-[80px] py-[50px] gap-[30px]">
         <section class="flex text-[14px] justify-center">

            <a href="{% url 'main:add_item' %}">
                  <button class="bg-[#0a1f2b] text-[#f5f5f5] px-[24px] py-[12px] rounded-[6px] text-[16px]">
                     Add Menu
                  </button>
            </a>
         </section>

         <!-- reference: https://fedingo.com/how-to-get-length-of-list-in-django-template/ -->
         <h1 class="flex justify-center text-[20px] font-medium">We have {{menus|length}} unique menu(s) here</h1>

         <table class="flex flex-col w-full border-gray-300 border-[1px] rounded-[12px] px-[25px] py-[20px]">
            <thead class="flex flex-col w-full border-b-gray-300 border-b-[1px] pb-[20px] px-[12px]">
                  <tr class="flex  text-center justify-center items-center">
                     <th class="flex w-full justify-center">Name</th>
                     <th class="flex w-full justify-center">Amount</th>
                     <th class="flex w-full justify-center">Description</th>
                     <th class="flex w-full justify-center">Price</th>
                  </tr>
            </thead>

            <tbody class="flex flex-col w-full gap-[14px] pt-[20px] px-[12px]">
                  {% for menu in menus %}
                  <tr class="flex text-center justify-center items-center">
                     <td class="flex w-full justify-center">{{menu.name}}</td>
                     <td class="flex w-full justify-center">{{menu.amount}}</td>
                     <td class="flex w-full justify-center">{{menu.description}}</td>
                     <td class="flex w-full justify-center">${{menu.price}}</td>
                  </tr>
                  {% endfor %}
            </tbody>
         </table>
      </main>

      {% endblock content %}
      ```
</details>

<details>
  <summary>Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID</summary>

  1) Buka berkas `views.py` pada direktori `main`, tambahkan fungsi sesuai ketentuan, hasil akhirnya akan menjadi
      ```python
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
      ```
</details>

<details>
  <summary>Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2</summary>

   1) Buka berkas `urls.py` pada direktori `main`, import semua fungsi yang sudah dibuat
      ```python
      from main.views import show_main, add_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
      ```
   2) Tambahkan fungsi yang sudah di-import ke dalam variabel `urlpatterns` sehingga menjadi
      ```python
      urlpatterns = [
      path('', show_main, name='show_main'),
      path('add_item', add_item, name='add_item'),
      path('xml/', show_xml, name='show_xml'), 
      path('json/', show_json, name='show_json'),
      path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
      ]
      ```
</details>

## 5. Screenshot Postman (pastikan anda memiliki akses internet untuk melihat screenshot)
1) HTML
![html](https://cdn.discordapp.com/attachments/811595942159056919/1153872414208426034/image.png)
2) XML
![xml](https://cdn.discordapp.com/attachments/811595942159056919/1153872654927929455/image.png)
3) JSON
![json](https://cdn.discordapp.com/attachments/811595942159056919/1153870019411849347/image.png)
4) XML by ID
![xml-by-id](https://cdn.discordapp.com/attachments/811595942159056919/1153872630869397565/image.png)
5) JSON by ID
![json-by-id](https://cdn.discordapp.com/attachments/811595942159056919/1153872647604670484/image.png)



# <a id="4">Tugas 4</a>
## 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya? 
Django `UserCreationForm` merupakan built-in class yang disediakan Django untuk membuat form pembuatan (atau pendaftaran) user.
`Kelebihan`: Pembuatan form pendaftaran user semakin mudah karena fitur fungsionalitas, field username dan password, ketentuan password, semuanya sudah disediakan oleh Django
`Kekurangan`: Sulit untuk melakukan kostumisasi karena form sudah disediakan dan "ditetapkan" demikian sehingga ketika ingin membuat form yang bersifat custom akan lebih sulit (jika alur yang diinginkan kompleks, lebih mudah membuat form sendiri dari awal)


## 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
`Autentikasi` merupakan proses verifikasi identitas pengguna, mengecek pengguna tersebut benar ada dan yang mengakses adalah "orang tersebut" (dapat dicek melalui verifikasi kecocokan password)
`Otorisasi` merupakan proses memutuskan kebolehan dan ketidakbolehan pengguna (yang sudah terautentikasi) dalam mengakses suatu resource ataupun melakukan suatu aksi, misalnya user umum tidak mendapatkan hak mengakses laman edit yang biasanya hanya dimiliki oleh admin. Otoritasi dilakukan agar resource yang dibatasi aksesnya tidak bocor ke pihak yang tidak seharusnya mengakses agar tidak disalahgunakan.


## 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Dalam konteks aplikasi web, `cookies` merupakan media penyimpanan rekam jejak pengguna pada suatu browser dengan kapasistas kecil, ~4 KB sumber tutorial 3 PBP. `Pemanfaatan cookie pada Django` adalah pada penerapan session based authentication, yaitu ketika seorang pengguna berhasil terautentikasi, Django akan membuat suatu sesi dari user yang tersimpan pada cookies setelah mereka terautentikasi. Cookies tersebut menyimpan informasi mengenai kunjungan user, selama data tersebut masih ada (belum expired), user tersebut akan dianggap masih terautentikasi dan data seperti preferensi situs, konten yang sesuai, dan sebagainya masih dapat diakses oleh user.


## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Sebenarnya penggunaan cookies secara default masih terdapat celah untuk dilakukan peretasan, salah satu contohnya adalah CSRF (Cross Site Request Forgery). Singkatnya, serangan CSRF memungkinkan pengiriman request oleh penyerang kepada suatu aplikasi website melalui aplikasi website yang sedang terautentikasi oleh user. Ini artinya, tindakan atau permintaan request yang dilakukan sebenarnya tidak dikehendaki oleh user (bahkan bisa menjadi tindakan yang merugikan user).

## 5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
<details>
  <summary>Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar</summary>

   1) Jalankan virtual environment terlebih dahulu
   2) Buka berkas `views.py` pada subdirektori `main`, kemudian import
   ```python
   from django.shortcuts import redirect
   from django.contrib.auth.forms import UserCreationForm
   from django.contrib import messages  
   ```
   3) Buat sebuah fungsi `register` sebagai berikut
   ```python
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
   ```
   4) Buat berkas `register.html` pada subdirektori `main/templates`, isi berkas dapat disesuaikan dengan styling yang diinginkan (lihat pada berkas terkait)
   5) Buka berkas `urls.py` pada direktori `main`, import fungsi register yang sudah dibuat
   ```python
   from main.views import register
   ```
   6) Tambahkan kode berikut ke dalam variabel `urlpatterns`
   ```python
   ...
   path('register/', register, name='register'),
   ...
   ```
   7) Buka berkas `views.py` pada subdirektori `main`, kemudian import
   ```python
   from django.contrib.auth import authenticate, login
   ```
   8) Buat sebuah fungsi `login_user` sebagai berikut
   ```python
   def login_user(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('main:show_main')
      else:
         messages.info(request, 'Sorry, incorrect username or password. Please try again.')
   context = {}
   return render(request, 'login.html', context)
   ```
   9) Buat berkas `login.html` pada subdirektori `main/templates`, isi berkas dapat disesuaikan dengan styling yang diinginkan (lihat pada berkas terkait)
   10) Buka berkas `urls.py` pada direktori `main`, import fungsi login_user yang sudah dibuat
   ```python
   from main.views import login_user
   ```
   11) Tambahkan kode berikut ke dalam variabel `urlpatterns`
   ```python
   ...
   path('login/', login_user, name='login'),
   ...
   ```
   12) Buka kembali berkas `views.py` pada subdirektori `main`, kemudian import
   ```python
   from django.contrib.auth import logout
   ```
   13) Buat sebuah fungsi `logout` sebagai berikut
   ```python
   def logout_user(request):
      logout(request)
      return redirect('main:login')
   ```
   14) Tambahkan button logout di berkas `main.html` pada subdirektori `main/template` 
   15) Buka kembali berkas `urls.py` pada direktori `main`, import fungsi logout_user yang sudah dibuat
   ```python
   from main.views import logout_user
   ```
   16) Tambahkan kode berikut ke dalam variabel `urlpatterns`
   ```python
   ...
   path('logout/', logout_user, name='logout'),
   ...
   ```
   17) Buka berkas `views.py` pada direktori `main`, tambahkan import berikut
   ```python
   from django.contrib.auth.decorators import login_required
   ```
   18) Tambahkan kode berikut persis di atas line `def show_main(request):`
   ```python
   @login_required(login_url='/login')
   ```
</details>

<details>
   <summary> Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal</summary>

   (DISCLAIMER: kerjakan setelah checklist berikutnya agar setiap user memiliki item uniknya masing-masing)
   1) Jalankan perintah `python manage.py runserver` dan buka `http://localhost:8000/`
   2) Registrasi user baru dengan menginput `username` dan `password` sesuai ketentuan
   3) Setelah berhasil membuat user, login dengan user tersebut lalu klik tombol `Add Menu`
   4) Isi input form tersebut lalu tekan `Submit`, ulangi langkah ini sebanyak 3 kali sehingga terdapat 3 menu berbeda
   5) Klik tombol `logout`
   6) Ulangi langkah 2 - 4 (pada akhirnya akan terdapat 2 user dengan masing-masing memiliki 3 dummy data)
</details>

<details>
   <summary>Menghubungkan model Item dengan User</summary>

   1) Buka berkas `models.py` pada direktori `main`, tambahkan import berikut
   ```python
   from django.contrib.auth.models import User
   ```
   2) Pada model product yang sudah dibuat, tambahkan potongan kode berikut
   ```python
   class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
   ...
   ```
   3) Buka berkas `views.py` pada direktori `main`, ubah potongan kode pada fungsi `create_product` menjadi
   ```python
   def create_product(request):
      form = ProductForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
         product = form.save(commit=False)
         product.user = request.user
         product.save()
         return HttpResponseRedirect(reverse('main:show_main'))
      ...
   ```
   4) Ubah fungsi `show_main` menjadi
   ```python
   def show_main(request):
      products = Product.objects.filter(user=request.user)

      context = {
         'name': request.user.username,
      ...
   ...
   ```
   5) Simpan semua perubahan dan jalankan kode
   ```
   python manage.py makemigrations
   ```
   6) Saat muncul error, ketik `1`, lalu `1` lagi
   7) Jalankan kode berikut
   ```
   python manage.py migrate
   ```
</details>

<details>
   <summary>Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi</summary>

   1) Buka berkas `views.py` pada direktori `main`, tambahkan import berikut
   ```python
   import datetime
   from django.http import HttpResponseRedirect
   from django.urls import reverse
   ```
   2) Pada fungsi `login_user`, ubah blok code `if user is not None` menjadi
   ```python
   ...
   if user is not None:
      login(request, user)
      response = HttpResponseRedirect(reverse("main:show_main")) 
      response.set_cookie('last_login', str(datetime.datetime.now()))
      return response
   ...
   ```
   3) Pada fungsi `show_main`, tambahkan potongan kode berikut ke dalam variabel `context`
   ```python
   ...
   last_login': request.COOKIES['last_login']
   ...
   ```
   4) Ubah fungsi `logout_user` menjadi berikut
   ```python
   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
   ```
   5) Tambahkan potongan kode berikut ke dalam `main.html` (letak bebas, bisa mengikuti repo ini)
   ```html
   ...
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ...
   ```
</details>