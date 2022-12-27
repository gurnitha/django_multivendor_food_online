# django_multivendor_food_online

Membuat multivendor ecommerce food online menggunakan django
Link to course:
https://www.udemy.com/course/python-django-real-world-project-multi-vendor-restaurant/learn/lecture

## 01. Intro

## 02. Getting started

### 1. Persiapan

- membuat root direktori
- memastikan versi python, pip, dan virtualenv

### 2. Menginstal django

- membuat virtual environment
- mengaktifkan virtual environment
- menginstal django versi 3.2
- meng-upgrade pip

### 3. Membuat django project

- membuat django project
- membuat file requirement.txt

### 4. Membuat repositori

- membuat repositori pada github
- meng-clone repositori

### 5. Menjalankan lokal server

- menjalankan lokal server
- menjalankan project pada browser

### 6. Meng-upload file ke repositori

- membuat git commit dan upload file ke repositori
- memastikan keberhasilan meng-upload file

### 7. Membuat hallo world

- Membuat home path
- Membuat def home method
- Git commit

### 8. Membuat home page

- Membuat folder templates
- Mengakses templates dari settings.py
- Membuat file templates/home.html
- Membuat home page
- Memodifikasi def home method
- Testing
- Git commit 

### 9. Membuat superuser

- Menjalankan migrasi
- Membuat superuser
- Testing
- Git commit

### 10. Menambahkan dan loading static files serta template 

- Membuat static folder: main/static
- Menambahkan static files
- Setting up static_root dan staticfiles_dirs
- Menambahkan template pada home page
- Loading static files
- Testing
- Git commit

## 03. Setting up PostgreSQL db

### 1. Membuat konfigurasi db

- Download PostgreSQL
- Instal PostgreSQL
- Membuat db
- Konek db dgn aplikasi
- Install psycopg2 module
- Jalankan migrasi
- Membuat superuser
- Testing
- Git commit

### 2. Melindungi konfigurasi parameter db, SECRET_KEY, dan DEBUG

- Instal python-decouple
- Membuat .env file
- Membuat konfigurasi parameter SECRET_KEY, DEBUG, dan DB pada .env
- Memasang parameter konfigurasi.env pada settings.py
- Testing
- Git commit 

### 3. Membuat .env-sample file

- Membuat file .env-sample
- Git commit

### 4. Fixing error pada settings.py tentang db parameter

- BEFORE
- 'DB_NAME': config('DB_NAME'),
- 'DB_USER': config('DB_USER'),
- 'DB_PASSWORD': config('DB_PASSWORD'),
- 'DB_HOST': config('DB_HOST')

- AFTER
- 'NAME': config('DB_NAME'),
- 'USER': config('DB_USER'),
- 'PASSWORD': config('DB_PASSWORD'),
- 'HOST': config('DB_HOST')
