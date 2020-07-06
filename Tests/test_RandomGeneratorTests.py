import unittest
from pprint import pprint
from RandomGenerator.Random import rand_num
from RandomGenerator.GenList_WithSeed import GenListWithSeed


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testData = rand_num(1, 20, 5, 30)

    #Generated List with seed (integers)
    def test_gen_list_with_seed_int(self):
        result = GenListWithSeed.list_int(1, 20, 5, 30)
        result2 = GenListWithSeed.list_int(1, 20, 5, 30)
        self.assertEqual(result, result2)
        pprint(result)
        #pprint(result2)



    #Generated List with seed (decimals)
    def test_gen_list_with_seed_float(self):
        result = GenListWithSeed.list_float(1, 20, 5, 30)
        result2 = GenListWithSeed.list_float(1, 20, 5, 30)
        self.assertEqual(result, result2)
        #pprint(result)


if __name__ == '__main__':
    unittest.main()
