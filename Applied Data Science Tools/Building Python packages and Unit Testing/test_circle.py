
# coding: utf-8

# In[ ]:


import unittest

from areaCalculator.curved.circle import circle as cir


# In[11]:


class Test_Circle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Use the folloing test radius:\n 1st: 2\n 2nd: a\n 3rd: c\n 4th: 17.8\n 5th: 562")
        cls.c1 = cir()
        cls.c2 = cir()
        cls.c3 = cir()
        cls.c4 = cir()
        cls.c5 = cir()
        print("\nEnter radius for the 1st test circle: ")
        cls.c1.setvalues()
        print("\nEnter radius for the 2nd test circle: ")
        cls.c2.setvalues()
        print("\nEnter radius for the 3rd test circle: ")
        cls.c3.setvalues()
        print("\nEnter radius for the 4th test circle: ")
        cls.c4.setvalues()
        print("\nEnter radius for the 5th test circle: ")
        cls.c5.setvalues()

    def setUp(self):
        print("Set up")

    def test_setvalues(self):
        print("test_setvalues")
        self.assertEqual(self.c1.radius, 2)
        self.assertEqual(self.c2.radius, "Error")
        self.assertEqual(self.c3.radius, "Error")
        self.assertEqual(self.c4.radius, 17.8)
        self.assertEqual(self.c5.radius, 562)


    def test_area(self):
        print("test_area")
        self.assertAlmostEqual(self.c1.area(), 12.57)
        self.assertEqual(self.c2.area(), "Error")
        self.assertEqual(self.c3.area(), "Error")
        self.assertAlmostEqual(self.c4.area(), 995.38)
        self.assertAlmostEqual(self.c5.area(), 992253.19)

    def tearDown(self):
        print("Tear Down\n")

    @classmethod
    def tearDownClass(cls):
        print("All tests completed")

unittest.main(argv=[''], verbosity=2, exit=False)
