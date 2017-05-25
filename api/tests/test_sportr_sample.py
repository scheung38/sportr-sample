import unittest
from api.sportr_sample import get_url, start
from requests import HTTPError


class TestGetUrl(unittest.TestCase):
    def test_get_valid_url(self):
        self.assertEqual(
            '[{"url": "http://www.bbc.co.uk/sport/tennis/37268846", '
            '"headline": "US Open 2016: Novak Djokovic beats Kyle Edmund in fourth round - BBC Sport", '
            '"images": [{"url": "http://ichef.bbci.co.uk/onesport/cps/624/cpsprodpb/2AC8/production/_91025901_djokovicedmund.jpg", '
            '"caption": "Edmund was unable to make much of an impression against Djokovic"}]}]',
            get_url('http://www.bbc.co.uk/sport/tennis/37268846'))


class TestGetBadUrl(unittest.TestCase):
    def test_get_invalid_url(self):
        self.failureException(HTTPError(u'404 Client Error: Not Found for url: http://www.bbc.co.uk/sport/tennis/xxx',),
                         get_url('http://www.bbc.co.uk/sport/tennis/xxx'))


class TestGetRandomUrl(unittest.TestCase):
    def test_get_random_text(self):
        self.failureException("Invalid URL 'xyz': No schema supplied. Perhaps you meant http://xyz?", get_url('xyz'))


class TestGetValidButNoIndexUrl(unittest.TestCase):
    def test_get_valid_but_not_valid_text(self):
        self.failureException(IndexError('list index out of range',), get_url('http://www.google.com'))


# class TestStart(unittest.TestCase):
#     def test_start(self):
#         # self.assertEqual(expected, start())
#         assert False  # TODO: implement your test here


if __name__ == '__main__':
    unittest.main()
