import math

def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

shape = ''

while shape != 'quit':
    shape = input('what shape do you have? ').lower()
    
    if shape == 'square':
        side = float(input('what is the length of the side? '))
        area = compute_area_square(side)
        print(f'The area is: {area}')

    elif shape == 'rectangle':
        length = float(input('What is the length? '))
        width = float(input('What is the width? '))
        area = compute_area_rectangle(length, width)
        print(f'The area of the rectangle is: {area}')

    elif shape == 'circle':
        radius = float(input('What is the radius? '))
        area = compute_area_circle(radius)
        print(f'The area of the circle is: {area}')


