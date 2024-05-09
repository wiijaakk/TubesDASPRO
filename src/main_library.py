# import main_library as mlib

# Fungsi CSV parsing
def csv_parse(line):
    # variabel yang akan digunakan dalam fungsi ini
    fields = []
    current_field = ''

    # For Loop untuk memindahkan setiap kata dalam sebuah CSV line, loop akan berhenti jika menemukan tanda koma DAN tidak memasukkan tanda koma tersebut.
    for char in line:
        if char == ';':
            fields.append(current_field)
            current_field = ''
        else:
            current_field += char
    fields.append(current_field)  # menambahkan kata yang sudah dibuat oleh For Loop kedalam fields
    return fields
 
 # Fungsi mencari nilai maksimum
def maksi(a, b):
    if a>b: return a
    else: return b

# Fungsi mengecek Integer atau bukan
def cekinteger(a):
    if len(a) == 0: return False
    else:
        for char in a:
            if not ('0' <= char <='9'): return False
        return True