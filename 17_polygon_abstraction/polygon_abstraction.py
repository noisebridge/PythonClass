"""
DRY - "Don't Repeat Yourself"

Lets implement the polygon algorithms here: http://www.mathsisfun.com/geometry/interior-angles-polygons.html

1+1=2
1+2=3
1+3=4
?? Is this a good plan?

Probably there is some general theory of addition...

Sum of 3 interior angles of a triangle = 180 degrees.

What's our goal again?
Find the sum of internal angles for a given regular convex polygon with n sides.

How do we test if a polygon is a triangle?
1. total sum of sides == 180 degrees
2. the number of sides == 3

What is a regular convex polygon?
It has sides. All sides have equal length.
Each intersection of 2 sides has an angle. All angles are equal.
How do we test that something is even a polygon?
a dictionary?


One piece of information: number of sides.

A polygon with 3 sides has an angle of 180 degrees.
(if polygon = 3, then sum of angles = 180)

GENERALIZATION ASSUMPTION 1:
For any polygon, if we divide the polygon into equal triangles,
then the number of triangles will be equal to the number of sides of the polygon.


GENERALIZATION ASSUMPTION 2:
The sum of the 'central angles' of the triangles will be 360 degrees.
To get the 'central angle' for all triangles, divide 360/'# of sides' 
so for a square, the central angle is 90 for each trangle.

"""

# we assume these variables from the fundamentals of geometry
sum_of_triangle_internal_angles = 180
one_full_rotation = 360

def calc_sum_of_internal_angles_of_polygon(number_of_sides_of_the_polygon):
    """ Return the sum of the internal angles calculated from the number of sides of the polygon.
    number_of_sides = n
    360 / n = 120
    180 - 120 = 60, 60 / 2 = 30 (corner angle of component triangle)
    ( 30 * 2 ) * 3 = 180 (sum of internal angles of polygon)

    """

    number_of_sides_of_the_polygon = float(number_of_sides_of_the_polygon)
        
    # Component Triangles = equal triangles drawn from the center to each corner.
    # central_angle_of_component_triangles
    central_angle_of_component_triangles = one_full_rotation / number_of_sides_of_the_polygon

    # all corner angles are equal.
    corner_angle_of_component_triangles = (sum_of_triangle_internal_angles - central_angle_of_component_triangles) / 2

    # This is the same as adding 2 component-triangle-corner-angles together, but we know that all corner angles are equal. 
    sum_of_internal_angles_of_polygon = corner_angle_of_component_triangles * number_of_sides_of_the_polygon * 2

    # Lets test it using our eyes and our source website.
    # We expect this to be == 180
             
    return sum_of_internal_angles_of_polygon


if __name__ == "__main__":
    """ 
    """

    test_sides = range(300,1000) # [3,4,5,6,7,8,9]

    for spaghetti in test_sides:
        print calc_sum_of_internal_angles_of_polygon(spaghetti)
        print spaghetti


