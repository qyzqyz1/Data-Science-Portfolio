
# coding: utf-8

# In[ ]:


import unittest

from areaCalculator.curved.ellipse import ellipse as elp


class Test_Ellipse(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Use the folloing major and minor axis sets:\n 1st: (4,e)\n 2nd: (8,2)\n 3rd: (a, 1.6)\n 4th: (17.8, 23)\n 5th: (28, 3.5)")
        cls.e1 = elp()
        cls.e2 = elp()
        cls.e3 = elp()
        cls.e4 = elp()
        cls.e5 = elp()
        print("\nEnter major and minor axis for the 1st test ellipse: ")
        cls.e1.setvalues()
        print("\nEnter major and minor axis for the 2nd test ellipse: ")
        cls.e2.setvalues()
        print("\nEnter major and minor axis for the 3rd test ellipse: ")
        cls.e3.setvalues()
        print("\nEnter major and minor axis for the 4th test ellipse: ")
        cls.e4.setvalues()
        print("\nEnter major and minor axis for the 5th test ellipse: ")
        cls.e5.setvalues()

    def setUp(self):
        print("Set up")

    def test_setvalues(self):
        print("test_setvalues")
        self.assertEqual(self.e1.ax_A, 4)
        self.assertEqual(self.e1.ax_B, "Error")
        self.assertEqual(self.e2.ax_A, 8)
        self.assertEqual(self.e2.ax_B, 2)
        self.assertEqual(self.e3.ax_A, "Error")
        self.assertEqual(self.e3.ax_B, 1.6)
        self.assertEqual(self.e4.ax_A, 17.8)
        self.assertEqual(self.e4.ax_B, 23)
        self.assertEqual(self.e5.ax_A, 28)
        self.assertEqual(self.e5.ax_B, 3.5)

    def test_area(self):
        print("test_area")
        self.assertAlmostEqual(self.e1.area(), "Error")
        self.assertEqual(self.e2.area(), 50.27)
        self.assertEqual(self.e3.area(), "Error")
        self.assertAlmostEqual(self.e4.area(), 1286.17)
        self.assertAlmostEqual(self.e5.area(), 307.88)

    def tearDown(self):
        print("Tear Down\n")

    @classmethod
    def tearDownClass(cls):
        print("All tests completed")

unittest.main(argv=[''], verbosity=2, exit=False)
