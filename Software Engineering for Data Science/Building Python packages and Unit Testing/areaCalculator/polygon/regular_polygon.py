
# coding: utf-8

# In[1]:



from math import pi, tan
class regular_polygon:
    def __init__(self,length=0,num_sides=0):
        self.length = length
        self.num_sides = num_sides
    
    def setvalues(self):
        self.length = float(input("Enter the length: "))
        self.num_sides = int(input("Enter the number of sides: "))
        if self.num_sides <= 2:
            print("A polygon must have minimum 3 sides")

    def area(self):
        if self.num_sides>2:
            return(self.num_sides*self.length**2/(4*tan(pi/self.num_sides)))
        else:
            return("Cannot Compute!")
            
    def display(self):
        print("The area of this {} sided regular polygon with length {} is {}".format(self.num_sides, self.length, self.area()))

