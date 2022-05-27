print("Hello World")
# komentar dari python

# number
print(3)

# oprasi aritmatika
# tambah
print(1 + 1)
# kurang
print(10-5)
# bagi
print( 10/2)
# kali
print(10 * 5)
# sisa bagi
print(10 % 3)

#variable
hello = "Hallo Dunia"

print(hello)
print(hello)
print(hello)

hello = "hello python"

print(hello)
print(hello)

# String
nama = "Kusnanto Hidayat"
kota = 'Subang'
alamat = 'rangdu'

nama_depan = "Kusnanto"
nama_belakang = "Hidayat"
nama_lengkap = nama_depan + " " + nama_belakang

print(nama_lengkap)

nama_depan = "Kus"
nama_tengah = "Nanto"
nama_belakang = "Hidayat"

sapa = f"Halo {nama_depan} {nama_tengah} {nama_belakang}"

print(sapa)

#Input Data

print("Silahkan Masukan Nama : ")

nama = input()

print(f"Hello {nama}, Selamat Datang")

#Input Number
print("Angka Pertama")
a = int(input())
print("Angka Kedua")
b = int(input())

hasil = a + b
print(f"{a} + {b} = {hasil}")

#Tipe Data Boolean
menikah = False
jomblo = True

print(menikah)
print(jomblo)

#Oprasi Logika
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

#Operasi Perbandingan
#
# > lebih dari
# < kurang dari
# >= lebih dari sama dengan
# <= kurang dari sama dengan
# == sama dengan
# != tidak sama dengan
#
print(1 > 1) 
print(1 < 10) 
print(1 == 1) 

print("Kus" == "Kus")
print("Kus" != "Kus")

#Belajar If-Statement
orang = 1000
zombi = 100

if orang < zombi:
    print("Dunia Mau Kiamat")

if orang > zombi:
    print("Ayo Basmi Zombi")

if orang == zombi:
    print("Mari Perang")


#Belajar If Else
menang = False

if menang:
    print("Selamat!")
else:
    print("Silahkan Coba Lagi")


#Belajar Elif
menu_pilihan = input("Silahkan pilih menu [1-3] : ")

if menu_pilihan == "1":
    print("Anda Memilih Menu 1")
elif menu_pilihan == "2":
    print("Anda Memilih Menu 2")
elif menu_pilihan == "3":
    print("Anda Memilih Menu 3")
else:
    print("Menu Tidak Tersedia")


#Belajar List
nama = ["Kus", "Budi", "Andi"]
#menambah data pada list
nama.append("Robert")
#mengakses list
print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3])

print(len(nama))
#menghapus data dari list
nama.remove("Budi")

print(nama)
#mengubah data di list
nama[0] = "Nanto"


#Belajar For loop
pelanggan = ["Kus", "Rudy", "Rafi"]
pelanggan.append("Nanto")
pelanggan.append("Hidayat")

#mengakses semua nama pelanggan
for nama in pelanggan:
    print("==============")
    print(f"Nama Pelanggan: {nama}")
    print("==============")


#Belajar Range
nomor = [1,2,3,4,5,6,7,8,9,10]
for no in range(1, 11):
    print(no)


#Belajar While-Loop
data = ""

while data != "x":
    print("Masuk perulangan : ")
    data = input("data : ")

#Belajar Continue
for i in range(1, 100):
    if i % 2 == 1:
        continue
    print(i)


#Belajar Break
while True:
    data = input("Data : ")
    if data == "x":
        break
    print(data)

#Belajar Tuple
#Tuple hampir sama kaya list, jika list pake[], sedangkan tuple pake(), dan data tuple tidak bisa di ubah seperti list
pelanggan = ("Kus", "Nanto", "Hidayat")
print(pelanggan)

#Belajar set
#set itu indexnya berpindah-pindah makanya data tidak bisa di ubah
#list => []
#tuple => ()
#set => {}
nama = {"Kus", "nanto", "Hidayat"}
for data in nama:
    print(data)



#Belajar method
nama = []

def print_nama():
    print("===========")
    for data in nama:
        print(data)

nama.append("Kus")
print_nama()

nama.append("Nanto")
print_nama()

nama.append("Hidayat")
print_nama()

#Belajar Method Parameter
def say_hello(first_name, last_name):
    print(f"Hello {first_name}{last_name}")

say_hello("Kusnanto Hidayat", " Amin")
say_hello("Widi yanti", " Child")

#belajar  Default Argument.Value
def say_hello(first_name="Kus", last_name=""):
    print(f"Hello {first_name} - {last_name}")

say_hello("Kusnanto Hidayat")
say_hello(last_name="Widi yanti")


#Belajar Argument List

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")

jumlahkan(10,10,10,10,10)


#Belajar Method Return Value
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return(list_angka, total)

list_angka, total = jumlahkan(10,10,10,10,10)

# Mengambil Data Total?
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")
print(f"Total {list_angka} = {total}")

#Belajar Tipe Data Dictionary

customer = {"nama":"kusnanto", "age":17, "address":"subang"}

nama = customer["nama"]
age = customer["age"]
address = customer["address"]

customer["Company"] = "x"
customer["nama"] = "Kusnanto"

del customer["address"]

for key, value in customer.items():
    print(f"{key}:{value}")

#Belajar Keyword Argument List
def create_html(tag,text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key} ='{value}'"
    
    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "Hello Python", style="Paragraf")
print(html)
html = create_html("a", "Ini Link", href="www.google.com", style="Link")
print(html)
html = create_html("div", "Ini Div", style="Contoh")
print(html)

# Belajar Numeric types
# 1. integer - angka normal tanpa koma,
# 2. float - angka koma contoh 1.5
# 3. complex - angka asli / matematikawan

#Belajar String method
#https://docs.python.org/3.7/library/stdtypes.html#string-methods

nama = "Kusnanto Hidayat"
print(nama)
print(nama.upper())
print(nama.capitalize())
print(nama.split(" "))



