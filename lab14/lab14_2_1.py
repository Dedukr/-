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
				countries[data[i][0]] = list(map(lambda x: round(float(x), 3), data[i][4:]))
		return countries

	file = Open("DataBase/Data.csv", "r")
	file = csv.reader(file)
	analysed = get_values(file)

	years, ukraine, uk = analysed.values()

	plt.figure(figsize=(12, 8))
	plt.title("Self-employed to total employment, %", fontsize=15)
	plt.plot(years, ukraine, "b", label="Ukraine")
	plt.plot(years, uk, "r", label="The Uk")
	plt.grid()
	plt.legend()
	plt.show()


if __name__ == "__main__":
	main()
