# Import
import main_library as mlib

# Menunjukkan CSV file yang akan digunakan
user_csv = 'data/user.csv'

# ambil input dari user
user = str(input("Masukkan Username: "))
pasw = str(input("Masukkan Password: "))

# mengecek validitas username
valid = True

# mengecek apakah username mengandung character selain alphabet, underscore, strip, dan angka
for char in user:
    if ord(char)==45 or ord(char)==95 or 48<=ord(char)<=57 or 65<=ord(char)<=90 or 97<=ord(char)<=122:
        '''
        ascii 45 adalah character strip -
        ascii 95 adalah character underscore _
        ascii 48 sampai 57 adalah angka 0-9
        ascii 65 sampai 90 adalah alphabet A-Z
        ascii 97 sampai 122 adalah alphabet a-z
        '''
        continue
    # jika username mengandung karakter selain alfabet A-Za-z, underscore “_”, strip “-”, dan angka 0-9, username tidak valid dan tidak akan disimpan ke user.csv
    else:
        print("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
        valid = False
        break

# Variabel bool untuk cek apakah username sama atau tidak
user_same = False

# jika username valid
if valid:
    # menghitung banyaknya username yang sudah tersimpan, id pertama adalah admin
        i_d = 1
        with open(user_csv, 'r') as file:
            # melewati header file jika ada dalam file
            next(file)
            # For Loop yang digunakan untuk membaca setiap line yang ada dalam File CSV
            for line in file:
                # untuk tiap line, banyak username bertambah satu
                i_d+=1
                # mulai mendata username yang ada di kolom yang diinginkan menggunakan fungsi Parse yang sudah dibuat di Main Library
                data = mlib.csv_parse(line)
                
                # cek apakah ada username yang sama dalam file CSV dengan yang diinputkan
                # username dicatat di kolom pertama dalam File CSV, maka digunakan data[0] untuk mendapatkan kolomnya
                if data[1] == user:
                    user_same = True
                    break

        # Hasil akhir dari fungsi try
        # jika ada username yang sama, maka pengguna akan diberitahu dan username yang diinput tidak akan dicatat dan dimasukkan kedalam file CSV
        if user_same:
            print(f"Username '{user}' sudah terdaftar, gunakan username yang lain!")
        # jika tidak ada yang menggunakan username yang diinputkan, maka username baru akan dimasukkan ke dalam File CSV beserta passwordnya
        else:
            print(f"Tidak ada yang menggunakan username '{user}'.")
            
            # merubah data input yang diterima menjadi format CSV
            new_input = f"\n{i_d};{user};{pasw};Agent;0"

            # masukkan data yang telah diformat ulang kedalam file CSV 
            with open(user_csv, 'a') as file:
                file.write(new_input)
            
            print("Silakan pilih salah satu monster sebagai monster awalmu.")
            monster_csv = 'data/monster.csv'
            with open(monster_csv, 'r') as monster:
                # melewati header file jika ada dalam file
                next(monster)
                # For Loop yang digunakan untuk membaca setiap line yang ada dalam File CSV
                nomor = 1
                for line in monster:
                    data = mlib.csv_parse(line)
                    print(f"{nomor}. {data[1]}")
                    nomor+=1
            with open(monster_csv, 'r') as monster:
                # melewati header file jika ada dalam file
                next(monster)
                pilihan_monster = int(input("Monster pilihanmu: "))
                for line in monster:
                    data = mlib.csv_parse(line)
                    if int(data[0])==pilihan_monster:
                        print(f"Selamat datang Agent {user}. Mari kita mengalahkan Dr. Asep Spakbor dengan {data[1]}!")