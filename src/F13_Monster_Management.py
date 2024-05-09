# Import
import main_library as mlib

# Menunjukkan CSV file yang akan digunakan
monsta = 'data/monster.csv'

# Mengambil input dari user
print("SELAMAT DATANG DI DATABASE PARA MONSTER !!! RAWR")
print("1. Tampilkan semua Monster")
print("2. Tambah Monster baru")
banyak_monster = 0
with open(monsta, 'r') as file:
        for line in file:
            banyak_monster+=1
valid_tak = False
while(valid_tak == False):
    aksi = int(input("Pilih Aksi : "))
    if aksi == 1:
        valid_tak = True
        with open(monsta, 'r') as file:
            max_widths = [0] * 5  
            for line in file:
                banyak_monster+=1
                data = mlib.csv_parse(line)
                for i in range(len(data)):
                    max_widths[i] = mlib.maksi(max_widths[i], len(str(data[i])))
            file.seek(0)
            for line in file:
                data = mlib.csv_parse(line)
                for i in range(len(data)):
                    if i==len(data)-1:print(f" {data[i]}")
                    elif i == 1: print(f"{data[i]:<{max_widths[i]}}", end=" | ")
                    else:print(f"{data[i]:<{max_widths[i]}}", end=" | ")
    elif aksi == 2:
        valid_tak = True
        print("Memulai pembuatan monster baru")
        with open(monsta, 'r') as file:
            valid = False
            monster = ""
            while(valid == False):
                    valid = True
                    nama = input("Masukkan Type / Nama : ")
                    next(file)
                    for line in file:
                        data = mlib.csv_parse(line)
                        if data[1] == nama:
                            valid = False
                            break
                    if valid == False: 
                        print("Nama sudah terdaftar, coba lagi!")
                    else: monster = nama
            valid = False
            atk_power = 0
            while(valid == False):
                nilai = input("Masukkan ATK Power : ")  
                if mlib.cekinteger(nilai)==True:
                    valid = True
                    atk_power = int(nilai)
                    break
                else:
                    print("Masukkan input harus bertipe Integer, coba lagi!")
            valid = False
            def_power = 0
            while(valid == False):
                nilai = input("Masukkan DEF Power (0-50) : ")  
                if mlib.cekinteger(nilai)==True and 0<=int(nilai)<=50:
                    valid = True
                    def_power = int(nilai)
                    break
                elif mlib.cekinteger(nilai)==False:
                    print("Masukkan input harus bertipe Integer, coba lagi!")
                else:
                    print("DEF Power harus bernilai 0-50, coba lagi!")
            valid = False
            hp = 0
            while(valid == False):
                nilai = input("Masukkan HP : ")  
                if mlib.cekinteger(nilai)==True:
                    valid = True
                    hp = nilai
                    break
                else:
                    print("Masukkan input harus bertipe Integer, coba lagi!")
        print("Monster baru berhasil dibuat!")
        print(f"Type : {monster}")
        print(f"ATK Power : {atk_power}")
        print(f"DEF Power : {def_power}")
        print (f"HP : {hp}")
        bener = False
        while (bener == False):
            tambah = input("Tambahkan Monster ke database (Y/N) : ")
            if tambah == 'N':
                bener = True
                print("Monster gagal ditambahkan!")
            elif tambah == 'Y':
                bener = True
                new_input = f"\n{banyak_monster};{monster};{atk_power};{def_power};{hp}"

                    # masukkan data yang telah diformat ulang kedalam file CSV 
                with open(monsta, 'a') as file:
                        file.write(new_input)
                print("Monster baru telah ditambahkan!")
            else: print("Masukkan tidak valid. Silakan memberi masukan (Y/N).")
    else: 
        print("Aksi tidak tersedia. Coba lagi.")