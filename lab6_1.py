def main():
	def insertion(arr,el,pos):
		return arr.insert(pos,el)
	arr=[]
	n=int(input("How many elements:\n"))
	for i in range(n):
		arr.append(input(f"Enter the {i+1} element:\n"))
	el=input("What element do you want to insert:\n")
	pos=int(input("Where do you want to insert(index):\n"))
	insertion(arr,el,pos)
	print(arr)

if __name__=="__main__":
	main()