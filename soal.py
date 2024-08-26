def add(a:float,b:float)->float:
    '''
    BUATLAH OPERASI PENJUMLAHAN

    hasil = a + b

    CONTOH:
    a = 1
    b = 2
    return 3
    '''

    #-----code-----#

    result = 0.0
    return result

def sub(a:float,b:float)->float:
    '''
    BUATLAH OPERASI PENGURANGAN

    hasil = a - b

    CONTOH:
    a = 1
    b = 2
    return  -1
    '''

    #-----code-----#

    result = 0.0
    return result

def multiplication(a:float,b:float)->float:
    '''
    BUATLAH OPERASI MULTIPLICATION

    hasil 2 angka dibelakang koma
    hasil = a*b

    CONTOH:
    a = 1
    b = 2
    return  2
    '''

    #-----code-----#

    result = 0.0
    return result

def division(a:float,b:float)->float:
    '''
    BUATLAH OPERASI PEMBAGIAN

    hasil 2 angka dibelakang koma
    hasil = a/b

    CONTOH:
    a = 2
    b = 2
    return  1

    Jika terdapat error ketika pembagi adalah angka 0 lakukan:
    Throw ValueError dengan message "Error division number"
    MISAL KETIKA:
    a = 2
    b = 0
    '''

    #-----code-----#
    
    result = 0.0
    return result

def count_capital_letters(data:str)->int:
    '''
    MENGHITUNG JUMLAH HURUF KAPITAL DARI DATA

    CONTOH:
    data = "ABCabc"
    return 3

    Jika terdapat spasi didalam data lakukan:
    Throw ValueError dengan message "Wrong input"
    MISAL KETIKA:
    data = "a     s  "
    '''

    #-----code-----#

    result=0
    return result

def reverse_sentence(data:str)->str:
    '''
    MELAKUKAN REVERSE SENTENCE DARI DATA
    
    CONTOH:
    data = "1234a5c6"
    return "6c5a4321"

    Jika terdapat spasi, harus dihilangkan

    CONTOH:
    data = "123456 asd 123456"
    return "654321dsa654321"
    '''

    #-----code-----#

    result=""
    return result

def check_palindrome(data:str)->bool:
    '''
    MELAKUKAN DETEKSI PALINDROME DARI DATA

    jika terdapat pola kalimat yang dibalik hasilnya sama maka hasilnya True
    jika sebaliknya maka salah

    CONTOH:
    data=  "uwu"
    return True

    CONTOH 2:
    data = "pull up if i pull up"
    return True

    CONTOH 3:
    data = "coding"
    return False

    CONTOH 4:
    data = "123awa335446  "
    return True

    Jika panjang data dibawah dari 3
    maka Throw ValueError("Wrong Input")
    MISAL KETIKA:
    data = "as"
    data = "1"
    '''

    #-----code-----#

    result=False
    return result