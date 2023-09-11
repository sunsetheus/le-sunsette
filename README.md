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
     ```p
     django-admin startproject le_sunsette .
     ```
  8) Untuk keperluan deployment, tambahkan `"*"` untuk bagian `ALLOWED_HOSTS` pada file `settings.py`, seperti:
     ```
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
<summary>
  
Membuat aplikasi dengan nama `main` pada proyek tersebut. 
</summary>

  1) Buat direktori `main` untuk membuat aplikasi baru dengan menjalankan:
     ```
     python manage.py startapp main
     ```
  2) Tambahkan `'main'` untuk bagian `INSTALLED_APPS` pada file `settings.py`, seperti:
     ```
     INSTALLED_APPS = [
       ...,
       'main',
       ...
     ]
     ```
</details>

<details>
<summary>
  
Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`.
</summary>

  1) Buka berkas `urls.py` di dalam direktori `le_sunsette` dan impor fungsi `include`:
     ```python
     ...
     from django.urls import path, include
     ...
     ```



</details>

<details><summary></summary></details>

<details><summary></summary></details>

<details><summary></summary></details>

<details><summary></summary></details>

<details><summary></summary></details>


    
  
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
-

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
-

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
-
