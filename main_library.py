# import main_library as mlib

# Menunjukkan CSV file yang akan digunakan
user_csv = 'tubes daspro/csv/user.csv'

# Fungsi CSV parsing
def csv_parse(line):
    # variabel yang akan digunakan dalam fungsi ini
    fields = []
    current_field = ''

    # For Loop untuk memindahkan setiap kata dalam sebuah CSV line, loop akan berhenti jika menemukan tanda koma DAN tidak memasukkan tanda koma tersebut.
    for char in line:
        if char == ";":
            fields.append(current_field)
            current_field = ''
        else:
            current_field += char
    fields.append(current_field)  # menambahkan kata yang sudah dibuat oleh For Loop kedalam fields

    # Debugging Station 1
    # line_debug = "username;password;role;coin"
    # print(csv_parse(line_debug))
    
    return fields

def check_user(user):
    file = open(user_csv, 'r')
    
    # menghitung banyaknya username yang sudah tersimpan, id pertama adalah admin
    i_d = 0
    
    line_found = ["","","","","",False,i_d]
    # For Loop yang digunakan untuk membaca setiap line yang ada dalam File CSV
    for line in file:
        # mulai mendata username yang ada di kolom yang diinginkan menggunakan fungsi Parse yang sudah dibuat di Main Library
        data = csv_parse(line)
        
        # untuk tiap line, banyak username bertambah satu
        i_d += 1
        line_found[6] = i_d

        # cek apakah ada username yang sama dalam file CSV dengan yang diinputkan
        # username dicatat di kolom pertama dalam File CSV, maka digunakan data[0] untuk mendapatkan kolomnya
        if data[1] == user:
            line_found = data
            line_found.append(True)
            line_found.append(i_d)
            break

    # Hasil akhir dari fungsi try
    return line_found

# Debugging Station 2
# user1 = "user1"
# user2 = "user2"
# user3 = "user3"
# print(check_user(user3))