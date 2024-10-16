from math import sqrt
import lab2_2

def find_z(m):

	return 1 / sqrt(m + 2)

def main():
	# m = float(input("Enter a number (>-2):\n"))
	# if m<-1:
	# 	raise("Invalid number")
	# z = find_z(m)
	# print(z)
	task2()



def task2():
	start=10
	step=0.1
	n = int(input("How many days has the sportsman run?\n"))
	result = lab2_2.total(start, step, n)
	print(f"Total distance is {result:.3f}km")




if __name__ == '__main__':
	main()
