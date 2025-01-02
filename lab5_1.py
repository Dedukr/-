def main():
	n = int(input("Enter the number of elements\n"))
	arr = []
	for i in range(n):
		arr.append(int(input(f"Enter {i + 1} element\n")))

	result = 0
	counter = 0
	for i in arr:
		if i < 0:
			result += i
			counter += 1
	if not counter:
		raise ValueError("There is no negative number")

	print(f"Result: {result / counter}")


if __name__ == '__main__':
	main()
