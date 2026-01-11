import logging

# Membuat logger kustom
logger = logging.getLogger('my_custom_logger')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Ini adalah pesan dari logger kustom")
# Fungsi: Membuat logger khusus dan menentukan pengaturannya.
# Kondisi: Ketika Anda ingin mencatat informasi terpisah dengan logger tertentu.