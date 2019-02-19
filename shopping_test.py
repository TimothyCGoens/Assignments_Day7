import unittest
from store import Store
from items import GroceryItem



class ShoppingListTest(unittest.TestCase):

    def SetUp(self):
        self.grocery_item = GroceryItem()
        self.store = Store()

    def test_add_items(self):
        print("Test add items")
        result = self.add_item(chips)
        self.assertEqual(chips, result)

    def test_add_store(self):
        print("Test add store")
        result = self.store(HEB)
        self.assertEqual(HEB, result)

unittest.main()
