import logging

# Mengatur logging ke file
logging.basicConfig(filename='app.log', level=logging.DEBUG)

logging.debug("Debugging pesan ke file")
# Fungsi: Mengirimkan log ke file alih-alih ke konsol.
# Kondisi: Ketika Anda perlu menyimpan riwayat log untuk analisis atau audit.