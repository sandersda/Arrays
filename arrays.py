#def haveThree(array):
#	threes = 0
#	for (i == 0; i < len(array); i += 1):
#		if (a[i] == 3):
#			threes ++
#	return threes == 3
#print haveThree([3, 1, 3, 1, 3])
#print haveThree([3, 4, 3, 4])


the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print 'This is count %d' % number

for fruit in fruits:
	print 'A fruit of type: %s' % fruit


for i in change:
	print "I got %r" % i

elements = []

for i in range(0, 6):
	print 'Adding %d to the list.' % i
	elements.append(i)

for i in elements:
	print "Element was: %d" % i


print "\n\n\n\n\n\nCoding Bat"


def sum28(array):
	twos = 0
	for i in array:
		if i == 2:
			twos+=1
	return twos == 4

print sum28([2,2,2,2]) # Expects True
print sum28([2,2,2,3,2]) # Expects True
print sum28([2,2,2,3]) # Expects False


def count_evens(array):
	evens = 0
	for i in array:
		if i % 2 == 0:
			evens+=1
	return evens

print count_evens([2,4,5,6,8]) # Expects 4
print count_evens([2,3,5,7,9]) # Expects 1
print count_evens([2,4,4,6,8]) # Expects 5
print count_evens([2,4,3,3,8]) # Expects 3

def big_dif(array):
	max = array[0]
	min = array[0]

	for n in array:
		if n > max:
			max = n

	for n in array:
		if n < min:
			min = n
	return max - min


print big_dif([10,3,4,5,6])
print big_dif([1,33,4,5,6])
print big_dif([11,3,4,5,2])


def centered_average(array):
	
	max = array[0]
	min = array[0]
	sum = 0
	for n in array:
		if n > max:
			max = n

	for n in array:
		if n < min:
			min = n

	for n in array:
		sum += n

	length = len(array) - 2	
	average = sum - max - min
	return average / length

print "\n\n\nCentered Average\n\n\n"
print centered_average([1,2,3,4,5]) # Expects 3
print centered_average([1,4,5]) # Expects 4
print centered_average([1,16,4,25]) # Expects 10

def unlucky_13(array):
	sum = 0
	for n in array:
		if n == 13:
			return sum
		else:
			sum += n
	return sum
		

print "\n\n\n\nSum 13\n\n\n"
print unlucky_13([1,2,3,13,1,1,1,2]) # Expects 6
print unlucky_13([1,2,3,1,1,1,1,2]) # Expects 12
print unlucky_13([1,2,3,1,1,1,1,3]) # Expects 13
print unlucky_13([13,2,3,1,1,1,1,3]) # Expects 0

