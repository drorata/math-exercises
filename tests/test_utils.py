import unittest
import numpy as np
import mathexercises.utils as utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.numbers = ['31', '14', '2']
        self.ops = [np.subtract, np.multiply]

    def test_build_string(self):
        self.assertEqual(
            utils.build_string(self.numbers,
                               self.ops),
            '31-14,*2'
        )
