import unittest
from crawler import *

class TestCrawler(unittest.TestCase):

    def setUp(self):
         bot = crawler(None, "urls.txt")
         bot.crawl(depth=1)
         self.inverted_index = bot.get_inverted_index()
         self.resolved_inverted_index = bot.get_resolved_inverted_index()

    def test_get_inverted_index(self):
        self.assertEqual({1: set([1]), 2: set([1]), 3: set([1])},self.inverted_index)

    def test_get_resolved_inverted_index(self):
        expected_results = {u'languages': set(['http://www.eecg.toronto.edu/~jzhu/csc326/csc326.html']), u'csc326': set(['http://www.eecg.toronto.edu/~jzhu/csc326/csc326.html']), u'programming': set(['http://www.eecg.toronto.edu/~jzhu/csc326/csc326.html'])}
        self.assertEqual(expected_results, self.resolved_inverted_index)

if __name__ == '__main__':
    unittest.main()