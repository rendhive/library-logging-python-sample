import logging

# Mengatur logging dengan format khusus
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

logging.warning("Ini adalah peringatan yang dicetak dengan format baru")
# Fungsi: Memodifikasi format standar log.
# Kondisi: Saat Anda ingin menunjukkan informasi lebih kontekstual dalam log.