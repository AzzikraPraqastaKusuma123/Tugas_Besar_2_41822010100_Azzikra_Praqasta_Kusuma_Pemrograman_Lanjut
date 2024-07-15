class Buku:
    def __init__(self, judul, penulis, penerbit, tahun_terbit, konten, iktisar):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        self.konten = konten
        self.iktisar = iktisar

    def read(self, halaman):
        for i in range(min(halaman, len(self.konten))):
            print(self.konten[i])

    def __str__(self):
        return f"{self.judul} by {self.penulis}"
