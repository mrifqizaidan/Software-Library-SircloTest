class Cart:
    def __init__(self):
        self.cart = {}

    def tambahProduk(self, namaProduk, kuantitas):
        if namaProduk in self.cart:
            self.cart[namaProduk] += kuantitas
        else:
            self.cart[namaProduk] = kuantitas

    def hapusProduk(self, namaProduk):
        if namaProduk in self.cart:
            del self.cart[namaProduk]

    def tampilkanCart(self):
        for namaProduk, kuantitas in self.cart.items():
            print(f"{namaProduk} ({kuantitas})")
