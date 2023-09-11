# Le-Sunsette
[Preview Website]()

<details>
<summary>## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial) </summary>
  
  <details>
  <summary>
    
  - [x] Membuat sebuah proyek Django baru. (pov pengguna Windows)</summary>
  Buat direktori bernama `Le-Sunsette` pada local.
  Di dalam direktori tersebut, buka command prompt dan buat virtual environemnt baru dengan menjalankan:
    ```
    python -m venv env
    ```
  Aktifkan virtual environtment
    ```
    env\Scripts\activate.bat
    ```
  - Virtual environment berhasil diaktifkan ditandai dengan `(env)` pada bagian awal input command line. Pastikan virtual environment tetap berjalan.
  - Di direktori yang sama, buat berkas `requirements.txt` yang berisi:
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
  - Unduh depedencies dengan menjalankan kode di command prompt
    ```p
    pip install -r requirements.txt
    ```
  - Pada direktori yang sama, buat direktori project Django bernama `le_sunsette` dengan menjalankan perintah (pastikan terdapat `.` pada akhir kode):
    ```p
    django-admin startproject le_sunsette .
    ```
  - Untuk keperluan deployment, tambahkan `"*"` bagian `ALLOWED_HOSTS` pada file `settings.py`, seperti:
    ```
    ...
    ALLOWED_HOSTS = ["*"]
    ...
    ```
  - Jalankan

</details>
    
  
  
- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
[x] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
[x]
[x]
[x]
[x]
[x]


</details>

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
-

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
-

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
-
