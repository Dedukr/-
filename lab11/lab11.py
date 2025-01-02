import csv
def main():
	def Open(name,mode):
		try:
			return open(name,mode,encoding="utf-8")
		except:
			print(f"There was an error while opening file {name}")
			return None

	def printf(file):
		for row in file:
			print(row)

	def search_more(file, value):
		for row in file:
			if not row[0]=="GDP per capita (current US$)":
				continue
			if row[4]==".." or float(row[4])>=value:
				print(row)


	file=Open("P_Popular_Indicators/Metadata.csv","r")
	file = csv.reader(file)

	printf(file)
	print()
	min_value=float(input("Enter the value:\n"))
	search_more(file, min_value)


if __name__ == "__main__":
	main()
