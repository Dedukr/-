import json
import matplotlib.pyplot as plt


def main():
	def Open(name, mode):
		try:
			return open(name, mode, encoding="utf-8")
		except:
			print(f"There was an error while opening file {name}")
			return None

	file = Open("lab12.json", "r")
	data = json.load(file)

	countries = list(data.keys())
	areas = [x[0] for x in data.values()]
	population = [x[1] for x in data.values()]
	explodes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	print(countries)
	print(areas)
	print(population)

	fig, grid = plt.subplots(1, 2, figsize=(12, 8))
	grid[0].pie(areas, labels=countries, autopct="%.2f%%", explode=explodes, pctdistance=0.9)
	grid[0].set_title("Area")
	grid[1].pie(population, labels=countries, autopct="%.2f%%", explode=explodes, pctdistance=0.9)
	grid[1].set_title("Population")
	plt.tight_layout()
	plt.suptitle("Countries comparison")
	plt.show()


if __name__ == "__main__":
	main()
