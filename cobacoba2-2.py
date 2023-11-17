import os
import pwinput
from prettytable import PrettyTable

user = {
    'Udin': {'PIN': '1234', 'saldo': 10000, 'e-pay': 150000, 'member': 'Gratisan'},
    'Salsa': {'PIN': '5678', 'saldo': 1000000, 'e-pay': 150000, 'member': 'Gratisan'}
}

vouchers = {
    'Salsa': {'nama': 'Diskon10', 'diskon': 10, 'status': 'Aktif'},
    'Udin': {'nama': 'Diskon20', 'diskon': 20, 'status': 'Non-Aktif'}
}

menu = [
    [1,"Expresso",15000],
    [2,"Caramel Machiato",20000],
    [3,"Matcha Blend",20000],
    [4,"Matcha Latte",20000],
    [5,"Lemon Tea",13000]
]

table = PrettyTable()
table.field_names=["No","Nama Menu","Harga"]
for item in menu:
    table.add_row(item)

os.system("cls" if os.name == "nt" else "clear")
while True:
    print("========================================================================")
    print("|                             SELAMAT DATANG                           |")
    print("|                                   DI                                 |")
    print("|                         Coffe Shop Keren Bingits                     |")
    print("========================================================================")
    print("|                     Silahkan Login Terlebih Dahulu                   |")
    print("|                                !!!!!!!!                              |")
    print("========================================================================")
    nama = input('Masukkan Nama Anda: ')
    pin = pwinput.pwinput(prompt="Masukkan password: ")

    if nama in user and pin == user[nama]['PIN']:
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            print("========================================================================")
            print("|                           Selamat Datang                             |")
            print("------------------------------------------------------------------------")
            print("|                         Silahkan Pilih Menu                          |")
            print("========================================================================")       
            print("| [1] Top Up Saldo                                                     |")
            print("| [2] Pesan Menu                                                       |")        
            print("| [3] Gabung member VIP                                                |")        
            print("| [0] keluar                                                           |")        
            print("========================================================================")       
            pilih_menu = input('Pilih nomor menu yang diinginkan: ')

            if pilih_menu == '1':
                amount = int(input('Masukkan jumlah saldo yang ingin di-top up: '))
                user[nama]['saldo'] += amount
                print(f'Saldo berhasil di-top up. Saldo sekarang: {user[nama]["saldo"]}\n')

            elif pilih_menu == '2':
                print(table)
                pilihan = int(input('Pilih nomor menu yang diinginkan: '))
                jumlah = int(input('Berapa jumlah yang ingin dibeli: '))
                
                print("===================================================")
                print("| [1] Bayar Dengan Saldo                          |")
                print("| [2] Bayar Dengan Epay                           |")
                print("===================================================")
                metode_pembayaran = input("Pilih metode pembayaran : ")

                if user[nama]['member'] == 'Gratisan':
                    ada_voucher = input("Apakah ada voucher? (ya/tidak): ")
                    diskon = 0
                    if ada_voucher.lower() == 'ya':
                        kode_voucher = input("Masukkan kode voucher: ")
                        if nama in vouchers:                        
                            if kode_voucher == vouchers[nama]['nama']:
                                if vouchers[nama]['status'] == 'Aktif':
                                    diskon = vouchers[nama]['diskon']
                                    print(f"Voucher '{vouchers[nama]['nama']}' berhasil digunakan. Diskon {diskon}% akan diberikan.")
                                else:
                                    print("Voucher tidak aktif.")
                            else:
                                print("Voucher tidak valid.")
                        else:
                            print("Nama pengguna tidak memiliki voucher.")
                else:
                    diskon = 30
                    print("Selamat! Anda sebagai member VIP mendapatkan diskon 30%.")

                total_harga = (menu[pilihan - 1][2] * jumlah) * (1 - diskon / 100)
                if metode_pembayaran == '1':
                    if user[nama]['saldo'] >= total_harga:
                        user[nama]['saldo'] -= total_harga
                        print("==========================================================")
                        print(f"Pembelian berhasil. Saldo sekarang: {user[nama]['saldo']}")
                        print("==========================================================")
                        print("==== Struk Pembelian ====")
                        print(f"Nama Menu   : {menu[pilihan - 1][1]}")
                        print(f"Jumlah      : {jumlah}")
                        print(f"Total Harga : Rp{total_harga}")
                    else:
                        print("======================================")
                        print("|          TRANSAKSI GAGAL!!         |")
                        print("-------------------------------------|")
                        print("|        Saldo Tidak Mencukupi!      |")
                        print("|        Silahkan Lakukan Topup!     |")
                        print("======================================")
                elif metode_pembayaran == '2':
                    if user[nama]['e-pay'] >= total_harga:
                        user[nama]['e-pay'] -= total_harga
                        print("=======================================================")
                        print(f"Pembelian berhasil. Saldo e-pay sekarang: {user[nama]['e-pay']}")
                        print("=======================================================")
                        print("==== Struk Pembelian ====")
                        print(f"Nama Menu   : {menu[pilihan - 1][1]}")
                        print(f"Jumlah      : {jumlah}")
                        print(f"Total Harga : Rp{total_harga}")
                    else:
                        print("======================================")
                        print("|   Saldo E-pay Tidak Mencukupi!!    |")
                        print("--------------------------------------")
                else:
                    print("Metode pembayaran tidak valid.")

            elif pilih_menu == '3':
                os.system("cls" if os.name == "nt" else "clear")
                if user[nama]['member'] == 'Gratisan':
                    print('Anda dapat bergabung menjadi member VIP dengan membayar menggunakan e-pay sebesar 100000.')
                    konfirmasi_gabung = input('Apakah Anda ingin bergabung menjadi member VIP? (ya/tidak): ')
                    if konfirmasi_gabung.lower() == 'ya':
                        if user[nama]['e-pay'] >= 100000:
                            user[nama]['e-pay'] -= 100000
                            user[nama]['member'] = 'VIP'
                            print('Selamat! Anda sekarang menjadi member VIP.')
                        else:
                            print('Saldo e-pay tidak mencukupi untuk bergabung menjadi member VIP.')
                    else:
                        print('Bergabung menjadi member VIP dibatalkan.')

                else:
                    print('Anda sudah menjadi member VIP.')

            elif pilih_menu == '0':
                os.system("cls" if os.name == "nt" else "clear")
                print("========================================================================")
                print("|                        PROGRAM TELAH SELESAI                         |")
                print("========================================================================")
                print("|           TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SEDERHANA            |")
                print("|              YANG DISUSUN OLEH ADINDA SALSABILLA NAURA               |")
                print("|                      SISTEM INFORMASI A'23 KELAS A                   |")
                print("|                                  |||                                 |")
                print("|                         UNIVERSITAS MULAWARMAN                       |")
                print("========================================================================")
                exit()

            else:
                print('Pilihan tidak valid. Coba lagi.\n')
    else:
        print('Nama atau PIN salah. Coba lagi.\n')
