from PIL import Image
offset = -100
earth = Image.open('earth.jpg')
spaceshuttle = Image.open('spaceshuttle.jpg')
combined = Image.new('RGB', earth.size)
pixels_earth = earth.load() 
pixels_spaceshuttle = spaceshuttle.load()
pixels_combined = combined.load()
width, height = earth.size
color = pixels_spaceshuttle[1, 1]

for x in range(0, width):
    for y in range(0, height):
        (r,g,b) = pixels_spaceshuttle[x,y]
        if r <= 80 and g>= 129 and b <= 82:
            pixels_spaceshuttle[x, y]  = pixels_earth[x, y]
        pixels_combined[x,y] = pixels_spaceshuttle[x,y]
combined.save('space.jpg')
combined.show()
