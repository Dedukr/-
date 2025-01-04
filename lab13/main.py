import csv, json


def ruslankonoz():
	def Open(name, mode):
		try:
			return open(name, mode, encoding="utf-8", newline=" ")
		except:
			print(f"There was an error while opening file {name}")
			return None

	def read_json(file):
		data = json.load(file)
		file.close()
		return data

	def write_json(file, text):
		json.dump(text, file, indent=4)
		file.close()

	def read_csv(file):
		reader = csv.DictReader(file)
		data = [row for row in reader]
		print(data)
		file.close()
		return data

	def write_csv(file, text):
		writer = csv.DictWriter(file)
		writer.writerows(text)
		file.close()

	def csv_to_json(filename):
		filename += ".csv"
		data = read_csv(Open(filename, "r"))
		write_json(Open(filename.replace("csv", "json"), "w"), data)

	def json_to_csv(filename):
		filename += ".json"
		data = read_json(Open(filename, "r"))
		headers = data[0].keys()
		write_csv(Open(filename.replace(".json", "2.csv"), "w"), data)

	def write_first(filename):
		headers = input("Write headers:\n").split(",")
		text = input("Write the first record\n").split(",")
		file = Open(filename, "w")
		writer = csv.DictWriter(file, fieldnames=headers)
		writer.writeheader()
		dictionary=dict(zip(headers,text))
		print(dictionary)
		writer.writerows(dictionary)
		file.close()

	def write_smth(filename):
		text = input("Write the first record\n").split(",")
		while True:
			format = input("Where do you want to write\n1. CSV\n JSON\n(Enter the number)\n")
			match format:
				case 1:
					text = input("What do you want to write:\n")
					write_json(Open(filename + ".csv", "a"), text)
				case 2:
					text = input("What do you want to write:\n")
					write_json(Open(filename + ".json", "a"), text)

	path = "forum"

	while True:
		ans = int(input(
			"\nWhat do you want to do?\n1. Write the first record\n2. Write some records\n3. Convert csv to json\n4. Convert json to csv\n4. Exit\n(Enter the number)\n"))
		match ans:
			case 1:
				write_first(path)
			case 2:
				write_smth(path)
			case 3:
				csv_to_json(path)
			case 4:
				json_to_csv(path)
			case 5:
				break
			case _:
				print("Enter the correct number")
				continue
	write_smth(path + ".csv")


# csv_to_json(path)
# json_to_csv(path)


if __name__ == '__main__':
	ruslankonoz()
