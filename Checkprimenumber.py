# check wheather no. is prime or not

num = 140

if num > 1:

	for i in range (2,int(num** 0.5)+1):

		if (num % i) == 0:
			print(num, " Is Not a prime Number")
			print(num ,"is divisible by ", num//i)
			break
	else:
		print(num, 'is a prime number')
