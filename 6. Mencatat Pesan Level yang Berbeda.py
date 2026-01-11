import logging

# Mengatur logging
logging.basicConfig(level=logging.DEBUG)

logging.debug("Ini debug")
logging.info("Ini informasi")
logging.warning("Ini peringatan")
logging.error("Ini kesalahan")
logging.critical("Ini kritis")
# Fungsi: Mencatat berbagai level pesan log.
# Kondisi: Ketika Anda perlu mencatat setiap level penting untuk pemecahan masalah.