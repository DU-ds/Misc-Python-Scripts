# https://puzzling.stackexchange.com/questions/98612/nn1-as-a-multiple-of-100

# n(n+1) as a multiple of 100

# Here's a puzzle I came up with while walking today:
#     For how many natural numbers n is the number n(n+1) a multiple of 100?

#     This is true for infinitely many n, so "how many" means something like 
# "one in every hundred n", an answer in that sort of form.
# There are some brute-forcey ways to do this, but also some nice shortcuts. 
# Checkmark will go (eventually) to the neatest solution.

def multiples_of_100(n):
	sum = 0
	for i in range(n):
		if (i % 4) == 0 & ((i + 1) % 25) == 0:
			sum += 1
	return sum


n = 100
print(n, n/multiples_of_100(n))
n = 500
print(n, n/multiples_of_100(n))
n = 1000
print(n, n/multiples_of_100(n))
n = 10000
print(n, n/multiples_of_100(n))
n = 100000
print(n, n/multiples_of_100(n))


def multiples_of_hundred(n):
	sum = 0
	for i in range(n):
		if ((i * (i+1)) % 100) == 0:
			sum += 1
	return sum

n = 100
print(multiples_of_hundred(n)/n)
n = 500
print(multiples_of_hundred(n)/n)
n = 1000
print(multiples_of_hundred(n)/n)
n = 10000
print(multiples_of_hundred(n)/n)
n = 100000
print(multiples_of_hundred(n)/n)

