"""
Write a function fib() that a takes an integer nnn and returns the nth Fibonacci number.

fib(0)  # => 0
fib(1)  # => 1
fib(2)  # => 1
fib(3)  # => 2
fib(4)  # => 3

"""
def fib(num):
	if num in [0,1]:
		return num
	i = 2
	f = [0,1]
	while i <= num:
		f.append(f[i-1]+f[i-2])
		i += 1

	return f[-1]

number = int(input().strip())

print(fib(number))