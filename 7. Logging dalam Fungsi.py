import logging

# Mengatur logging
logging.basicConfig(level=logging.DEBUG)

def my_function():
    logging.debug("Ini debug dalam fungsi")
    return 5

my_function()
# Fungsi: Mencatat log saat fungsi dipanggil.
# Kondisi: Ketika Anda ingin mengecek eksekusi fungsi dalam kode.