# capstone_project_2_arka_-_program_offline_store
Program ini digunakan untuk manajemen stok dan kasir sederhana berbasis python. Fiturnya adalah CRUD data produk, riwayat penghapusan, sistem belanja yang otomatis menghitung subtotal, memproses pembayaran, dan memperbarui jumlah stok secara real-time. Program ini bisa digunakan oleh usaha kecil hingga menengah yang membutuhkan aplikasi sederhana untuk menjalankan bisnis secara offline.
## Penjelasan Fitur Utama
- **Sistem Kasir (Belanja):** Memilih produk, menghitung subtotal otomatis, dan validasi pembayaran.
- **Update Stok Otomatis:** Stok berkurang secara real-time setelah transaksi berhasil.
- **Manajemen Inventaris:** Menambah produk baru ke database atau menghapus produk yang sudah ada.
- **Riwayat Penghapusan:** Mencatat produk apa saja yang pernah dihapus dari daftar
## Penjelasan coding

### **1. List Produk**
![image alt](https://github.com/arkaruz/capstone_project_2_arka_-_program_offline_store/blob/main/images/gambar%201.jpg?raw=true)

**Pada bagian awal** terdapat variable produk_list yang berisi informasi tentang detail produk dan memiliki 6 kolom yaitu
  - Nama Produk
  - Jenis Lengan
  - Ukuran
  - Jumlah Stok
  - Harga
  - SKU 

Lalu pada variable riwayat_hapus digunakan untuk wadah yang berisi data produk yang di hapus saat program berjalan

### **2. Visualisasi Data**
![image alt](https://github.com/arkaruz/capstone_project_2_arka_-_program_offline_store/blob/main/images/gambar%202.png?raw=true)

**Pada bagian def yang pertama** digunakan untuk menampilkan list produk dalam bentuk tabel yang rapi. 
Saya menggunakan def karena fungsi ini akan sering di tampilkan di setiap fitur program

### **3. Fitur Belanja**
![image alt](https://github.com/arkaruz/capstone_project_2_arka_-_program_offline_store/blob/main/images/gambar%203.png?raw=true)

Pada bagian ini adalah Fitur utama dari sistem kasir (fitur_belanja):
  -  **Manajemen Keranjang:** Menggunakan list keranjang untuk menampung item yang dipilih secara sementara sebelum proses pembayaran.
  -  **Validasi Stok:** Program secara otomatis mengecek apakah jumlah yang dibeli melebihi stok yang tersedia di produk_list. Jika tidak cukup, muncul pesan peringatan.
  -  **Penanganan Error (try-except):** Digunakan untuk memastikan pengguna memasukkan angka yang benar, mencegah program crash jika terjadi salah input.
  -  **Alur Belanja:** Terdapat sistem looping yang memungkinkan pelanggan menambah belanjaan berkali-kali sebelum akhirnya diarahkan ke fungsi pembayaran.

### **4. Proses Pembayaran**
![image alt](https://github.com/arkaruz/capstone_project_2_arka_-_program_offline_store/blob/main/images/gambar%204a.png?raw=true)
![image alt](https://github.com/arkaruz/capstone_project_2_arka_-_program_offline_store/blob/main/images/gambar%204b.png?raw=true)

Bagian ini menunjukkan mekanisme penyelesaian transaksi:
  - **Validasi Keranjang Kosong:** Jika pengguna belum memilih barang namun masuk ke menu bayar, sistem akan memberi tahu bahwa keranjang kosong dan kembali ke menu utama.
  - **Ringkasan Belanja Otomatis:** Program merangkum semua item yang dipilih ke dalam tabel, menampilkan kolom Produk, Jumlah, dan Subtotal, sehingga pembeli bisa meninjau ulang pesanan mereka.
  - **Hitung Kembalian:** Sistem meminta nominal uang dari pengguna. Jika uang cukup, sistem menghitung kembalian. Jika uang kurang, muncul pesan peringatan dan pengguna diminta memasukkan nominal kembali.
  - **Pembaruan Stok Real-Time:** Program secara otomatis mencari indeks produk di database utama dan mengurangi jumlah stok berdasarkan jumlah yang dibeli
  - **Pembatalan Transaksi:** Pengguna dapat membatalkan dengan cara memilih untuk tidak melanjutkan pembayaran. bisa digunakan untuk merevisi pesanan / tidak jadi beli

### **5. Menambahkan Produk**
![image alt](https://github.com/arkaruz/capstone_project_2_arka_-_program_offline_store/blob/main/images/gambar%205.png?raw=true)

Fungsi ini memungkinkan pengguna untuk memperbarui produk toko tanpa harus mengubah kode program secara manual:
  - Program menampilkan tabel produk terbaru terlebih dahulu, sehingga admin bisa melihat apa saja yang sudah ada sebelum menambah item baru.
  - Sistem meminta input detail untuk setiap atribut produk, mulai dari Nama, Jenis Lengan, Ukuran, hingga SKU unik.
  - Produk baru akan berada di baris paling bawah setelah ditambahkan.
  - Fungsi while True memudahkan admin untuk menambah banyak produk sekaligus tanpa harus keluar-masuk menu berkali-kali.

### **6. Menghapus Produk**
![image alt](https://github.com/arkaruz/capstone_project_2_arka_-_program_offline_store/blob/main/images/gambar%206.png?raw=true)

Fungsi ini memberikan akses admin untuk membersihkan database atau mengelola produk yang sudah tidak dijual lagi:
  - **Penghapusan Berbasis Indeks:** Admin cukup memasukkan nomor urut produk yang tampil di tabel. Program kemudian menggunakan metode .pop(idx) untuk mengeluarkan data dari list utama.
  - **Sistem Log Riwayat:** Produk yang dihapus dipindahkan ke dalam list riwayat_hapus menggunakan perintah .append(terhapus). Ini berfungsi sebagai "Recycle Bin".
  - **Fitur Monitoring:** Admin bisa melihat daftar produk apa saja yang telah dihapus melalui menu "Riwayat Produk Dihapus".

### **7. Program Utama**
![image alt](https://github.com/arkaruz/capstone_project_2_arka_-_program_offline_store/blob/main/images/gambar%207.png?raw=true)

Bagian ini merupakan program utama yang menggabungkan fungsi fungsi sebelumnya. saya meletakan di akhir supaya tidak perlu menuliskan kode berulangkali.
bagian ini menjalankan fitur utama seperti:
  - **Belanja:** memanggil fungsi belanja pada gambar no 3, dan memanggil fungsi pembayaran pada gambar no 4
  - **Menambah Produk:** memanggil fungsi menambahkan produk pada gambar no 5
  - **Menghapus Produk:** memanggil fungsi hapus produk pada gambar no 6
  - **Selesai:** menghentikan program 
