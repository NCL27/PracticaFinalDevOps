import unittest

class TestIndexPage(unittest.TestCase):
    def test_title(self):
        with open("index.html", "r") as f:
            content = f.read()
            self.assertIn("<title>Nicol Cuello</title>", content)
if __name__ == "__main__":
    unittest.main()
