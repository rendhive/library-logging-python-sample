import logging

# Mengatur logging
logging.basicConfig(level=logging.ERROR)

try:
    # Membuat kesalahan pembagian dengan nol
    result = 10 / 0
except ZeroDivisionError:
    logging.error("Terjadi kesalahan pembagian dengan nol")
# Fungsi: Mencatat kesalahan saat terjadi exception.
# Kondisi: Ketika Anda ingin menangani dan mencatat kesalahan dalam aplikasi.