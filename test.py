import unittest
import hello_world


class OurTests(unittest.TestCase):
    def test_00_exists(self):
        self.assertTrue()

    def test_english(self):
        english = 'Hello World'
        output = english    
        self.assertEqual('Hello World',output)

