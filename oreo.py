import random

# init
oreo_prob = {
	'O': 180,
	'RE': 45,
	'CRE': 30,
	'SRE': 20,
}
oreo_terminate = 0.1 # probability of terminating oreo sequence

# utilities
oreo_items = list(oreo_prob.items())

# function 
def oreo():
	oreo = ""
	oreo_count = {key:0 for key in oreo_prob.keys()}
	while True:
		rand_terminate = random.random()
		if rand_terminate < oreo_terminate:
			if oreo == "":
				oreo = "- v o i d -"
			print(oreo)
			return oreo_count, oreo
		rand_choice = random.uniform(0, sum(count for name, count in oreo_items))
		counter = 0
		for name, count in oreo_items:
			counter += count
			if counter >= rand_choice:
				oreo += name
				oreo_count[name] += 1
				break

# main
def main():
	oreo_count, output = oreo()
	print(oreo_count)
  
if __name__== "__main__":
	main()
