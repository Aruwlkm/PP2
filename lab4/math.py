import math
# Convert degree to radian
degree = 15
radian = math.radians(degree)
print("Degree:", degree)
print("Radian:", radian)



#Area of trapezoid
height = 5
base1 = 5
base2 = 6
area = 0.5 * (base1 + base2) * height
print("Area of trapezoid:", area)



#Area of regular polygon
n_sides = 4
length = 25
area_polygon = (n_sides * (length ** 2)) / (4 * math.tan(math.pi / n_sides))
print("Area of polygon:", area_polygon)



#Area of parallelogram
base = 5
height = 6
area_para = base * height
print("Area of parallelogram:", area_para)