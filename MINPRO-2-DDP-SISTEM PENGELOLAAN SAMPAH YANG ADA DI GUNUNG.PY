import os
import time
from prettytable import PrettyTable
import pwinput

users = {
    "admin": {"password": "admin", "role": "admin"},
    "user": {"password": "user123", "role": "user"},
}
sampah = {

    1: {"lokasi": "Pos 1", "jenis": "Organik", "berat": 10, "status": "Belum Diangkut"},
    2: {"lokasi": "Pos 2", "jenis": "Anorganik", "berat": 20, "status": "Sudah Diangkut"},
    3: {"lokasi": "Pos 3", "jenis": "Sampah B3", "berat": 30, "status": "Belum Diangkut"},
}


def jeda():
    input("\nTekan Enter untuk kembali ke menu...")


def bersih():
    os.system("cls" if os.name == "nt" else "clear")


def registrasi():
    print("=== REGISTRASI ===")
    username = input("Username: ").strip()
    password = pwinput.pwinput("Password: ")
    if username == "" or username in users or len(password) < 4:
        print("ahihihihihihii username nya sudah terpakai nih")
    else:
        users[username] = {"password": password, "role": "user"}
        print("uhuyy registrasi berhasil nih")


def login():
    print("=== LOGIN ===")
    username = input("Username: ").strip()
    password = pwinput.pwinput("Password: ")
    if username in users and users[username]["password"] == password:
        print("loginn berhasill nih ndut")
        time.sleep(1)
        return users[username]["role"]
    print("berhasil login ndut")


def lihat_sampah():
    print("=== DATA SAMPAH YANG ADA DI GUNUNG ===")
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Lokasi", "Jenis", "Berat (kg)", "Status"]
    for id, d in sampah.items():
        tabel.add_row([id, d["lokasi"], d["jenis"], d["berat"], d["status"]])
    print(tabel)


def tambah_sampah():
    print("=== TAMBAH DATA SAMPAH ===")
    lokasi = input("Lokasi: ").strip()
    jenis = input("Jenis sampah: ").strip()
    try:
        berat = int(input("Berat (kg): "))
    except ValueError:
        print("berat harus berupa angka ya ndut")
        return
    if lokasi == "" or jenis == "" or berat <= 0:
        print("data tidak boleh kosong ya ndut dan berat harus lebih dari 0")
        return
    id = max(sampah, default=0) + 1
    sampah[id] = {"lokasi": lokasi, "jenis": jenis, "berat": berat, "status": "Belum Diangkut"}
    print("Data berhasil ditambah!")


def ubah_sampah():
    lihat_sampah()
    print("\n=== UBAH DATA SAMPAH ===")
    try:
        id = int(input("Masukkan ID: "))
        berat = int(input("Berat (kg): "))
    except ValueError:
        print("Hey ndut input harus berupa angka")
        return
    status = input("Status (1. Belum Diangkut / 2. Sudah Diangkut): ")
    if id not in sampah or berat <= 0 or status not in ["1", "2"]:
        print("ID tidak ditemukan, berat <= 0, atau status salah!")
        return
    sampah[id]["berat"] = berat
    sampah[id]["status"] = "Belum Diangkut" if status == "1" else "Sudah Diangkut"
    print("Data berhasil diubah!")


def hapus_sampah():
    lihat_sampah()
    print("\n=== HAPUS DATA SAMPAH YANG ADA DI GUNUNG ===")
    try:
        id = int(input("Masukkan ID: "))
    except ValueError:
        print("ID harus berupa angka!")
        return
    if id in sampah:
        del sampah[id]
        print("Data berhasil dihapus!")
    else:
        print("ID tidak ditemukan!")



def menu_admin():
    while True:
        bersih()
        print("=" * 35)
        print("   MENU ADMIN")
        print("=" * 35)
        print("1. Tambah Data Sampah")
        print("2. Lihat Data Sampah")
        print("3. Ubah Data Sampah")
        print("4. Hapus Data Sampah")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        bersih()
        if pilih == "1":
            tambah_sampah()
        elif pilih == "2":
            lihat_sampah()
        elif pilih == "3":
            ubah_sampah()
        elif pilih == "4":
            hapus_sampah()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")
        jeda()


def menu_user():
    while True:
        bersih()
        print("=" * 35)
        print("   MENU USER")
        print("=" * 35)
        print("1. Lihat Data Sampah")
        print("0. Logout")
        pilih = input("Pilih menu: ")

        bersih()
        if pilih == "1":
            lihat_sampah()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak valid!")
        jeda()


def main():
    while True:
        bersih()
        print("=" * 35)
        print("SISTEM PENGELOLAAN SAMPAH GUNUNG")
        print("=" * 35)
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        pilih = input("Pilih menu: ")

        bersih()
        if pilih == "1":
            role = login()
            if role == "admin":
                menu_admin()
                continue
            elif role == "user":
                menu_user()
                continue
        elif pilih == "2":
            registrasi()
        elif pilih == "3":
            print("Terima kasih!")
            break
        else:
            print("Harus memilih 1-3")
        jeda()


main()