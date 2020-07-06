import unittest
from pprint import pprint
from RandomGenerator.Random import rand_num
from RandomGenerator.GenList_WithSeed import GenListWithSeed


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testData = rand_num(1, 1000, 250, 55)

    #Generated List with seed (integers)
    def test_gen_list_with_seed_int(self):
        result = GenListWithSeed.list_int(1, 1000, 20, 55)
        result2 = GenListWithSeed.list_int(1, 1000, 20, 55)
        self.assertEqual(result, result2)
        #pprint(result)

    #Generated List with seed (decimals)
    def test_gen_list_with_seed_float(self):
        result = GenListWithSeed.list_float(1, 1000, 20, 55)
        result2 = GenListWithSeed.list_float(1, 1000, 20, 55)
        self.assertEqual(result, result2)
        #pprint(result)


if __name__ == '__main__':
    unittest.main()
