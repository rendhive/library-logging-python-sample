import logging

# Mengatur logging untuk merekam exception
logging.basicConfig(level=logging.ERROR)

try:
    x = 1 / 0
except ZeroDivisionError as e:
    logging.exception("Exception yang ditangkap")
# Fungsi: Mencatat pesan kesalahan disertai detail exception.
# Kondisi: Ketika Anda ingin melihat pelacakan kesalahan secara lengkap.