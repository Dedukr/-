def validation(n):
	if 1 < n < 9:
		return
	raise("Invalid input")


def main():
	n = int(input("enter a number (1<N<9):\n"))
	validation(n)

	for i in range(1, n + 1):
		for j in range(1, i + 1):
			print(j, end="")
		print(end="\n")



if __name__ == '__main__':
	main()
