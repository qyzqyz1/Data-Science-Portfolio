
# coding: utf-8

# In[20]:


class rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    
    def setvalues(self):
        try:
            self.length = float(input("Enter the length: "))
        except:
            self.length = "error"
        try:
            self.width = float(input("Enter the width: "))
        except:
            self.width = "error"
    
    def area(self):
        try:
            self.area = round(self.length*self.width, 2)
            return self.area
        except:
            return ("error")

