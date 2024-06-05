class User:
    def __init__(self, id, nama, email, password):
        self.id = id
        self.nama = nama
        self.email = email
        self.password = password

class Pelanggan(User):
    def __init__(self, id, nama, email, password):
        super().__init__(id, nama, email, password)
        self.pemesanan = []

class Admin(User):
    pass

class Film:
    def __init__(self, id, judul, genre, durasi):
        self.id = id
        self.judul = judul
        self.genre = genre
        self.durasi = durasi

class Jadwal:
    def __init__(self, id, film, tanggal, waktu):
        self.id = id
        self.film = film
        self.tanggal = tanggal
        self.waktu = waktu

class Tiket:
    def __init__(self, id, jadwal, pelanggan):
        self.id = id
        self.jadwal = jadwal
        self.pelanggan = pelanggan

class Pemesanan:
    def __init__(self, id, tiket, status):
        self.id = id
        self.tiket = tiket
        self.status = status
