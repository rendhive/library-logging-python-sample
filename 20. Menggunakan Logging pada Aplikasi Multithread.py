import logging
import threading

logging.basicConfig(level=logging.INFO)

def thread_function(name):
    logging.info(f'Thread {name}: mulai')
    logging.info(f'Thread {name}: selesai')

# Membuat dan menjalankan beberapa thread
threads = []
for index in range(3):
    thread = threading.Thread(target=thread_function, args=(index,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
# Fungsi: Menggunakan logging dalam aplikasi yang menggunakan threading.
# Kondisi: Ketika Anda ingin memahami interaksi antar thread melalui logging.