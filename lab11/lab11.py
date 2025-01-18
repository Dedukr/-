import csv


def main():
	def Open(name, mode):
		try:
			return open(name, mode, encoding="utf-8")
		except:
			print(f"There was an error while opening file {name}")
			return None

	def printf(file):
		reader = csv.reader(file)
		for row in reader:
			if row[0] == "":
				return
			print(row)
		file.close()

	def search_more(file, value):
		reader = csv.reader(file)
		answer=[]
		for row in reader:
			if not row[0] == "GDP per capita (current US$)":
				continue
			if row[4] != ".." and float(row[4]) >= value:
				answer.append(row)
		file.close()
		return answer


	def writef(file, text):
		writer = csv.writer(file)
		writer.writerows(text)
		file.close()

	path="P_Popular_Indicators/Data.csv"

	printf(Open(path, "r"))

	min_value = float(input("\nEnter the value which you want to use as minimal GDP per capita (current US$):\n"))
	answer=search_more(Open(path, "r"), min_value)
	writef(Open("Filtered_data.csv", "w"), answer)




if __name__ == "__main__":
	main()
