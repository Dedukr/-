import pandas as pd


def main():
	def agregation(df):
		average_scores = df.groupby("Subject")["Score"].mean()
		print("\nСередній бал по предмету:")
		print(average_scores)

	def grouping(df):
		total_scores = df.groupby("Name")["Score"].sum()
		print("\nЗагальна сума балів по студентам:")
		print(total_scores)

	data = {
		"Name": ["Volodymyr", "Eugen", "Ruslan", "Volodymyr", "Ruslan"],
		"Subject": ["Math", "Math", "Science", "Science", "Math"],
		"Score": [85, 78, 92, 88, 95]
	}

	df = pd.DataFrame(data)
	print(df)

	agregation(df)

	grouping(df)


if __name__ == "__main__":
	main()
