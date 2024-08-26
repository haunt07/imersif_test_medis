def add(a:float,b:float)->float:
    '''
    BUATLAH OPERASI PENJUMLAHAN
    hasil maksimal 2 dibelakang koma
    
    hasil = a + b

    CONTOH 1:
    hasil = add(1,2)
    print(hasil) 

    Output Terminal:
    3

    CONTOH 2:
    hasil = add(1,2.111)
    print(hasil) 

    Output Terminal:
    3.11
    '''

    #-----code-----#
    pass
    

def sub(a:float,b:float)->float:
    '''
    BUATLAH OPERASI PENGURANGAN
    hasil maksimal 2 dibelakang koma

    hasil = a - b

    CONTOH 1:
    hasil = sub(1,2)
    print(hasil)

    Output Terminal:
    -1

    CONTOH 2:
    hasil = sub(1,2.1111)
    print(hasil)

    Output Terminal:
    -1.11
    '''

    #-----code-----#
    pass



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
    
    Output Terminal:
    1.21
    '''


    #-----code-----#
    pass


def division(a:float,b:float)->float:
    '''
    BUATLAH OPERASI PEMBAGIAN

    hasil 2 angka dibelakang koma
    hasil = a/b

    CONTOH:
    hasil = division(2,3)
    print(hasil)

    Output Terminal:
    0.67

    Jika terdapat error ketika pembagi adalah angka 0 lakukan:
    Throw ValueError dengan message "Error division number"
    MISAL KETIKA:
    division(2,0)
    
    Output Terminal:
    ValueError: Error division number
    '''

    #-----code-----#
    pass

    

def count_capital_letters(data:str)->int:
    '''
    MENGHITUNG JUMLAH HURUF KAPITAL DARI DATA

    CONTOH:
    hasil = count_capital_letters("ABCabc")
    print(hasil)

    Output Terminal:
    3

    Jika terdapat spasi didalam data lakukan:
    Throw ValueError dengan message "Wrong input"
    MISAL KETIKA:
    count_capital_letters("a     s  ")

    Output Terminal:
    ValueError: Wrong input
    '''

    #-----code-----#
    pass


def reverse_sentence(data:str)->str:
    '''
    MELAKUKAN REVERSE SENTENCE DARI DATA
    
    CONTOH 1:
    hasil = reverse_sentence("1234a5c6")
    print(hasil)

    Output Terminal:
    6c5a4321

    Jika terdapat spasi, harus dihilangkan

    CONTOH 2:
    hasil = reverse_sentence("123456 asd      123456")
    print(hasil)

    Output Terminal:
    654321dsa654321
    '''

    #-----code-----#
    pass


def check_palindrome(data:str)->bool:
    '''
    MELAKUKAN DETEKSI PALINDROME DARI DATA

    jika terdapat pola kalimat yang dibalik hasilnya sama maka hasilnya True
    jika sebaliknya maka salah

    CONTOH 1:
    hasil=check_palindrome("uwu")
    print(hasil)
    
    Output Terminal:
    True

    CONTOH 2:
    hasil=check_palindrome("pull up if i pull up")
    print(hasil)

    Output Terminal:
    True

    CONTOH 3:
    hasil=check_palindrome("coding")

    Output Terminal:
    False

    CONTOH 4:
    hasil=check_palindrome("123awa335446  ")

    Output Terminal:
    True

    Jika panjang data dibawah dari 3
    maka Throw ValueError("Wrong Input")
    MISAL KETIKA:
    check_palindrome("as")
    check_palindrome("1")

    Output Terminal:
    ValueError: Wrong Input
    '''

    #-----code-----#
    pass
    

def uwu_text_converter(data:str)->str:
    '''
    KONVERSI TEKS MENJADI IMOET UwU

    Untuk mengubah teks menjadi imut UwU, terdapat beberapa kondisi yang harus terpenuhi:

    1. Mengubah huruf 'r' menjadi 'w' termasuk huruf kapital (R -> W & r -> w)
    2. Mengubah huruf 'l' menjadi 'w' termasuk huruf kapital (L -> W & l -> w)
    3. Mengubah huruf 's' menjadi 'c' termasuk huruf kapital (S -> C & s -> c)
    3. Jika ada huruf 'm' dan 'n' yang diikuti dengan 'o' termasuk huruf kapital, maka masukkan huruf y di antaranya.

    CONTOH 1:
    hasil=uwu_text_converter("Semoga hari lancar sesuai rencana")
    print(hasil)

    Output Terminal:
    Cemyoga hawi ini wancaw cecuai wencana

    CONTOH 2:
    hasil=uwu_text_converter("Lamborghini mobil tercepat nomor satu di dunia")
    print(hasil)

    Output Terminal:
    Wambowghini mobil tewcepat nyomow catu di dunia

    CONTOH 3:
    hasil=uwu_text_converter("Sakura menolong naruto dari madara")

    Output Terminal:
    Cakuwa menyolong nawuto dawi madawa
    '''

    #-----code-----#
    pass