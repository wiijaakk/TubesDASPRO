import os
import time

def lcm(batas_bawah, batas_atas): # Membuat fungsi rng (random number generator) yang menerima masukan seed (X0), batas_bawah, batas_atas, lalu mengembalikan angka random yang berada pada interval [batas_bawah, batas_atas]
    a = 48271 # Memilih angka multipier tern random a
    c = 0 # Memilih angka increment term random c
    X0 = int(os.getpid()+time.time()) #Menggunakan seed berdasar pada waktu dan id sehingga semakin random
    # Menggunakan Liner Congruential Method, yaitu:
    # batas_bawah + (((a*X0)+c) % (batas_atas - batas_bawah + 1))
    # Dengan menggunakan metode ini, dipastikan akan menghasilkan angka yang bernilai lebih besar sama dengan batas_bawah dan lebih kecil sama dengan batas_atas (karena hasil modulo akan berada pada interval [0, batas_atas - batas_bawah], lalu nilainya ditambahkan dengan nilai batas_bawah sehinggal interval menjadi [batas_bawah, batas_atas])
    return batas_bawah + ((a*X0 + c) % (batas_atas - batas_bawah +1))
