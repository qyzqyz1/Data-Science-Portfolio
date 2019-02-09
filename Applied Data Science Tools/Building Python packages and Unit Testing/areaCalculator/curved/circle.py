
# coding: utf-8

# In[ ]:


from math import pi
class circle:
    def __init__(self,radius=0):
        self.radius = radius

    def setvalues(self):
        try:
            self.radius = float(input("Enter the radius: "))
        except ValueError:
            self.radius="Error"

    def area(self):
        try:
            self.area=round(pi*self.radius**2,2)
            return self.area
        except TypeError:
            return("Error")




# In[ ]:
