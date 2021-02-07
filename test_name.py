#Jackson Eubank
#CS362
#HW4 - Full Name

import unittest;
import name;

class TestName(unittest.TestCase):
    def test_full_name(self):
        testName = name.getFullName("Jackson","Eubank");
        self.assertEqual(testName,"Jackson Eubank");

    def test_err_if_first_empty(self):
        self.assertRaises(ValueError,name.getFullName,"","Eubank");

    def test_err_if_last_empty(self):
        self.assertRaises(ValueError,name.getFullName,"Jackson","");
        
    def test_err_if_first_digits(self):
        self.assertRaises(TypeError,name.getFullName,"12","Three Four");

    def test_err_if_last_digits(self):
        self.assertRaises(TypeError,name.getFullName,"One Two","34");


if (__name__ == '__main__'):
    unittest.main();
