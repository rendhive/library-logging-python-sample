import logging
import unittest

class TestLogging(unittest.TestCase):
    def test_logging(self):
        with self.assertLogs('root', level='INFO') as log:
            logging.info("Ini adalah test logging")
            self.assertIn("Ini adalah test logging", log.output[0])

# Menjalankan pengujian
unittest.main(argv=[''], exit=False)
# Fungsi: Menguji output logging dalam unit test.
# Kondisi: Ketika Anda ingin memverifikasi output logging dalam pengujian otomatis.