from flask import Flask, render_template, request, redirect, url_for
from models import Pelanggan, Film, Jadwal, Tiket, Pemesanan

app = Flask(__name__)

# Data Sementara
films = [
    Film(1, "Film A", "Action", 120),
    Film(2, "Film B", "Drama", 90)
]

jadwals = [
    Jadwal(1, films[0], "2024-05-28", "18:00"),
    Jadwal(2, films[1], "2024-05-28", "20:00")
]

pelanggan = Pelanggan(1, "User1", "user1@example.com", "password")

@app.route('/')
def index():
    return render_template('index.html', films=films)

@app.route('/film/<int:film_id>')
def film(film_id):
    selected_film = next((f for f in films if f.id == film_id), None)
    film_jadwals = [j for j in jadwals if j.film.id == film_id]
    return render_template('film.html', film=selected_film, jadwals=film_jadwals)

@app.route('/jadwal/<int:jadwal_id>', methods=['GET', 'POST'])
def jadwal(jadwal_id):
    selected_jadwal = next((j for j in jadwals if j.id == jadwal_id), None)
    if request.method == 'POST':
        tiket = Tiket(len(pelanggan.pemesanan) + 1, selected_jadwal, pelanggan)
        pemesanan = Pemesanan(len(pelanggan.pemesanan) + 1, tiket, "Pending")
        pelanggan.pemesanan.append(pemesanan)
        return redirect(url_for('index'))
    return render_template('jadwal.html', jadwal=selected_jadwal)

@app.route('/pemesanan')
def pemesanan():
    return render_template('pemesanan.html', pemesanan=pelanggan.pemesanan)

if __name__ == '__main__':
    app.run(debug=True)
