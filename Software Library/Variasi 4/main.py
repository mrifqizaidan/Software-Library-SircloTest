# Nama : Muhammad Rifqi Zaidan
# Instansi : Universitas Diponegoro
# Code dibuat dalam rangka memenuhi tugas Technical Test SIRCLO GROUP

from CartLibrary import Cart

if __name__ == "__main__":
    keranjang = Cart()

    while True:
        print("\nMenu:")
        print("1. Tambah Produk")
        print("2. Hapus Produk")
        print("3. Tampilkan Cart")
        print("4. Keluar")

        pilihan = input("Pilih tindakan (1/2/3/4): ")

        if pilihan == "1":
            namaProduk = input("Masukkan nama produk: ")
            kuantitas = int(input("Masukkan kuantitas: "))
            keranjang.tambahProduk(namaProduk, kuantitas)
            print("Produk Berhasil diinput")
        elif pilihan == "2":
            namaProduk = input("Masukkan nama produk yang akan dihapus: ")
            keranjang.hapusProduk(namaProduk)
        elif pilihan == "3":
            print("\nIsi Cart:")
            keranjang.tampilkanCart()
        elif pilihan == "4":
            print("Terima kasih. Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
