import re
def main():
	def Open(name,mode):
		try:
			return open(name,mode)
		except:
			print(f"There was an error while opening file {name}")
			return None

	file=Open("TF4_1", "w")
	file.write("Stepping outside your comfort zone may feel daunting - it’s where growth, opportunity, and self-discovery truly begin")
	file.close()

	file=Open("TF4_1","r")
	text = file.read()
	file.close()
	words=re.split(", | - | ", text)
	word_count={}
	for i in words:
		if len(i) not in word_count:
			word_count[len(i)]=0
		word_count[len(i)]+=1


	word_count=dict(sorted(word_count.items()))

	file=Open("TF4_2", "w")
	for i in word_count.keys():
		file.write(f"{i} characters: {word_count.get(i)} words\n")
	file.close()

	file=Open("TF4_2","r")
	text=file.read()
	print(text)
if __name__ == "__main__":
	main()
