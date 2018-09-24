__author__ = 'TheRusher28'
__mantainer__ = 'TheRusher28'
__email__ = 'therusher28@gmail.com'
__status__ = 'Beginner'

operation = input("What geometric shape do you need calculate? ")
if operation == 'Triangle':
	base = input("How many cm is the base? ")
	height = input("How many cm is height? ")
	print(float(base) * float(height) / 2)
elif operation == 'Square':
	base = input("How many cm is the base? ")
	print(float(base) * float(base))
elif operation == 'Circle':
	radio = input("How many cm is the radio? ")
	print(3.141592654 * float(radio) * float(radio))
elif operation == 'Rectangle':
	base = input("How many cm is the base? ")
	height = input("How many cm is height? ")
	print(float(base) * float(height))
elif operation == 'Parallelograms':
	base = input("How many cm is the base? ")
	height = input("How many cm is height? ")
	print(float(base) * float(height))
elif operation == 'Regular polygons':
	Side = input("How many cm is the side? ")
	Side_numbers = input("How many sides it has? ")
	Perimeter = float(Side) * float(Side_numbers)
	apothem = input("How many cm is the apothem? ")
	print(float(Perimeter) * float(apothem) / 2)
elif operation == 'Trapezoid':
	B_Base = input("How many cm is the biggest base? ")
	s_Base = input("How many cm is the smallest base? ")
	Bases = float(B_Base) + float(s_Base)
	height = input("How many cm is the height? ")
	print(float(Bases) * float(height) / 2)
else:
	print("Yoy have not written any operation")
