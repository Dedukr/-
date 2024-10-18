def find_duplicates(word):
	word = word.lower()
	duplicate_letters = {}

	for letter in set(word):
		if word.count(letter) > 1:
			duplicate_letters[letter]=word.count(letter)

	for l, n in duplicate_letters.items():
		print(f"{l} - {n}")

def main():
	test="Antananarivo"

	find_duplicates(test)


if __name__ == '__main__':
	main()
