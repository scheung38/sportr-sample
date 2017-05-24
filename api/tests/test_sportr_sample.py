import unittest
from api.sportr_sample import get_url, start, multiply


class TestGetUrl(unittest.TestCase):
    def test_get_valid_url(self):
        self.assertEqual(
            '[{"url": "http://www.bbc.co.uk/sport/tennis/37268846", "headline": "US Open 2016: Novak Djokovic beats Kyle Edmund in fourth round - BBC Sport", "images": [{"url": "http://ichef.bbci.co.uk/onesport/cps/624/cpsprodpb/2AC8/production/_91025901_djokovicedmund.jpg", "caption": "Edmund was unable to make much of an impression against Djokovic"}]}]',
            get_url('http://www.bbc.co.uk/sport/tennis/37268846'))


class TestGetBadUrl(unittest.TestCase):
    def test_get_invalid_url(self):
        self.assertEqual(None, get_url('http://www.bbc.co.uk/sport/tennis/xxx'))


class TestGetRandomUrl(unittest.TestCase):
    def test_get_random_text(self):
        self.assertEqual(None, get_url('somerandomtext'))


# class TestStart(unittest.TestCase):
#     def test_start(self):
#         # self.assertEqual(expected, start())
#         assert False  # TODO: implement your test here


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(6, multiply(2, 3))
        # assert False # TODO: implement your test here


if __name__ == '__main__':
    unittest.main()
