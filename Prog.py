User_Input=input("Enter the name of the shape wich's area you want to calculate: ")
if User_Input in ("Square","square","SQUARE"):
    length=int(input("Enter the length of the square: "))
    width=int(input("Enter the width of the square: "))
    area=length*width
    print("The area of the square is: ",area)
elif User_Input in ("Rectangle","rectangle","RECTANGLE"):
    length=int(input("Enter the length of the rectangle: "))
    width=int(input("Enter the width of the rectangle: "))
    area=length*width
    print("The area of the rectangle is: ",area)
elif User_Input in ("Triangle","triangle","TRIANGLE"):
    base=int(input("Enter the base of the triangle: "))
    height=int(input("Enter the height of the triangle: "))
    area=(base*height)/2
    print("The area of the triangle is: ",area)
elif User_Input in ("Circle","circle","CIRCLE"):
    radius=int(input("Enter the radius of the circle: "))
    area= 3.142*radius*radius
    print("The area of the circle is: ",area)
else:
    input("This is not valid. Try again and be sure you wrote it right")