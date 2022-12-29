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

## 04. Custom user model, Media files, dan Django signals

### 1. Membuat app baru app/accounts

- Membuat app baru dengan nama accounts
- Register app accounts pada settings.py
- Testing
- Git commit

### 2. Modified app name

- Modified nama app from name='accounts' to name='app.accounts'

## 05 Membuat Custom User

### 5.1 Membuat Custom User - Part 1: basics

- Membuat class UserManager and CustomUser

### 5.2 Membuat Custom User - Part 2: create user

- Membuat def create_user method

### 5.3 Membuat Custom User - Part 3: create superuser

- Membuat def create_superuser method

### 5.4 Membuat Custom User - Part 4: create CustomUser class

- Membuat CustomUser class

### 5.5 Membuat Custom User - Part 5: register CustomeUser to settings.py

- Register CustomUser model pada settings.py
- We need to tell Django that we are not using its default user model anymore.
- Instead, we are using our CustomUser model that we have created.
- AUTH_USER_MODEL = 'accounts.CustomUser'
- Testing
- CustomUser model membuat error karena di dalam database sudah ada tabel auth_user
- Git commit

### 5.6 Membuat Custom User - Part 6: Menghilangkan error

- Penyebab error: membuat tabel CustomUser sedangkan tabel auth_user sudah ada di dalam db
- Menghilangkan error: hapus file migrasi dan hapus database dan buat database baru
- Jalankan migrasi
- Buat superuser
- Jalankan lokal server
- Testing: customuser model tidak tampak pada admin panel
- Git commit

### 5.7 Membuat Custom User - Part 7: Register CustomUser model pada admin

- Register CustomUser model pada admin
- Testing
- Git commit

## 06. Membuat Password tidak bisa diedit

### 6.1. Membuat Password tidak bisa diedit - Part 1: Membuat CustomUserAdmin class

- Membuat CustomUserAdmin class
- Gunakan module UserAdmin sebagai parameter untuk modifikasi tampilan pada admin panel
- Buat filter: filter_horizontal = (), list_filter = (), dan fieldsets = ()
- Testing
- Git commit

### 6.2. Membuat Password tidak bisa diedit - Part 2: Kustomais tampilan pada admin panel

- Membuat filter pada fields dari CustomUserAdmin class
- Testing
- Git commit

## 07. Membuat UserProfile model

- Membuat UserProfile model
- Menginstal modul Pillow untuk gambar
- Menjalankan migrasi
- Meregistrasi UserProfile model pada admin
- Testing: link gambar tidak berfungsi karena media file belum disetup
- Git commit

## 08. Mensetup media file

- Menghapus users folder
- Membuat konfigurasi media file pada settings.py
- Pada main/urls.py import django.conf import settings
- Pada main/urls.py import django.conf.urls.static import static
- Membuat path media file pada main/urls.py
- Membuat media folder
- Mengupload ulang gambar user
- Testing: berhasil
- Git commit

## 09.Django Signals To Create User Profile

### 9.1 Django Signals To Create User Profile - Part 1: basic, create and test signals

- In app/accounts/models.py impor post_save and receiver
- Gunakan dekorator @receiver(post_save, sender=CustomUser)
- Buat mothod dengan 4 parameter: def post_save_create_profile_receiver(sender, instance, created, **kwargs):
- Testing: berhasil
- Git commit

### 9.2 Django Signals To Create User Profile - Part 2: Membuat user prifile dari admin panel secara otomatis

- Pada : def post_save_create_profile_receiver(sender, instance, created, **kwargs): 
- tambahkan ini: UserProfile.objects.create(user=instance)
- Buat user baru dari admin panel
- Testing: user profile berhasil dibuat secara otomatis
- Git commit

### 9.3 Django Signals To Create User Profile - Part 3: Upadate User profile (1)

- Tambahkan else pada: def post_save_create_profile_receiver(sender, instance, created, **kwargs):
- dan print('User profile is updated')
- Testing: berhasil
- Git commit 

### 9.4 Django Signals To Create User Profile - Part 4: Meng-update user yang profilenya telah dihapus (2)

- Update: def post_save_create_profile_receiver(sender, instance, created, **kwargs):
- dengan yang di bawah ini:
- profile = UserProfile.objects.get(CustomUser=instance)
- profile.save()
- print('User profile is updated')  
- Tesing: hapus User profile dan update user yang sama, hasil error
- Git commit

### 9.5 Django Signals To Create User Profile - Part 5: Menggunakan try block untuk atasi masalah di atas(3)

- Update: def post_save_create_profile_receiver(sender, instance, created, **kwargs):
- Gunakan try block
- Testing: berhasil
- Git commit

### 9.6 Django Signals To Create User Profile - Part 6: Menggunakan pre_save signals untuk hindari masalah di atas(4)

- Buat hal di bawah ini:
- impor pre_save signals
- @receiver(pre_save, sender=CustomUser)
- def pre_save_create_profile_receiver(sender, instance, **kwargs):
- print(instance.username, 'this user is being saved')
- Testing: berhasil
- Git commit

### 9.7 Django Signals To Create User Profile - Part 7: Memindahkan signals ke file baru signals.py(5)

- Pada app/accounts buat file baru: app/accounts/signals.py
- Pindahkan semua codes signals dari models.py ke signals.py
- Import modul dan model yang diperlukan
- Pada try block, ganti CustomUser dengan user seperti di bawah ini:
- profile = UserProfile.objects.get(CustomUser=instance)
- profile = UserProfile.objects.get(user=instance)
- Tambahkan ready() function pada app/accounts/apps.py agar signals bisa berfungsi
- Testing: berhasil (sebelumnya ada error karena CustomUser, seharusny user)
- Git commit


## 10. User registrations, Django messages and error

### 10.1 Foodonline Flowchart: penjelasan flow of chart (no codes have made)

- Penjelasan flow dari cara kerja Multi Vendor Food Online
- 1. In comming random user (registered or not register user)
- 2. If not register, he can register as customer or vendor
- REGISTER AS VENDOR
- 3. Let say he will register as vendor
- 4. A register form will be comes up
- 5. Once he registered, the admin will verify it (give him a certificate) and give the approval or reject it
- 6. Once admin approved, then he, as the vendor can login to our marketplace (note: the can distinguished vendor or customer)
- 7. If he loged in as vendor, he will be redirect to vendor dashboard
- 8. In the vendor dasboard, vendor can do CRUD operation for his: profile, location and restaurant timing
- 9. Vendor create or build menu and publish it to the marketplace (here is the critical part of the app)
- REGISTER AS CUSTOMER
- 10. Register as customer
- 11. Log in as customer
- 12. Once he loged in, he can visit the marketplace or Customer dashboard
- 13. If he go to customer dashboar, he will be able to: update profile, check order, sign out    
- 14. If he go to the marketplace, he can order the food
- 15. In the marketplace, customer can search restaurant by location (near by location) or key words (by rest name, for example)
- 16. Once he happy with the search, he will be able to order, showed the cart, and make payment
- 17. If the payment is failed, the the app will show him again the cart
- 18. Once the payment is success, the app will deduct it for the admin commision (some percentage of the amount) 
- 19. Admin will receive the commision, then clear the cart and send emil to the customer (we have take care the order)
- 20. At the same time, we will send email to the restauran that he got a new order
- 21. Once the restaurant owner open the email, the transaction can be procceded: except or reject the order

### 10.2 Membuat User registration path

- modified:   README.md
- new file:   app/accounts/urls.py (membuat path registeruser)
- modified:   app/accounts/views.py (membuat registeruser method)
- modified:   main/urls.py (include app.accounts/urls.py)
- Testing: berhasil
- Git commit

## 10.3 Template Inheritance Base Html

- modified:   README.md
- modified:   app/accounts/views.py (render html)
- new file:   templates/base.html (template inheritance django)
- modified:   templates/home.html (extends base.html to reder home page)
- new file:   templates/includes/footer.html (include footer)
- new file:   templates/includes/navbar.html (include footer)
- Testing: berhasil
- Git commit