import unittest
from mtdl import MultiThreadDownloader
from hashlib import sha256
import subprocess

class Tester(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_download(self):
        link = "https://free.nchc.org.tw/vlc/vlc/3.0.20/win64/vlc-3.0.20-win64.exe"
        d = MultiThreadDownloader(link, filename="cache")
        d.start()
        with open("cache", "rb") as file:
            self.assertEqual(sha256(file.read()).hexdigest(), "d8055b6643651ca5b9ad58c438692a481483657f3f31624cdfa68b92e8394a57")
            
    def test_download2(self):
        link = "https://free.nchc.org.tw/vlc/vlc/3.0.20/win64/vlc-3.0.20-win64.exe"
        d = MultiThreadDownloader(link, filename="cache2", chunk_size=100000000)
        d.start()
        with open("cache2", "rb") as file:
            self.assertEqual(sha256(file.read()).hexdigest(), "d8055b6643651ca5b9ad58c438692a481483657f3f31624cdfa68b92e8394a57")
            
    def test_cli(self):
        link = "https://free.nchc.org.tw/vlc/vlc/3.0.20/win64/vlc-3.0.20-win64.exe"
        status = subprocess.call(f"mtdl {link} -c 100000 -o cache3")
        with open("cache3", "rb") as file:
            self.assertEqual(sha256(file.read()).hexdigest(), "d8055b6643651ca5b9ad58c438692a481483657f3f31624cdfa68b92e8394a57")
            self.assertEqual(status, 0)
            
if __name__ == "__main__":
    unittest.main()
