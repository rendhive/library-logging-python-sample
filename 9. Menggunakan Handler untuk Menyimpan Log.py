import logging

# Membuat log file handler
logger = logging.getLogger('file_logger')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('logfile.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.error("Ini adalah kesalahan yang dicatat ke file log")
# Fungsi: Mencatat pesan log ke file menggunakan handler.
# Kondisi: Ketika Anda ingin menyimpan log dalam file dengan cara terstruktur.