Nama: Alfian Nugraha
NIM: 2609116084
Kelas: C

# SISTEM PENGELOLAAN SAMPAH YANG ADA DI GUNUNG 

Penjelasan untuk kode
import os, berfungsi untuk membersihkan layar
import time, berfungsi sebagai memberi jeda pada program
from prettytable import prettytable, berfungsi untuk membuat tabel menjadi rapi
import pwinput, berfungsi apabila kita memasukan password password tersebut akan tampil menjadi bintang bintang 

user, adalah daftar akun yang di dalamnya itu berisi username,password,dan role di dalam kode saya itu ada dua role yaitu admin dan user 

registrasi(), adalah dimana kita disuruh membuat akun baru, apabila username nya kosong bearti username sudah dipakai dan apabila password kurang dari 4 akun di tolak dan apabila berhasil akun akan di simpan dengan role user 

login(), adalah dimana kita disini disuruh memasukan username dan password yang telah kita buat lalu di cocokan dengan daftar user apabila cocok dia akan kasitau role nya dan apabila tidak cocok tidak memberitahu apapun

lihat_sampah(), berfungsi sebagai menampilkan data sampah dalam bentuk tabel
tambah_sampah(), berfungsi sebagai nambah data sampah baru dan berat dari sampah nya haru lebih dari 0 
hapus_sampah(), berfungsi sebagai menghapus data sampah bedasarkan ID yang dimasukkan 
menu_admin(), disini menampilkan pilihan tambah data, ubah data, hapus data, dan logout
menu_user(), nah untuk menu ini hanya bisa lihat dan logout 

<img width="630" height="288" alt="Screenshot 2026-10-05 032341" src="https://github.com/user-attachments/assets/b504d397-56a5-4efe-a234-92ef5b159f28" />

<img width="592" height="318" alt="Screenshot 2026-10-05 032424" src="https://github.com/user-attachments/assets/f92fffd0-b7bc-4ad8-af01-6652791e4c00" />

<img width="611" height="313" alt="Screenshot 2026-10-05 032451" src="https://github.com/user-attachments/assets/888e70b0-2b59-4d64-bb8e-78fa35da98d2" />

<img width="940" height="707" alt="Screenshot 2026-10-05 040323" src="https://github.com/user-attachments/assets/99dde1ae-8540-4b15-9f30-7ebd5af447af" />

Penjelasan untuk flowchart 

yang pertama disini kita disuruh milih angka 1 sampai 3 
pilih 1 (Login), disini kita disuruh memasukan username dan password kalo benar program lihat kita itu sebagai admin atau bukan, kalo jadi admin kita bisa (tambah data, lihat data, ubah data, dan hapus data) dan apabila tidak menjadi admin hanya bisa melihat data

pilih 2 (Registrasi), disini kita disuruh membuat akun baru apabila sudah membuat akun akun nya itu bakalan di simpan sebagai user, lalu balik lagi ke menu awal 

pilih 3 (Keluar), disini program akan berhenti 

pilih (Selain Itu), nah disini harus milih lagi dari dari angka 1-3



