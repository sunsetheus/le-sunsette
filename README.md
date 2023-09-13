# Le-Sunsette
[Preview Website]()

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
