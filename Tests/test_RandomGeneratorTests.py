import unittest
from pprint import pprint
from RandomGenerator.Random import rand_num
from RandomGenerator.GenList_WithSeed import GenListWithSeed
from RandomGenerator.GenNum_NoSeed import GenNumNoSeed
from RandomGenerator.GenNum_WithSeed import GenNumWithSeed
from RandomGenerator.ListItems_NoSeed import ListItemNoSeed


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testData = rand_num(1, 20, 5, 30)

    #Generated List with seed (integers)
    def test_gen_list_with_seed_int(self):
        result = GenListWithSeed.list_int(1, 20, 5, 30)
        result2 = GenListWithSeed.list_int(1, 20, 5, 30)
        self.assertEqual(result, result2)
        #pprint(result)
        #pprint(result2)

    #Generated List with seed (decimals)
    def test_gen_list_with_seed_float(self):
        result = GenListWithSeed.list_float(1, 20, 5, 30)
        result2 = GenListWithSeed.list_float(1, 20, 5, 30)
        self.assertEqual(result, result2)
        #pprint(result)
        #pprint(result2)



    #Generated Number with no seed (integer)
    def test_gen_num_no_seed_int(self):
        result = GenNumNoSeed.random_int(1, 50)
        self.assertEqual(isinstance(result, int), True)
        #pprint (result)

    #Generated Number with no seed (decimal)
    def test_gen_num_no_seed_float(self):
        result = GenNumNoSeed.random_float(1, 50)
        self.assertEqual(isinstance(result, float), True)
        #pprint (result)



    #Generated Number with seed (integer)
    def test_gen_num_seed_int(self):
        result = GenNumWithSeed.random_int(1, 50, 30)
        self.assertEqual(isinstance(result, int), True)
        #pprint (result)

    #Generated Number with seed (integer)
    def test_gen_num_seed_float(self):
        result = GenNumWithSeed.random_float(1, 50, 30)
        self.assertEqual(isinstance(result, float), True)
        #pprint (result)



    #Pick N number of items from a list without a seed
    def test_list_item_no_seed(self):
        the_list = GenListWithSeed.list_int(1, 20, 5, 30)
        result = ListItemNoSeed.list_items(the_list)
        self.assertEqual(result, 10)




if __name__ == '__main__':
    unittest.main()
