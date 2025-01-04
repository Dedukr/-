def find_words(sentence, letter):
	arr = sentence.lower().split()

	for word in arr:
		if word[0] == letter.lower():
			print(word)

def main():
	test = "Програмування - це не лише мистецтво створення нового коду, який необхідно налагоджувати."
	letter = "Н"
	find_words(test, letter)


if __name__ == '__main__':
	main()
