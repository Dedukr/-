import pandas as pd
import matplotlib.pyplot as plt
import calendar as cal


def main():
	# Завантаження даних з CSV
	file_path = "bike_data_2018.csv"  # Вкажіть шлях до вашого файлу
	df = pd.read_csv(file_path)

	# Перетворення стовпця 'Date' у формат дати
	df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")

	# Додамо новий стовпець для місяця
	df["Month"] = df["Date"].dt.month
	# Підрахунок загальної кількості велосипедистів для кожного місяця
	monthly_usage = df.groupby("Month").sum(numeric_only=True)

	print("\nВикористання велодоріжок за місяцями:")
	print(monthly_usage)

	# Визначення місяця з найбільшою активністю
	most_popular_month = monthly_usage.sum(axis=1).idxmax()
	print(f"\nНайбільш популярний місяць: {cal.month_name[most_popular_month]}")

	# Візуалізація використання за місяцями
	plt.figure(figsize=(10, 6))
	plt.plot(monthly_usage.index, monthly_usage.sum(axis=1), marker="o", label="Загальна активність")
	plt.title("Використання велодоріжок за місяцями (2018)")
	plt.xlabel("Місяць")
	plt.ylabel("Кількість велосипедистів")
	plt.xticks(range(1, 13))  # Мітки місяців
	plt.grid()
	plt.legend()
	plt.show()


if __name__ == '__main__':
	main()
