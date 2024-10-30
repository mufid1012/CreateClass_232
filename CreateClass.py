class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang, Panjang {self.panjang} cm, dan Lebar {self.lebar} cm"

def main():
    try:
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))
        
        persegipanjang= PersegiPanjang(panjang, lebar)
        
        print(persegipanjang)  # Menampilkan informasi persegi panjang
        print("Keliling:", persegipanjang.hitung_keliling())  # Menghitung keliling
        print("Luas:", persegipanjang.hitung_luas())          # Menghitung luas

    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka.")

if __name__ == "__main__":
    main()