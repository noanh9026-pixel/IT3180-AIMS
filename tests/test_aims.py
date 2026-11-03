
import unittest
from aims.main import DVD, AIMS


class TestAIMS(unittest.TestCase):

    def test_create_dvd(self):
        dvd = DVD("Titanic", "Romance", 60000)

        self.assertEqual(dvd.title, "Titanic")
        self.assertEqual(dvd.price, 60000)

    def test_initial_dvd_list(self):
        app = AIMS()

        self.assertEqual(len(app.dvds), 3)

    def test_add_dvd_to_cart(self):
        app = AIMS()
        dvd = app.dvds[0]

        app.cart.append(dvd)

        self.assertEqual(len(app.cart), 1)
        self.assertEqual(app.cart[0].title, "The Lion King")


if __name__ == "__main__":
    unittest.main()
