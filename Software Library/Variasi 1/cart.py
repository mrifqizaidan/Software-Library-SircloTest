# Nama : Muhammad Rifqi Zaidan
# Instansi : Universitas Diponegoro
# Code dibuat dalam rangka memenuhi tugas Technical Test SIRCLO GROUP

class Cart:
    def __init__(self):
        self.cart = {}

    def tambahProduk(self, kodeProduk, kuantitas):
        if kodeProduk in self.cart:
            self.cart[kodeProduk] += kuantitas
        else:
            self.cart[kodeProduk] = kuantitas

    def hapusProduk(self, kodeProduk):
        if kodeProduk in self.cart:
            del self.cart[kodeProduk]

    def tampilkanCart(self):
        for kodeProduk, kuantitas in self.cart.items():
            print(f"{kodeProduk} ({kuantitas})")

#unit test
if __name__ == "__main__":
    keranjang = Cart()

    keranjang.tambahProduk("Pisang Hijau", 2)
    keranjang.tambahProduk("Semangka Kuning", 3)
    keranjang.tambahProduk("Apel Merah", 1)
    keranjang.tambahProduk("Apel Merah", 4)
    keranjang.tambahProduk("Apel Merah", 2)
    keranjang.tambahProduk("Semangka Merah", 3)

    keranjang.hapusProduk("Semangka Kuning")

    print("Isi Cart:")
    keranjang.tampilkanCart()

    keranjang.hapusProduk("Semangka Merah")

    print("Isi Cart setelah semangka merah dihapus:")
    keranjang.tampilkanCart()