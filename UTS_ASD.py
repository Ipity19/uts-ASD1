from prettytable import PrettyTable

class HijabStore:
    def __init__(self):
        self.hijab_list = {
            '001': ['Segi Empat', 'Black', 'tersedia', 20000],
            '002': ['Segi Empat', 'Blue', 'tersedia', 20000],
            '003': ['Segi Empat', 'White', 'tersedia', 20000],
            '004': ['Pashmina Inner', 'Dusty pink', 'tersedia', 35000],
            '005': ['Pashmina Inner', 'Black', 'tersedia', 35000],
            '006': ['Pashmina Inner', 'Grey', 'tersedia', 35000],
            '007': ['Pashmina Crinkle', 'Black', 'tersedia', 35000],
            '008': ['Pashmina Crinkle', 'Coksu', 'tersedia', 35000],
            '009': ['Pashmina Crinkle', 'Cream', 'tersedia', 35000],
            '010': ['Pashmina kaos', 'Black', 'tersedia', 40000],
            '011': ['Pashmina Kaos', 'Milo', 'tersedia', 40000],
            '012': ['Pashmina Kaos', 'Soft Pink', 'tersedia', 40000],
            '013': ['Bergo ', 'Black', 'tersedia', 45000],
            '014': ['Bergo ', 'White', 'tersedia', 45000],
            '015': ['Bergo', 'Navy', 'tersedia', 45000],
            '016': ['Mukena ', 'White', 'tersedia', 250000],
            '017': ['Mukena', 'Black', 'tersedia', 250000],
            '018': ['Mukena', 'Milo', 'tersedia', 250000]
        }
        self.cart = []

    def display_hijab(self):
        table = PrettyTable(['ID', 'Tipe Hijab', 'Warna Hijab', 'Status', 'Harga'])
        for id, hijab in self.hijab_list.items():
            table.add_row([id] + hijab)
        print(table)

    def order_hijab(self):
        self.display_hijab()
        while True:
            id = input('Masukkan ID hijab yang ingin dipesan (Ketik "selesai" untuk selesai): ')
            if id.lower() == 'selesai':
                break
            quantity = int(input('Masukkan jumlah pesanan: '))

            if id in self.hijab_list:
                hijab = self.hijab_list[id]
                total_price = hijab[3] * quantity
                self.cart.append([id] + hijab + [quantity, total_price])
                print(f'{hijab[0]} ({hijab[1]}, {quantity} buah) telah ditambahkan ke keranjang.')
            else:
                print('Hijab dengan ID tersebut tidak ditemukan.')

    def display_cart(self):
        if self.cart:
            table = PrettyTable(['ID', 'Tipe Hijab', 'Warna Hijab', 'Status', 'Harga', 'Jumlah pesanan', 'Total Harga'])
            for item in self.cart:
                table.add_row(item)
            print(table)
        else:
            print('Keranjang belanja kosong.')

    def clear_cart(self):
        self.cart = []
        print('Keranjang belanja berhasil dikosongkan.')

    def menu_pembeli(self):
        while True:
            print('===================================================')
            print('|        SELAMAT DATANG DI HIJAB STORE            |')
            print('===================================================\n')
            print('[1.] Lihat Daftar Hijab')
            print('[2.] Pesan Hijab')
            print('[3.] Lihat Keranjang Belanja')
            print('[4.] Kosongkan Keranjang Belanja')
            print('[5.] Keluar\n')
            choice = input('Apa yang Anda Butuhkan? :')

            if choice == '1':
                self.display_hijab()
            elif choice == '2':
                self.order_hijab()
            elif choice == '3':
                self.display_cart()
            elif choice == '4':
                self.clear_cart()
            elif choice == '5':
                print('Terima kasih telah menggunakan layanan kami.')
                break
            else:
                print('Pilihan tidak valid. Silakan coba lagi.')

    def menu_admin(self):
        usn = input('Masukkan username :')
        pw = input('Masukkan Password :')
        if usn == 'Fy' and pw == '7':
            while True:
                print('\n===== MENU ADMIN =====')
                print('[1.] Tampilkan Daftar Hijab')
                print('[2.] Tambahkan Hijab Baru')
                print('[3.] Perbarui Informasi Hijab')
                print('[4.] Hapus Tipe Hijab')
                print('[5.] Keluar\n')
                choice = input('Masukkan Pilihan Anda :')

                if choice == '1':
                    self.display_hijab()
                elif choice == '2':
                    self.add_new_hijab()
                elif choice == '3':
                    self.update_hijab()
                elif choice == '4':
                    self.delete_hijab()
                elif choice == '5':
                    break
                else:
                    print('Pilihan tidak valid. Silakan coba lagi.')
        else:
            print('Username atau password salah.')

    def add_new_hijab(self):
        self.display_hijab()
        tipe = input('Masukkan Tipe hijab yang ingin ditambahkan :')
        warna = input("Masukkan warna hijab yang ingin ditambahkan :")
        status = input("Masukkan Status hijab yang ingin ditambahkan:")
        harga = int(input('Masukkan harga hijab yang ingin ditambahkan :'))

        new_id = self.generate_id()
        self.hijab_list[new_id] = [tipe, warna, status, harga]
        print('Berhasil menambahkan hijab baru.')

    def update_hijab(self):
        self.display_hijab()
        id = input('Masukkan ID hijab yang akan diubah: ')
        if id in self.hijab_list:
            hijab = self.hijab_list[id]
            print(f'Informasi Hijab yang akan diubah: {hijab}')
            tipe = input('Masukkan Tipe hijab baru: ')
            warna = input('Masukkan warna hijab baru: ')
            status = input('Masukkan Status hijab baru: ')
            harga = int(input('Masukkan harga hijab baru: '))
            self.hijab_list[id] = [tipe, warna, status, harga]
            print('Data hijab berhasil diubah.')
        else:
            print('Hijab dengan ID tersebut tidak ditemukan.')

    def delete_hijab(self):
        self.display_hijab()
        id = input('Masukkan ID hijab yang ingin dihapus: ')
        if id in self.hijab_list:
            del self.hijab_list[id]
            print('Data hijab berhasil dihapus.')
        else:
            print('Hijab dengan ID tersebut tidak ditemukan.')

    def generate_id(self):
        last_id = max(map(int, self.hijab_list.keys())) if self.hijab_list else 0
        new_id = str(int(last_id) + 1).zfill(3)
        return new_id

    def pilih_menu(self):
        while True:
            print('===================================================')
            print('|        SELAMAT DATANG DI HIJAB STORE            |')
            print('===================================================\n')
            print('[1.] Pembeli')
            print('[2.] Admin  ')
            pilihan = input('Masukkan Pilihan Anda :')
            if pilihan == '1':
                self.menu_pembeli()
            elif pilihan == '2':
                self.menu_admin()
            else:
                print('Maaf inputan yang anda masukan salah, Silahkan input (1/2) saja.')

store = HijabStore()
store.pilih_menu()
