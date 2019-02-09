
# coding: utf-8

# In[ ]:


from math import pi
class ellipse:
    def __init__(self, ax_A=0, ax_B=0):
        self.ax_A = ax_A
        self.ax_B = ax_B

    def setvalues(self):
        try:
            self.ax_A = float(input("Enter the major axis length: "))
        except ValueError:
            self.ax_A = "Error"
        try:
            self.ax_B = float(input("Enter the minor axis length: "))
        except ValueError:
            self.ax_B = "Error"

    def area(self):
        try:
            self.area=round(pi*self.ax_A*self.ax_B,2)
            return(self.area)
        except:
            return("Error")
