def fibonacci(pre_last, last, count, sum):
	if pre_last == None:
		print(0)
		print(1)
		count += 1
		return fibonacci(0,1, count, 1)
	if count > 8:
		print(f"sum - {sum}")
		return last

	current = pre_last+last
	sum+=current
	print(current)
	count += 1
	return fibonacci(last, current, count, sum)


if __name__ == '__main__':
	fibonacci(None, 0, 1, 0)
