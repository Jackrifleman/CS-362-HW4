#Jackson Eubank
#CS362
#HW4 - Cube

import unittest;
import cube;

class TestCube(unittest.TestCase):
    def test_volume(self):
        testVolume = cube.cubeVolume(2);
        self.assertEqual(testVolume,8);
        
    def test_volume_zero(self):
        self.assertRaises(ValueError,cube.cubeVolume,0);

    def test_volume_less_than_zero(self):
        self.assertRaises(ValueError,cube.cubeVolume,-1);


if (__name__ == '__main__'):
    unittest.main();
