import random

# init
oreo_terminate = 0.1
oreo_o = oreo_re = (1-oreo_terminate)/2

# function 
def oreo():
	oreo = ""
	count = 0
	while True:
		rand = random.random()
		if rand < oreo_terminate:
			if oreo == "":
				oreo = "- v o i d -"
			print(oreo)
			return count, oreo
		elif rand < (oreo_terminate + oreo_o):
			oreo += "O"
		else:
			oreo += "RE"
		count += 1

# main
def main():
	oreo()
  
if __name__== "__main__":
	main()
