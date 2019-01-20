
# coding: utf-8

# In[1]:


class triangle:
    def __init__(self, side_a=0, side_b=0, side_c=0):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def setvalues(self):
        self.side_a = float(input("Enter the side_a length: "))
        self.side_b = float(input("Enter the side_b length: "))
        self.side_c = float(input("Enter the side_c length: "))
    
    def area(self):
        import math
        p = (self.side_a + self.side_b + self.side_c)/2
        area = math.sqrt(p*(p-self.side_a)*(p-self.side_b)*(p-self.side_c))
        return area
    
    def display(self):
        print("The area of this triangle is: ", self.area())

class triangle_with_height(triangle):
    def __init__(self, side_a=0, side_b=0, side_c=0, height=0, side=0):
        triangle.__init__(self, side_a, side_b, side_c)
        self.height = height
        self.side = side
    
    def setvalues(self):
        self.height = float(input("Enter the height: "))
        choice = input("The height is perpendicular to side a, b or c? ")
        if choice == 'a':
            self.side_a = float(input("Enter the side_a length: "))
            self.side = self.side_a
        elif choice == 'b':
            self.side_b = float(input("Enter the side_b length: "))
            self.side = self.side_b
        else:
            self.side_c = float(input("Enter the side_c length: "))
            self.side = self.side_c
    
    def area(self):
        return self.height * self.side /2
    
    def display(self):
        triangle.display(self)

