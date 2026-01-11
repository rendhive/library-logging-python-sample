import logging

# Mengatur logging dengan timestamp
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

logging.info("Log ini mencatat waktu dan pesan")
# Fungsi: Mencatat informasi waktu bersama pesan log.
# Kondisi: Ketika Anda ingin melacak waktu saat logging dijalankan.