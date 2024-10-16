def validation(num):
	if num<=0:
		raise("Should be positive numbers")

def main():
	print("For this task you should enter natural numbers (more than 0)")
	a = int(input("Enter the number for a:\n"))
	validation(a)
	b = int(input("Enter the number for b:\n"))
	validation(b)
	if a<b:
		x=a/b +5
	elif a==b:
		x=-5
	else:
		x=(a*a-b)/b
	print(f"Your x is {x}")

if __name__ == '__main__':
	main()
