i = 6
numbers = [2, 3, 5]
primes = [1, 1, 1]

while sum(numbers) < 1000000-i:
	digits = map(int, range(2, i))

	digits[:] = [i % x for x in digits]

	from operator import mul
	p = reduce(mul, digits, 1)

	if p == 0:
#		print "Nope"

		i = i + 1

	else:
		numbers.append(i)
		primes.append(1)
		i = i + 1

print "The highest prime number under 1,000,000 consisting of the sum of consecutive prime numbers is: %d" % (sum(numbers))
print "The number of consecutive primes in that number are: %d"  % (sum(primes))
