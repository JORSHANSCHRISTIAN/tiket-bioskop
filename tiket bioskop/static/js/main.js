function notifyFilmSelection(filmTitle) {
    alert('Anda memilih film: ' + filmTitle);
}

function notifyJadwalSelection(tanggal, waktu) {
    alert('Anda memilih jadwal pada ' + tanggal + ' pukul ' + waktu);
}

function confirmPesanTiket() {
    return confirm('Apakah Anda yakin ingin memesan tiket untuk jadwal ini?');
}

document.addEventListener('DOMContentLoaded', function() {
    if (document.body.classList.contains('pemesanan-page')) {
        alert('Anda melihat daftar pemesanan');
    }
});
