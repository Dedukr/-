import matplotlib.pyplot as plt
import numpy as np

# Y(x)=2^x*sin(10x), x=[-3...3]
def main():
	x=[x for x in range(-3,4)]
	print(x)
	y=[pow(2,x*np.sin(10*x)) for x in x]
	plt.plot(x,y, "r-", lw=5, label="Y(x)=2^x*sin(10x)")
	plt.title("Graph", fontsize=24)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.legend(loc="upper center")
	plt.grid()


	plt.show()


if __name__ == "__main__":
	main()
