
# coding: utf-8

# In[1]:


import unittest


# In[2]:


from areaCalculator.polygon.trapezoid import trapezoid


# In[4]:


class Test_Trapezoid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Use the folloing test top, bottom and height value sets:\n 1st: (4, 5, 2)\n 2nd: (a, 2, 1.6)\n 3rd: (4.2, b, 8)\n 4th: (17.8, 23, c)\n 5th: (28, 3.5, 6.8)")
        cls.t1 = trapezoid()
        cls.t2 = trapezoid()
        cls.t3 = trapezoid()
        cls.t4 = trapezoid()
        cls.t5 = trapezoid()
        print("\nEnter dimensions for the 1st test trapezoid: ")
        cls.t1.setvalues()
        print("\nEnter dimensions for the 2nd test trapezoid: ")
        cls.t2.setvalues()
        print("\nEnter dimensions for the 3rd test trapezoid: ")
        cls.t3.setvalues()
        print("\nEnter dimensions for the 4th test trapezoid: ")
        cls.t4.setvalues()
        print("\nEnter dimensions for the 5th test trapezoid: ")
        cls.t5.setvalues()
    
    def setUp(self):
        print("Set up")
    
    def test_setvalues(self):
        print("test_setvalues")
        self.assertEqual(self.t1.top, 4)
        self.assertEqual(self.t1.bottom, 5)
        self.assertEqual(self.t1.height, 2)
        self.assertEqual(self.t2.top, "error")
        self.assertEqual(self.t2.bottom, 2)  
        self.assertEqual(self.t2.height, 1.6)
        self.assertEqual(self.t3.top, 4.2)
        self.assertEqual(self.t3.bottom, "error")
        self.assertEqual(self.t3.height, 8)
        self.assertEqual(self.t4.top, 17.8)
        self.assertEqual(self.t4.bottom, 23)
        self.assertEqual(self.t4.height, "error") 
        self.assertEqual(self.t5.top, 28)
        self.assertEqual(self.t5.bottom, 3.5)
        self.assertEqual(self.t5.height, 6.8)
        
    def test_area(self):
        print("test_area")
        self.assertEqual(self.t1.area(), 9)
        self.assertEqual(self.t2.area(), "error")
        self.assertEqual(self.t3.area(), "error")
        self.assertEqual(self.t4.area(), "error")
        self.assertEqual(self.t5.area(), 107.1)

    def tearDown(self):
        print("Tear Down\n")
        
    @classmethod
    def tearDownClass(cls):
        print("All tests completed")
        
unittest.main(argv=[''], verbosity=2, exit=False)

