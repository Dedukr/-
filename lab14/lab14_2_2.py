import csv
import matplotlib.pyplot as plt


def main():
	def Open(name, mode):
		try:
			return open(name, mode, encoding="ISO-8859-1")
		except:
			print(f"There was an error while opening file {name}")
			return None

	def get_values(data):
		data = list(data)
		years = list(map(lambda x: x[:4], data[0][4:]))
		countries = {"Years": years}
		for i in range(1, len(data) - 5):
			if not data[i][0] in countries:
				countries[data[i][0]] = list(map(lambda x: round(float(x), 3) if not x == ".." else None, data[i][4:]))
		return countries

	file = Open("DataBase2/Data.csv", "r")
	file = csv.reader(file)
	analysed = get_values(file)

	years = analysed.get("Years")

	while True:
		country = input("What country you want to look at?\n")
		data = analysed.get(country.title(), False)
		if not data:
			print("Not valid country. Check the spelling")
			continue
		if None in data:
			print("Unfortunately, we dont have records about this country. Try other")
			continue
		break

	plt.figure(figsize=(12, 8))
	plt.title("Self-employed to total employment, %", fontsize=15)
	plt.bar(years, data, label=country.title())

	buffer = 1
	minlimit = round(min(data) - buffer)
	maxlimit = round(max(data) + buffer)

	plt.ylim(minlimit, maxlimit)
	yticks = list(range(minlimit, maxlimit))

	plt.yticks(yticks, [f"{x}%" for x in yticks])

	plt.grid()
	plt.legend()
	plt.show()


if __name__ == "__main__":
	main()
