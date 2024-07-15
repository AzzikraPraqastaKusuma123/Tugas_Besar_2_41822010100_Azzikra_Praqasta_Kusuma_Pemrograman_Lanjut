from buku import Buku
from database import get_buku, post_buku
from exceptions.py import HTTPException

# Contoh penggunaan
try:
    buku = get_buku("Some Book")
    if not buku:
        raise HTTPException(404, "Buku tidak ditemukan")
    else:
        print(buku)
        buku.read(5)  # Membaca 5 halaman pertama

    # Menambah buku baru
    buku_baru = Buku(
        judul="Judul Buku Baru",
        penulis="Penulis Baru",
        penerbit="Penerbit Baru",
        tahun_terbit=2024,
        konten=["Bab 1", "Bab 2", "Bab 3"],
        iktisar="Ini adalah intisari dari buku baru."
    )
    post_buku(buku_baru)

except HTTPException as e:
    print(f"Error: {e.status_code} - {e.message}")
