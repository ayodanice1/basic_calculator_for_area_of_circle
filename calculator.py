
def calculateArea(radius) :
	pie = 3.143

	return pie * radius * radius

# Needed to run the file as a CLI program from the command line
def main():
	radius = float(input("\nPlease, enter the radius here: "))

	area = calculateArea(radius)
	print(f"The Area of the circle with radius {radius:.2f} is {area:.2f}")


# Runs the file when the program is run from the command line
main()	