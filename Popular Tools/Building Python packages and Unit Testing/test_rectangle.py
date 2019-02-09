
# coding: utf-8

# In[6]:


import unittest


# In[7]:


from areaCalculator.polygon.rectangle import rectangle


# In[8]:


class Test_Rectangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Use the folloing test length and width value sets:\n 1st: (4, 5)\n 2nd: (b, 2)\n 3rd: (4.2, a)\n 4th: (17.8, 23)\n 5th: (28, 3.5)")
        cls.r1 = rectangle()
        cls.r2 = rectangle()
        cls.r3 = rectangle()
        cls.r4 = rectangle()
        cls.r5 = rectangle()
        print("\nEnter dimensions for the 1st test rectangle: ")
        cls.r1.setvalues()
        print("\nEnter dimensions for the 2nd test rectangle: ")
        cls.r2.setvalues()
        print("\nEnter dimensions for the 3rd test rectangle: ")
        cls.r3.setvalues()
        print("\nEnter dimensions for the 4th test rectangle: ")
        cls.r4.setvalues()
        print("\nEnter dimensions for the 5th test rectangle: ")
        cls.r5.setvalues()

    
    def setUp(self):
        print("Set up")
    
    def test_setvalues(self):
        print("test_setvalues")
        self.assertEqual(self.r1.length, 4)
        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.length, "error")
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.length, 4.2)
        self.assertEqual(self.r3.width, "error")
        self.assertEqual(self.r4.length, 17.8)
        self.assertEqual(self.r4.width, 23)
        self.assertEqual(self.r5.length, 28)
        self.assertEqual(self.r5.width, 3.5)
        
    def test_area(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), "error")
        self.assertEqual(self.r3.area(), "error")
        self.assertEqual(self.r4.area(), 409.4)
        self.assertEqual(self.r5.area(), 98)

    def tearDown(self):
        print("Tear Down\n")
        
    @classmethod
    def tearDownClass(cls):
        print("All tests completed")
        
unittest.main(argv=[''], verbosity=2, exit=False)

