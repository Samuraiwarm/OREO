from oreo import oreo

# prompt
n = input("> How many sets of OREOs do you want? ")

# function
def multiOreo():
	max = 0
	max_oreo = ""
	for i in range(int(n)):
		size, output = oreo()
		if size > max:
			max, max_oreo = (size, output)
	print('\nLongest oreo =', max_oreo, 'length = ', max)

# main
def main():
	multiOreo()
  
if __name__== "__main__":
	main()
