from oreo import oreo

# prompt
n = input("> How many sets of OREOs do you want? ")

# function
def multiOreo():
	max = 0
	max_oreo = ""
	for i in range(int(n)):
		oreo_count, output = oreo()
		size = sum(list(oreo_count.values()))
		if size > max:
			max, max_oreo, max_oreo_count = (size, output, oreo_count)
	print('\nLongest oreo =', max_oreo, ', length =', max)
	print('oreo count:', max_oreo_count) # only the latest max is displayed

# main
def main():
	multiOreo()
  
if __name__== "__main__":
	main()
