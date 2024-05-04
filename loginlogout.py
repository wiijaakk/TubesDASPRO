
import main_library as mlib

# list untuk menyimpan username-usernam yang sudah login
logged = [] 

def login():
    user = str(input("Masukkan username anda: "))
    pasw = str(input("Masukkan password anda: "))

    data = mlib.check_user(user) 

    if data[5]: # memeriksa data username yang ditemukan
        if data[1] not in logged: #  jika data tidak ada di list logged 
            if data[2] == pasw: # jika password ditemukan dalam data
                logged.append(data[1]) # data ditambahkan ke dalam list logged
                print(f"Anda berhasil login! Selamat Datang, Agent {data[1]} ")
                return data[1]
            else : 
                print("Password anda salah")
        else: # jika data ada di list logged
            print("Anda telah login dengan username ini, lakukan 'LOGOUT' terlebih dahulu")
            return None
    else: # jika data tidak ditemukan
        print("Username anda salah..")
        return None


def logout(logged):
    if logged: # jika username yang sedang login terdapat dalam list logged
        logged = [] # kosongkan kembali list
        return None
    else: # jika username yang sedang login tidak terdapat dalam list logged
        print("Logout Gagal")
        print("Anda belum login, silahkan masuk ke menu 'LOGIN' terlebih dahulu")
        return logged

def main():
    logged = None # inisialisasi logged
    while True:
        command = input(">>> ").upper()
        if command == "LOGIN":
            logged = login()
        elif command == "LOGOUT":
            logged = logout(logged)
        else:
            print("Command tidak tersedia.")
