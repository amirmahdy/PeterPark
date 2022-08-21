import unittest
from plate.levenshtein import lev_dist


class TestValidator(unittest.TestCase):

    one_dist = [["book", "look"], ["bag", "lag"], ["adoor", "door"], ["appl", "apple"]]
    not_one_dist = [["book", "back"], ["bag", "slang"], ["adoor", ""], ["apple", "apll"]]

    def test_one(self):
        for od in self.one_dist:
            self.assertEqual(lev_dist(od[0], od[1]), 1, f"{od[0]} & {od[1]}")

    def test_not_one(self):
        for nod in self.not_one_dist:
            self.assertNotEqual(lev_dist(nod[0], nod[1]), 1, f"{nod[0]} & {nod[1]}")