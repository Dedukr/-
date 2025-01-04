def main():
	def find_subsequence(sequence, subsequence):

		seq_len = len(sequence)
		sub_len = len(subsequence)

		for i in range(seq_len - sub_len + 1):
			if sequence[i:i + sub_len] == subsequence:
				return i

		return -1

	sequence = list(map(int, input('Enter a list:\n').split()))
	subsequence = [3, 4, 5]

	index = find_subsequence(sequence, subsequence)
	if index != -1:
		print(f"Підпослідовність знайдено за індексом {index}.")
	else:
		print("Підпослідовність не знайдено.")


if __name__ == "__main__":
	main()
