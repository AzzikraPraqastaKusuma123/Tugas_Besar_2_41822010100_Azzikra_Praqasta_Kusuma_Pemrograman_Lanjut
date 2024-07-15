import psycopg2

def get_buku(judul):
    try:
        connection = psycopg2.connect(
            user="username",
            password="password",
            host="localhost",
            port="5432",
            database="perpustakaan"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM buku WHERE judul=%s", (judul,))
        record = cursor.fetchone()
        
        if record:
            buku = Buku(*record[1:])
            return buku
        else:
            raise Exception("Buku tidak ditemukan")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

def post_buku(buku):
    try:
        connection = psycopg2.connect(
            user="username",
            password="password",
            host="localhost",
            port="5432",
            database="perpustakaan"
        )
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.konten, buku.iktisar)
        )
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
