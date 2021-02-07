#Jackson Eubank
#CS362
#HW4 - Array

import unittest;
import arrayAvg;

class TestArray(unittest.TestCase):
    def test_average(self):
        testAvg = arrayAvg.getAverage([1,2,3]);
        self.assertEqual(testAvg,2);
        
    def test_err_if_str(self):
        self.assertRaises(TypeError,arrayAvg.getAverage,[1,"apple",3]);

    def test_err_if_size_zero(self):
        self.assertRaises(ValueError,arrayAvg.getAverage,[]);


if (__name__ == '__main__'):
    unittest.main();
