# Tugas Kecil 1 Strategi Algoritma
# Penyelesaian Cryptarithmetic dengan Algoritma Brute Force
# Nama: Gayuh Tri Rahutami
# NIM: 13519192

import time

# Fungsi untuk permutasi
def permutasi(li):
    listPermutasi = []

    if(len(li) < 2):
        return li
    else:
        for i in range (len(li)):
            temp = permutasi(li[0:i] + li[i+1:len(li)])
            
            if(len(li) > 2):
                for member in temp:
                    member.append(li[i])
                    listPermutasi.append(member)
            else:
                temp.append(li[i])
                listPermutasi.append(temp)

        return listPermutasi

# Fungsi untuk meng-convert string ke integer
def convert(str, listHuruf):
    converted = 0
    for huruf in str:
        converted *= 10
        converted += listHuruf.index(huruf)
    return converted

# Fungsi untuk mengecek apakah permutasi sudah benar
def check(listKata, listHuruf, result):
    sum = 0
    convKata = []
    i = 0
    errorFound = False

    while(not errorFound and i < len(listKata)):
        convKata.append(0)
        if (listHuruf.index(listKata[i][0]) == 0): # Apabila ditemukan sebuah kata yang huruf pertamanya = 0 maka permutasi salah
            errorFound = True
        else:
            #meng-convert kata menjadi integer dan menjumlahkannya
            convKata[i] = convert(listKata[i], listHuruf)
            sum += convKata[i]
        i += 1
    
    if(sum == result and not errorFound): #Apabila jumlah operand-operand = hasil, maka list berisi kata yang telah diconvert dikembalikan
        return convKata
    else: #Jika jumlah operand-operand != hasil, maka list kosong dikembalikan
        return []

print("========================================")
filename = input("Masukkan nama file:\n")
print("========================================")
start_time = time.time()
file = open(filename, 'r')          

listKata = [] # List untuk menyimpan kata-kata operand
listHuruf = [] # list untuk menyimpan huruf-huruf yang ada di operasi

# Pengambilan operand pertama
listKata.append(file.readline())
i =  0

# Membersihkan spasi dan newline
listKata[i] = listKata[i].replace(" ", "")
listKata[i] = listKata[i].replace("\n", "")

# Memasukkan huruf-huruf ke listHuruf
for huruf in listKata[i]:
    if not(huruf in listHuruf) and (huruf != "+") and (huruf != " ") and (huruf != "\n"): # Jika huruf belum ada sebelumnya baru dimasukkan ke list
        listHuruf.append(huruf)

# Membaca operand-operand selanjutnya
# Pembacaan berhenti apabila ditemukan baris yang mengandung tanda "+"
while not('+' in listKata[i]):
    i += 1

    # Pengambilan input ke-i
    listKata.append(file.readline())

    # Membersihkan spasi dan newline
    listKata[i] = listKata[i].replace(" ", "")
    listKata[i] = listKata[i].replace("\n", "")

    # Memasukkan huruf-huruf ke listHuruf
    for huruf in listKata[i]:
        # Jika huruf belum ada sebelumnya baru dimasukkan ke list
        # Jika huruf = "+" tidak perlu dimasukkan
        if not(huruf in listHuruf) and (huruf != "+"): 
            listHuruf.append(huruf)

# Menghilangkan tanda + dari operand terakhir
listKata[i] = listKata[i].replace("+", "")

file.readline() #Garis tidak perlu disimpan

result = file.readline() # Menyimpan hasil penjumlahan

#Membersihkan spasi dan newline pada string hasil
result = result.replace("\n", "")
result = result.replace(" ", "")

file.close()
i = 0

# Mencetak input
print("Input:\n")
for kata in listKata:
    if (i == len(listKata) - 1): #Jika kata bukan elemen terakhir pada list
        space = len(result) - len(kata)
        print("+", end="")
    else:
        space = len(result) - len(kata) + 1
    print(space*" " + kata)
    i += 1
  
print((len(result)+1) * "-")
print(" " + str(result))

print("========================================")

# Memasukkan huruf-huruf di string hasil ke listHuruf
for huruf in result:
    # Jika huruf belum ada sebelumnya baru dimasukkan ke list
    if not(huruf in listHuruf): 
        listHuruf.append(huruf)

# Apabila total huruf < 10, maka tambahkan string kosong hingga panjang list = 10
while(len(listHuruf) < 10):
    listHuruf.append("")

# Mencari Permutasi List
permutationList = permutasi(listHuruf)

found = False
i = 0
convKata = []

# Mengevaluasi setiap permutasi
while(convKata == []) and (i < len(permutationList)):
    convResult = convert(result, permutationList[i])
    convKata = check(listKata, permutationList[i], convResult)
    i += 1

# Mencetak hasil
if(convKata == []):
    print("Persoalan ini tidak memiliki penyelesaian.")
else:
    print("Result:\n")
    for kata in convKata:
        if(convKata.index(kata) == len(convKata) - 1):
            space = len(result) - len(str(kata))
            print("+", end="")
        else:
            space = len(result) - len(str(kata)) + 1
        print(space*" " + str(kata))

    print((len(result)+1) * "-")
    print(" " + str(convResult))

# Mencetak waktu eksekusi dan jumlah percobaan
print("========================================")
print("Waktu eksekusi: %.2f detik" %(time.time()-start_time))
print("Jumlah percobaan: %d percobaan" %(i))
print("========================================")

input()