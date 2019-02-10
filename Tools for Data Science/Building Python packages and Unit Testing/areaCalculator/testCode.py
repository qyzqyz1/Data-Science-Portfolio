
# coding: utf-8

# In[1]:


from areaCalculator.curved.circle import circle 
from areaCalculator.curved.ellipse import ellipse 
from areaCalculator.polygon.rectangle import rectangle 
from areaCalculator.polygon.regular_polygon import regular_polygon 
from areaCalculator.polygon.trapezoid import trapezoid 
import areaCalculator.polygon.triangle as triangle 


# In[2]:


# Test code
shape = input("Please enter a shape:\nr-Rectangle \nc-Circle \ne-Ellipse \nrp-Regular Polygon: \nt-Trapezoid \ntr-Triangle \nq-Quit\n")
while shape != "q":
    if shape == "r":
        r = rectangle()
        r.setvalues()
        r.area()
        r.display()
    elif shape == "c":
        c = circle()
        c.setvalues()
        c.area()
        c.display()
    elif shape == "e":
        e = ellipse()
        e.setvalues()
        e.area()
        e.display()
    elif shape == "rp":
        rp = regular_polygon()
        rp.setvalues()
        rp.area()
        rp.display()
    elif shape == "t":
        t = trapezoid()
        t.setvalues()
        t.area()
        t.display()
    elif shape == "tr":
        if_height = input("Do you have height information for this triangle? Y/N ")
        if if_height == "N":
            tr = triangle.triangle()
            tr.setvalues()
            tr.area()
            tr.display()
        else:
            tr = triangle.triangle_with_height()
            tr.setvalues()
            tr.area()
            tr.display()
    else:
        print("Please enter the correct shape!")
    shape = input("\nPlease enter another shape or enter q to quit: \n")
        

