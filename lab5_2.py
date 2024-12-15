import numpy as np
def main():
	n = 7
	arr=np.zeros((n,n))
	print(arr)

	for i in range(n):
		for j in range(n-1,0,-1):
			arr[i][j]=n
	print(arr)

if __name__ == '__main__':
	main()
