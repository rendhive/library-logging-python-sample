import logging

# Membuat logger dan handler
logger = logging.getLogger('multi_file_logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info("Ini informasi juga dicetak di konsol")
logger.error("Ini kesalahan yang dicatat di file")
# Fungsi: Mencatat log ke beberapa target.
# Kondisi: Ketika Anda ingin log ke konsol dan file secara bersamaan.