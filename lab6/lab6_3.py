def main():
	def count_vowels_and_consonants(text):
		alphabet = set("abcdefghijklmnopqrstuvwxyz")
		vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
		consonants = alphabet - vowels

		vowel_count = 0
		consonant_count = 0

		text = text.lower()

		for char in text:
			if char in vowels:
				vowel_count += 1
			elif char in consonants:
				consonant_count += 1

		return vowel_count, consonant_count

	text = input("Введіть текст з цифр і літер латинського алфавіту:\n")

	vowel_count, consonant_count = count_vowels_and_consonants(text)

	if vowel_count > consonant_count:
		print(f"У тексті більше голосних ({vowel_count}), ніж приголосних ({consonant_count}).")
	elif vowel_count < consonant_count:
		print(f"У тексті більше приголосних ({consonant_count}), ніж голосних ({vowel_count}).")
	else:
		print(f"Кількість голосних і приголосних однакова ({vowel_count}).")


if __name__ == "__main__":
	main()
