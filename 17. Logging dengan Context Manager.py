import logging
import contextlib

@contextlib.contextmanager
def log_context():
    logging.info("Masuk ke dalam konteks")
    yield
    logging.info("Keluar dari konteks")

# Mengatur logging
logging.basicConfig(level=logging.INFO)

with log_context():
    print("Di dalam konteks")
# Fungsi: Menggunakan logging dalam context manager.
# Kondisi: Ketika Anda ingin memastikan konteks dikelola dengan baik dan dampak pada logging.