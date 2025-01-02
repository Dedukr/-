import math, cmath
import lab2_2


def find_z(m):
	try:
		return (1 / math.sqrt(m + 2))
	except:
		return 1 / cmath.sqrt(m + 2)


def task2():
	start = 10
	step = 0.1
	n = int(input("How many days has the sportsman run?\n"))
	result = lab2_2.total(start, step, n)
	print(f"Total distance is {result:.3f}km")


def main():
	m = float(input("Enter a number:\n"))
	z = find_z(m)
	print(z)
	task2()


if __name__ == '__main__':
	main()
