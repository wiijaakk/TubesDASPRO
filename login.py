print("WOI LOGIN\n")

import main_library as mlib

user = str(input("Masukkan username anda: "))
pasw = str(input("Masukkan password anda: "))

data = mlib.check_user(user)

if data[5]:
    if data[2] == pasw:
        print("anda berhasil login!")
    else:
        print("username atau password salah..")
else:
    print("username atau password salah..")


