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

### 10.3 Template Inheritance Base Html

- modified:   README.md
- modified:   app/accounts/views.py (render html)
- new file:   templates/base.html (template inheritance django)
- modified:   templates/home.html (extends base.html to reder home page)
- new file:   templates/includes/footer.html (include footer)
- new file:   templates/includes/navbar.html (include footer)
- Testing: berhasil
- Git commit

### 10.4 User Registration Form Template

- modified:   app/accounts/views.py (render accounts/registerUser.html)
- new file:   templates/accounts/registerUser.html (membuat folder (accounts) dan file baru (registerUser.html) dan menambahkan template form register)
- modified:   templates/base.html (mengembalikan file javascript dari footer)
- Testing: berhasil
- Git commit

### 10.5 Menggunakan class Meta verbose_name to rename CustomUser to Users in admin panel

- Tambahkan class Meta dan verbose_name = "User" pada CustomUser class
- Testing: berhasil berubah dari 'Custom users' menjadi 'Users'
- Git commit

### 10.6.1 User Registration Form Implementation - Part 1: testing UserRegistrationForm

- modified:   README.md
- new file:   app/accounts/forms.py (membuat file baru forms.py dan buat UserRegistrationForm class)
- modified:   app/accounts/views.py (load UserRegistrationForm)
- modified:   templates/accounts/registerUser.html (load form)
- Testing: berhasil
- Git commit

### 10.6.2 User Registration Form Implementation - Part 2: Loading form instan pada RegisterUser form

- modified:   app/accounts/forms.py (menambahkan password dan confirm_password field)
- modified:   app/accounts/urls.py (koreksi nama path dari registeruer menjadi registeruser)
- modified:   templates/accounts/registerUser.html (loading form instan)
- Testing: berhasil
- Git commit

### 10.6.3 User Registration Form Implementation - Part 3: Membuat basic user register logik pada views

- modified:   README.md
- modified:   app/accounts/views.py (membuat basik logik)
- modified:   templates/accounts/registerUser.html (menambahkan csrf_token pada form)
- Testing: berhasil merekam data dari form
- Git commit

### 10.6.4 User Registration Form Implementation - Part 4: Membuat user register logik pada views

- modified:   app/accounts/forms.py (deleting phone_number field)
- modified:   app/accounts/signals.py (disable print for testing)
- modified:   app/accounts/views.py (Membuat user register logik pada views)
- modified:   templates/accounts/registerUser.html (modifikasi form)
- Testing: berhasil
- Git commit

### 10.6.5 User Registration Form Implementation - Part 5: Menambahkan role sebagai CUSTOMER pada user register logik pada views

- modified:   README.md
- modified:   app/accounts/views.py
- Testing: berhasil menambahkan role sebagai CUSTOMER pada user register
- Git commit

## 11. Hash The Password From Form

### 11.1 Hash The Password From Form - Part 1: Hash password from the views

- modified:   README.md
- modified:   app/accounts/views.py (clean data and store password in has format)
- Testing: berhasil
- Git commit

### 11.2 Hash The Password From Form - Part 2: Create user using create_method

- modified:   README.md
- modified:   app/accounts/models.py
- modified:   app/accounts/views.py
- Testing: Data pada form tetap tinggal setelah submit the form
- Git commit

### 11.3 Hash The Password From Form - Part 3: Cleaning data from the form after submitting

- modified:   README.md
- modified:   app/accounts/views.py (add this: return redirect(registeruser))
- Testing: Berhasil
- Git commit

## 12. Django Field Errors And Non Field Errors

### 12.1 Django Field Errors And Non Field Errors - Part 1: Showing field error in terminal using existing email and username

FIELD ERROR

In simple words, any errors that are associated with your model fields are called field errors.

NONE FIELD ERROR

These non field errors are the errors that are not associated with your model field, but they are associated
with your form's clean method where you raise your own custom validation errors from the form level
itself without attaching these fields into your model.
So that's what we call the non field errors.

The best example for this non field error is actually the confirm password.
So in our case, if I type a different password in this password and confirm password fields, then
this should actually give us an error saying password password do not match.

So this password has to be same.
Then we will be allowed to submit this form, otherwise we will get an error.
So that kind of error is called the non field error.

- modified:   README.md
- modified:   app/accounts/views.py (add else print(form.errors))
- Testing: berhasil
- Git commit

### 12.2 Django Field Errors And Non Field Errors - Part 2: Showing field error in form using existing email and username

- modified:   README.md
- modified:   templates/accounts/registerUser.html (looping error)
- Testing: berhasil
- Git commit

### 12.3 Django Field Errors And Non Field Errors - Part 3: Showing NONE field errors 

So field error actually should be raised from the form level.
If password is not equal to confirm password then raise an error.

For NONE FIELD ERROR, we have to use Clean Method prepares by
Django to see the error.

What hat is Clean Method?

So Django model forms by default calls the clean method behind the scenes whenever the form is triggered.
This will actually make your data clean by using some input functions.
Clean method on a field subclass is responsible for running to Python validate and run validate those

In this example, we are going to override the clean method because we want to raise the custom validation
error to know whether this password is equal to confirm password.
If they are not equal, then just throw him an error.

This super function will actually give you an ability to override this clean method, which
is a inbuilt function.

- modified:   README.md
- modified:   app/accounts/forms.py (add clean method)
- modified:   templates/accounts/registerUser.html (showing error using this: form.non_field_errors)
- Testing: berhasil
- Git commit

## 13. Django Messages

We need to actually check if we have a message or not message
If messages.
If messages and we'll be wondering how this messages is available in this register user
dot HTML because if you see this view we are not passing anything except form to this HTML.
But still we are able to access these messages. So that because of this context processors
in the settings.py file (inside the TEMPLATES).

So this context processor is something. It's kind of a function.
And when you write or when you return something inside the context processor, those module
will be available in all of your HTML files.

### 13.1 Django Messages - Part 1: Setup django messages in views and register page

- modified:   README.md
- modified:   app/accounts/views.py (setup django messages)
- modified:   templates/accounts/registerUser.html (loop messages)
- Testing: berhasil
- Git commit

### 13.2 Django Messages - Part 2: Using template inheritance (include) to show messages

- modified:   README.md
- modified:   templates/accounts/registerUser.html (include alert file)
- new file:   templates/includes/alert.html (pindahkan message codes dari register)
- Testing: berhasil
- Git commit

### 13.3 Django Messages - Part 3: Menambahkan close button page alert message

- modified:   README.md
- modified:   templates/includes/alert.html
- Testing: berhasil
- Git commit