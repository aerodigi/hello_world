import unittest


class OurTests(unittest.TestCase):
    def test_00_exists(self):
        self.assertTrue()
         
    def test_english(self):
        helloworld = "G'day, world!"
        output = helloworld
        self.assertTrue("G'day, world!", output)
    
    def test_french(self):
        helloworld = "Bonjour Monde!"
        output = helloworld
        self.assertTrue("Bonjour Monde!", output)
    
    def test_japanese(self):
        helloworld = "Konnichi wa!"
        output = helloworld
        self.assertTrue("Konnichi wa!", output)
    
