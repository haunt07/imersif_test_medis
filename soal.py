def add(a:float,b:float)->float:
    '''
    BUATLAH OPERASI PENJUMLAHAN

    hasil = a + b

    CONTOH:
    hasil = add(1,2)
    print(hasil) 
    
    Output = 3
    '''

    #-----code-----#
    

def sub(a:float,b:float)->float:
    '''
    BUATLAH OPERASI PENGURANGAN

    hasil = a - b

    CONTOH:
    hasil = sub(1,2)
    print(hasil)

    Output: -1
    '''

    #-----code-----#



def multiplication(a:float,b:float)->float:
    '''
    BUATLAH OPERASI MULTIPLICATION

    hasil 2 angka dibelakang koma
    hasil = a*b

    CONTOH 1:
    hasil = multiplication(1,2)
    print(hasil)
    
    Output = 2

    CONTOH 2:
    hasil = multiplication(1.1,1.1)
    print(hasil)
    
    Output = 1.21
    '''


    #-----code-----#


def division(a:float,b:float)->float:
    '''
    BUATLAH OPERASI PEMBAGIAN

    hasil 2 angka dibelakang koma
    hasil = a/b

    CONTOH:
    hasil = division(2,3)
    print(hasil)

    Output = 0.67

    Jika terdapat error ketika pembagi adalah angka 0 lakukan:
    Throw ValueError dengan message "Error division number"
    MISAL KETIKA:
    hasil = division(2,0)
    print(hasil)

    Output = "Error division number"
    '''

    #-----code-----#

    

def count_capital_letters(data:str)->int:
    '''
    MENGHITUNG JUMLAH HURUF KAPITAL DARI DATA

    CONTOH:
    hasil = count_capital_letters("ABCabc")
    print(hasil)

    Output = 3

    Jika terdapat spasi didalam data lakukan:
    Throw ValueError dengan message "Wrong input"
    MISAL KETIKA:
    hasil = count_capital_letter("a     s  ")
    print(hasil)

    Output = "Wrong input"
    '''

    #-----code-----#


def reverse_sentence(data:str)->str:
    '''
    MELAKUKAN REVERSE SENTENCE DARI DATA
    
    CONTOH 1:
    hasil = reverse_sentence("1234a5c6")
    print(hasil)

    Output = "6c5a4321"

    Jika terdapat spasi, harus dihilangkan

    CONTOH 2:
    hasil = reverse_sentence("123456 asd 123456")
    print(hasil)

    Output = "654321dsa654321"
    '''

    #-----code-----#


def check_palindrome(data:str)->bool:
    '''
    MELAKUKAN DETEKSI PALINDROME DARI DATA

    jika terdapat pola kalimat yang dibalik hasilnya sama maka hasilnya True
    jika sebaliknya maka salah

    CONTOH 1:
    check_palindrome("uwu")
    Output = True

    CONTOH 2:
    check_palindrome("pull up if i pull up")
    Output = True

    CONTOH 3:
    check_palindrome("coding")
    Output = False

    CONTOH 4:
    check_palindrome("123awa335446  ")
    Output = True

    Jika panjang data dibawah dari 3
    maka Throw ValueError("Wrong Input")
    MISAL KETIKA:
    check_palindrome("as")
    check_palindrome("1")

    Output = "Wrong input"
    '''

    #-----code-----#
    

def uwu_text_converter(data:str)->str:
    '''
    KONVERSI TEKS MENJADI IMOET UwU

    Untuk mengubah teks menjadi imut UwU, terdapat beberapa kondisi yang harus terpenuhi:

    1. Mengubah huruf 'r' menjadi 'w' termasuk huruf kapital (R -> W & r -> w)
    2. Mengubah huruf 'l' menjadi 'w' termasuk huruf kapital (L -> W & l -> w)
    3. Mengubah huruf 's' menjadi 'c' termasuk huruf kapital (S -> C & s -> c)
    3. Jika ada huruf 'm' dan 'n' yang diikuti dengan 'o' termasuk huruf kapital, maka masukkan huruf y di antaranya.

    CONTOH 1:
    uwu_text_converter("Semoga hari lancar sesuai rencana")
    Output = "Cemyoga hawi ini wancaw cecuai wencana"

    CONTOH 2:
    uwu_text_converter("Lamborghini mobil tercepat nomor satu di dunia")
    Output = "Wambowghini mobil tewcepat nyomow catu di dunia"

    CONTOH 3:
    uwu_text_converter("Sakura menolong naruto dari madara")
    Output = "Cakuwa menyolong nawuto dawi madawa"
    '''

    #-----code-----#