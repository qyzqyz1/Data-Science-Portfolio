
## Package Description
The package areaCalculator aims at providing the users an efficient way to calculate the area of commonly used 2D shapes. This package contains two sub packages, polygon and curved. The polygon sub-package contains the modules for calculating the areas of rectangle, triangle, trapezoid and regular polygon based on dimensions given by the user. The curved sub-package contains the modules for calculating areas of circle and ellipse.

## Function Description
Here is the description of how each type of shape is calculated.

- Rectangle:
The calculation is executed by the rectangle module which contains the class "rectangle" with four functions, __init__, setvalues, area and display. The names of the functions self explain. The user is required to provide the length and width of the rectangle through the setvalues function. The area is calculated using the formula (length * width) in the area function. Eventually the result is displayed through the display function.

- Trapezoid:
The trapezoid module has similar structure to the rectangle module except that the user is required to provide the dimension of top, bottom and height of the trapezoid. The area is calculated using the formula ((top + bottom) * height/2).

- Triangle:
The triangle modules has one super class and one sub class. The super class triangle calculates the area of any triangle given the length of each side (a,b,c). The structure of the super is similar to the above modules. The area is calculated using the following formulas:

  p = (a + b + c)/2

  area = sqrt(p*(p-a)*(p-b)*(p-c))

  The subclass triangle_with_height refers to a special case where one extra variable height is given for the calculation. It takes the   initialization from its parent class triangle for other variables (a,b,c). The user is then required to chose to which side is the 
  height perpendicular to. The area is then calculated as: height * side /2

- Regular polygon:
The regular polygon module has similar structure to the rectangle module except that the user is required to provide the length and number of sides. The area is calculated using the formula (num_sides*length**2/(4*tan(pi/self.num_sides).


- Circle:
The circle module has similar structure to the rectangle module except that the user is required to provide the radius of the circle. The area is calculated using the formula (pi*radius*radius).


- Ellipse:
The ellipse module has similar structure to the rectangle module except that the user is required to provide the major (a) and minor (b) axis of the ellipse. The area is calculated using the formula (pi*a*b).


## Test File Description


A user-interactive python test file is provided to allow specifying the type of the shape which directly corresponds to the modules/classes for the calculation. By executing the test file, the user is required to input the name of the shape until "quit" command is provided:

- r: Rectangle 

- c: Circle 

- e: Ellipse 

- rp: Regular Polygon 

- t: Trapezoid 

- tr: Triangle 

- q: Quit


