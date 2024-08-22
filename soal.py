def add(a:float,b:float)->float:
    '''
    Soal penjumlahan
    hasil=a+b
    a=1
    b=2
    return 3
    '''
    result = 0.0
    return result

def sub(a:float,b:float)->float:
    '''
    Soal substraction
    hasil=a-b
    a=1
    b=2
    return  -1
    '''
    result = 0.0
    return result

def multiplication(a:float,b:float)->float:
    '''
    Soal multiplication
    hasil 2 angka dibelakang koma
    hasil=a*b
    a=1
    b=2
    return  2
    '''
    result = 0.0
    return result

def division(a:float,b:float)->float:
    '''
    Soal pembagian
    hasil 2 angka dibelakang koma
    hasil=a/b
    a=2
    b=2
    return  1
    Jika terdapat error jika pembagi adalah angka 0 lakukan:
    Throw ValueError dengan message "Error division number"
    example error:
    a=2
    b=0
    '''
    result = 0.0
    return result

def count_capital_letters(data:str)->int:
    '''
    Soal menghitung huruf kapital
    data = "ABCabc"
    return 3
    Jika terdapat spasi didalam data lakukan:
    Throw ValueError dengan message "Wrong input"
    example error:
    data="a     s  "
    '''
    result=0
    return result

def reverse_sentence(data:str)->str:
    '''
    Soal reverse sentence
    data="1234a5c6"
    return "6c5a4321"
    Jika terdapat spasi, harus dihilangkan
    data="123456 asd 123456"
    return "654321dsa654321"
    '''
    result=""
    return result

def check_palindrome(data:str)->bool:
    '''
    Soal cek palindrom
    jika terdapat pola kalimat yang dibalik hasilnya sama maka hasilnya True
    jika sebaliknya maka salah
    data="uwu"
    return True
    data="pull up if i pull up"
    return True
    data="coding"
    return False
    data="123awa335446  "
    return True
    Jika panjang data dibawah dari 3
    maka Throw ValueError("Wrong Input")
    example error:
    data="as"
    data="1"
    '''
    result=False
    return result