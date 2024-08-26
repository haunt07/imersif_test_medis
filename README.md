# Test Medis
## Requirement
- python3
## Tatacara pengerjaan
1. Kerjakan soal dengan mengisi program didalam setiap function yang ada di file soal.py
2. Untuk cek apakah program sesuai dengan eksekusi command berikut di terminal pada root project directory
```
python3 -m unittest discover -v -s test
```
3. Jika soal berhasil dikerjakan dengan benar, maka pada terminal akan muncul keterangan "ok" untuk tiap-tiap soal.\
DI BAWAH ADALAH CONTOH KETIKA SEMUA SOAL BERHASIL DIKERJAKAN DENGAN BENAR
```
test_add (test_index.TestSoal.test_add) ... ok
test_check_palindrome (test_index.TestSoal.test_check_palindrome) ... ok
test_count_capital_letters (test_index.TestSoal.test_count_capital_letters) ... ok
test_division (test_index.TestSoal.test_division) ... ok
test_multiplication (test_index.TestSoal.test_multiplication) ... ok
test_reverese_sentence (test_index.TestSoal.test_reverese_sentence) ... ok
test_sub (test_index.TestSoal.test_sub) ... ok
test_uwu_text_converter (test_index.TestSoal.test_uwu_text_converter) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK
```