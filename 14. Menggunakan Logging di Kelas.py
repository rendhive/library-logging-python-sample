import logging

class MathOperations:
    def __init__(self):
        self.logger = logging.getLogger('MathOperations')
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            self.logger.error("Pembagian dengan nol!")
            raise

# Mengatur logger
logging.basicConfig(level=logging.ERROR)

math_op = MathOperations()
math_op.divide(10, 0)
# Fungsi: Menggunakan logging di dalam metode kelas.
# Kondisi: Ketika Anda ingin melacak kesalahan di dalam kelas.