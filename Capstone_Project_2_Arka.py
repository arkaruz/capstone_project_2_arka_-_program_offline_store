from prettytable import PrettyTable

# Database Produk Awal
produk_list = [
    ['kaos hitam', 'lengan panjang', 'l', 20, 120000, 'sbl-01'],
    ['kaos hitam', 'lengan panjang', 'xl', 20, 120000, 'sbl-02'],
    ['kaos hitam', 'lengan pendek', 'l', 20, 99000, 'sbs-01'],
    ['kaos hitam', 'lengan pendek', 'xl', 20, 99000, 'sbs-02'],
    ['kaos putih', 'lengan panjang', 'l', 20, 120000, 'swl-01'],
    ['kaos putih', 'lengan panjang', 'xl', 20, 120000, 'swl-02'],
    ['kaos putih', 'lengan pendek', 'l', 20, 99000, 'sws-01'],
    ['kaos putih', 'lengan pendek', 'xl', 20, 99000, 'sws-02'],
    ['kemeja hitam', 'lengan panjang', 'l', 20, 180000, 'tbl-01'],
    ['kemeja hitam', 'lengan panjang', 'xl', 20, 180000, 'tbl-02'],
    ['kemeja hitam', 'lengan pendek', 'l', 20, 160000, 'tbs-01'],
    ['kemeja hitam', 'lengan pendek', 'xl', 20, 160000, 'tbs-02'],
    ['kemeja putih', 'lengan panjang', 'l', 20, 180000, 'twl-01'],
    ['kemeja putih', 'lengan panjang', 'xl', 20, 180000, 'twl-02'],
    ['kemeja putih', 'lengan pendek', 'l', 20, 160000, 'tws-01'],
    ['kemeja putih', 'lengan pendek', 'xl', 20, 160000, 'tws-02']
]

# Variable untuk menyimpan produk yang dihapus
riwayat_hapus = []

# def untuk menampilkan tabel list produk
def tampilkan_tabel(data):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Produk", "Lengan", "Size", "Stok", "Harga", "SKU"]
    for i, item in enumerate(data):
        tabel.add_row([i + 1] + item)
    print(tabel)

# def untuk memanggil fitur belanja
def fitur_belanja():
    keranjang = []
    while True:
        tampilkan_tabel(produk_list)
        try:
            pilih = int(input("Pilih nomor produk yang dibeli: ")) - 1
            if 0 <= pilih < len(produk_list):
                jumlah = int(input(f"Jumlah {produk_list[pilih][0]} yang dibeli: "))
                
                if jumlah <= produk_list[pilih][3]:
                    # Tambah ke keranjang [nama, qty, subtotal]
                    subtotal = jumlah * produk_list[pilih][4]
                    keranjang.append([produk_list[pilih][0], jumlah, subtotal, pilih])
                    print("Produk berhasil dimasukkan ke keranjang.")
                else:
                    print("Maaf, stok tidak mencukupi!")
            else:
                print("Nomor produk tidak tersedia.")
        except ValueError:
            print("Masukkan angka yang valid!")

        # Tanya tambah belanja
        while True:
            tambah = input("Apakah ingin menambahkan belanja? (1. yes / 2. no): ")
            if tambah == '1':
                break
            elif tambah == '2':
                # Masuk ke Pembayaran
                proses_pembayaran(keranjang)
                return
            else:
                print("Masukan angka yang benar!")

# def untuk melalkukan pembayaran dalam fitur belanja
def proses_pembayaran(keranjang):
    if not keranjang: # jika produk yang dibeli kosong, dan lanjut ke pembayaran
        print("Keranjang kosong.")
        return

    while True:
        total_belanja = 0
        print("\n--- Ringkasan Belanja ---")
        tabel_bayar = PrettyTable(["Produk", "Jumlah", "Subtotal"])
        for item in keranjang:
            tabel_bayar.add_row([item[0], item[1], item[2]])
            total_belanja += item[2]
        print(tabel_bayar)
        print(f"Total Belanja: Rp {total_belanja}")

        konfirmasi = input("Lanjutkan pembayaran? (1. yes / 2. no): ")
        if konfirmasi == '1':
            while True:
                try:
                    bayar = int(input("Masukkan nominal uang: "))
                    if bayar >= total_belanja:
                        kembalian = bayar - total_belanja
                        # Update Stok di list utama
                        for item in keranjang:
                            idx_produk = item[3]
                            qty_beli = item[1]
                            produk_list[idx_produk][3] -= qty_beli
                        
                        print(f"Kembalian: Rp {kembalian}")
                        print("--Pembayaran Berhasil, Terimakasih--")
                        return
                    else:
                        print("Mohon maaf uang anda tidak cukup, Silakan melakukan pembayaran kembali")
                except ValueError:
                    print("Masukkan angka nominal!")
        elif konfirmasi == '2':
            print("Keranjang dikosongkan. Kembali ke awal.")
            return
        else:
            print("Pilihan tidak valid.")

# def untuk menambahkan produk baru
def fitur_tambah_produk():
    while True:
        tampilkan_tabel(produk_list)
        print("\n1. Menambahkan Produk Baru")
        print("2. Selesai")
        opsi = input("Pilih menu: ")
        
        if opsi == '1':
            nama = input("Nama Produk: ")
            lengan = input("Jenis Lengan: ")
            ukuran = input("Ukuran: ")
            stok = int(input("Jumlah Stok: "))
            harga = int(input("Harga: "))
            sku = input("SKU: ")
            
            produk_list.append([nama, lengan, ukuran, stok, harga, sku])
            print("\n---Produk Berhasil Ditambahkan!---")
        elif opsi == '2':
            break
        else:
            print("Silahkan Masukan Angka yang Benar")

def fitur_hapus_produk():
    while True:
        tampilkan_tabel(produk_list)
        print("\n1. Menghapus Produk")
        print("2. Riwayat Produk Dihapus")
        print("3. Selesai")
        opsi = input("Pilih menu: ")

        if opsi == '1':
            try:
                idx = int(input("Masukkan nomor produk yang akan dihapus: ")) - 1
                if 0 <= idx < len(produk_list):
                    terhapus = produk_list.pop(idx)
                    riwayat_hapus.append(terhapus)
                    print("--Produk Berhasil Dihapus!--")
                else:
                    print("Nomor tidak ditemukan.")
            except ValueError:
                print("Masukan angka yang benar!")
        elif opsi == '2':
            if not riwayat_hapus:
                print("\nBelum ada riwayat penghapusan.")
            else:
                print("\n--- Riwayat Produk Dihapus ---")
                tampilkan_tabel(riwayat_hapus)
        elif opsi == '3':
            break
        else:
            print("Silahkan Masukan Angka yang Benar")

# Program Utama
while True:
    print("\n=== Selamat Datang di Outfit Polos ===")
    print("1. Belanja")
    print("2. Menambah Produk")
    print("3. Menghapus Produk")
    print("4. Selesai")
    
    pilihan_menu = input("Pilih Menu (1/2/3/4): ")
    
    if pilihan_menu == '1':
        fitur_belanja()
    elif pilihan_menu == '2':
        fitur_tambah_produk()
    elif pilihan_menu == '3':
        fitur_hapus_produk()
    elif pilihan_menu == '4':
        print("--- Terima kasih! ---")
        break
    else:
        print("Silahkan Masukan Angka yang Benar")