import logging

# Misalkan ini adalah hasil konfigurasi logging
logging.basicConfig(level=logging.DEBUG)

def web_request_handler(request):
    logging.info("Menerima request dari %s", request.remote_addr)

# Simulasi request
web_request_handler(type('Request', (object,), {'remote_addr': '192.168.1.1'})())
# Fungsi: Menggunakan logging untuk menangani aktivitas di aplikasi web.
# Kondisi: Ketika Anda ingin merekam aktivitas web untuk keperluan audit atau debugging.