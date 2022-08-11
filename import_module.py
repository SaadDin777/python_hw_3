from math import pi as p

def house_square_footage():
    length = int(input("What is the length you are trying to measure? "))
    width = int(input("What is the width you are trying to measure? "))

    square_footage = length * width

    print("The house's square footage is: ", square_footage)


def circumference_of_circle():
    radius = float(input("What is the radius? "))
    circumference = p*radius*radius
    print("The circumference of this circle is = ", circumference)
