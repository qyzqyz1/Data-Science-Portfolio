
# coding: utf-8

# In[1]:


class trapezoid:
    def __init__(self, top=0, bottom=0, height=0):
        self.top = top
        self.bottom = bottom
        self.height = height
    
    def setvalues(self):
        try: 
            self.top = float(input("Enter the top length: "))
        except:
            self.top = "error"
        try:
            self.bottom = float(input("Enter the bottom length: "))
        except:
            self.bottom = "error"
        try:
            self.height = float(input("Enter the height: "))
        except:
            self.height = "error"
    
    def area(self):
        try:
            self.area = round((self.top + self.bottom) * self.height/2, 2)
            return self.area
        except:
            return ("error")

