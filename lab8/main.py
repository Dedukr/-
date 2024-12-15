def ruslankonoz():
	from config import TEXT
	# lowercase the sentence
	TEXT = TEXT.lower()

	# replace a letter "a" with @
	TEXT = TEXT.replace("а", "@")

	# split the TEXT by separator @
	TEXT = TEXT.split("@")

	var = "{There was a}"

	# join the string with "{0}" as joiner"
	TEXT = "{0}".join(TEXT)

	# format the TEXT substituting the "var" into the sentence
	TEXT = TEXT.format(var)

	# make all first letters capital
	TEXT = TEXT.title()

	print(TEXT)


if __name__ == '__main__':
	ruslankonoz()
