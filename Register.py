# Import
import main_library as mlib

# Menunjukkan CSV file yang akan digunakan
user_csv = 'tubes daspro/csv/user.csv'

# ambil input dari user
user = str(input("Masukkan Username: "))
pasw = str(input("Masukkan Password: "))


data = mlib.check_user(user)

# mengecek validitas username
valid = True

# mengecek apakah username mengandung character selain alphabet, underscore, strip, dan angka
for char in user:
    if ord(char) == 45 or ord(char) == 95 or 48 <= ord(char) <= 57 or 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
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
    # Hasil akhir dari fungsi try
    # jika ada username yang sama, maka pengguna akan diberitahu dan username yang diinput tidak akan dicatat dan dimasukkan kedalam file CSV
    if data[5]:
        print(f"Username '{user}' sudah terdaftar, gunakan username yang lain!")
    # jika tidak ada yang menggunakan username yang diinputkan, maka username baru akan dimasukkan ke dalam File CSV beserta passwordnya
    else:
        print(f"Tidak ada yang menggunakan username '{user}'.")
        
        # merubah data input yang diterima menjadi format CSV
        new_input = f"{data[6]};{user};{pasw};Agent;0\n"

        # masukkan data yang telah diformat ulang kedalam file CSV 
        with open(user_csv, 'a') as file:
            file.write(new_input)
        
        print("Username telah dibuat!")
