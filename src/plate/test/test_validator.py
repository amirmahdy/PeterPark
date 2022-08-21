import unittest
from plate.validator import validate_plate

class TestValidator(unittest.TestCase):
    correct_format = ["MM-AA123", "M-A123", "MMM-AX1234", "M-AA1"]
    wrong_format = ["MM-A0", "MMMM-A123", "MM-AAA123", "πPi-S231", "M--123"]
    
    def test_correct(self):
        for cf in self.correct_format:
            self.assertEqual(validate_plate({"plate":cf}), True, cf)

    def test_wrong(self):
        for wf in self.wrong_format:
            self.assertEqual(validate_plate({"plate":wf}), False, wf)