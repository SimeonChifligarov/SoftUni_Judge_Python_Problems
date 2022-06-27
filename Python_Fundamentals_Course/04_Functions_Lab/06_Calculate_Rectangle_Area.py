# Create a function that calculates and returns the area of a rectangle by given width and height:

def area_of_rect(width, height):
    result = width * height
    return result


width_data = int(input())
height_data = int(input())
print(area_of_rect(width_data, height_data))
