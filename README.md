# Le-Sunsette
[Preview Website]()

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial) 
<details>
  <summary>Membuat sebuah proyek Django baru. (pov pengguna Windows)</summary>
  
  1) Buat direktori bernama `Le-Sunsette` pada local.
  2) Di dalam direktori tersebut, buka command prompt dan buat virtual environemnt baru dengan menjalankan:
     ```
     python -m venv env
     ```
  3) Aktifkan virtual environtment
     ```
     env\Scripts\activate.bat
     ```
  4) Virtual environment berhasil diaktifkan ditandai dengan `(env)` pada bagian awal input command line. Pastikan virtual environment   tetap berjalan.
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
  <summary>Membuat aplikasi dengan nama main pada proyek tersebut (langkah 1).</summary>
  
  1) Buat direktori `main` untuk membuat aplikasi baru dengan menjalankan:
     ```
     python manage.py startapp main
     ```
  2) Tambahkan `'main'` untuk variabel `INSTALLED_APPS` pada file `settings.py`, seperti:
     ```
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
  <summary>Membuat model pada aplikasi main (langkah 2).</summary>
  
  1) Buka berkas `models.py` pada direktori `main` dan isi dengan kode:
     ```pyhton
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
  <summary>Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. (nomor 3)</summary>

  1) Tambahkan baris impor berikut pada berkas `views.py` di direktori aplikasi `main`:
     ```python
     from django.shortcuts import render
     ```
 
  2) Tambahkan fungsi `show-main` yang menampilkan nama aplikasi, serta nama dan kelas mahasiswa
     ```
     def show_main(request):
       context = {
          'nama_mahasiswa': 'William',
          'kelas_mahasiswa': 'PBP D'
          'nama_aplikasi: 'le-sunsette',
          'name': 'Plain croissant'
          'amount': 6
          'description: 'Classic type croissant with layers of buttery dough, each bite reveals a harmony of flaky and melted buttery. Savor the simplicity of pure delight – the perfect companion to your morning coffee or a snack'
          'price': 35000
       }

     return render(request, "main.html", context)
     ```

3) Buka berkas `main.html` yang dibuat sebelumnya, ubah tampilannya dengan penambahan context (kreasikan bentuk layouting yang diinginkan)
     
</details>

<details>
  <summary>Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py (langkah 4).</summary>

  1) Buat berkas `urls.py` di dalam direktori `main` dan isi dengan kode berikut:
     ```
     from django.urls import path
     from main.views import show_main

     app_name = 'main'
     urlpatterns = [
       path('', show_main, name='show_main'),
     ]
     ```

</details>

<details>
  <summary>Melakukan routing pada proyek agar dapat menjalankan aplikasi main (langkah 5).</summary>
  
  1) Buka berkas `urls.py` di dalam direktori `le_sunsette` dan impor fungsi `include`:
     ```python
     ...
     from django.urls import path, include
     ...
     ```
  2) Tambahkan rute URL untuk ke `main` dengan menambahkan `from django.urls import path, include` untuk variabel `urlpatterns`, seperti:
     ```
     urlpatterns = [
       ...
       path('main/', include('main.urls')),
       ...
     ]
     ```
</details>

<details>
  <summary>Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
  
  
  </summary>


</details>

<details>
  <summary>Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.</summary>


</details>


    
  
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
-

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
-

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
-
