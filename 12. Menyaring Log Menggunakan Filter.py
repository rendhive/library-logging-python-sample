import logging

class CustomFilter(logging.Filter):
    def filter(self, record):
        return 'error' in record.getMessage()

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

console_handler.addFilter(CustomFilter())

logger.debug("Ini hanya debug")
logger.error("Ini adalah error")
# Fungsi: Menggunakan filter untuk mengontrol apa yang dicatat.
# Kondisi: Ketika Anda ingin mencatat hanya pesan yang memenuhi kriteria tertentu.