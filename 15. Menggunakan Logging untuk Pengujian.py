import logging

def sample_function():
    logging.info("Fungsi diuji")
    return True

# Mengatur logging
logging.basicConfig(level=logging.INFO)

if sample_function():
    logging.debug("Fungsi berhasil dijalankan")
# Fungsi: Menguji fungsi dengan logging untuk output debug dan info.
# Kondisi: Ketika Anda menginginkan log sebagai furnitur dokumentasi pengujian.