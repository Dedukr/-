import numpy as np
def main():
	n = 7
	arr=np.zeros((n,n))

	for i in range(n):
		for j in range(n - i - 1, n):
			arr[i][j] = j - (n - i - 1) + 1
	print(arr)

if __name__ == '__main__':
	main()
