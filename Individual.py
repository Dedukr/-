def main():
	import numpy as np


	# Постановка задачі
	# Матриця коефіцієнтів
	A = np.array([[2, 1], [1, 3]], dtype=float)

	# Вектор правих частин
	b = np.array([5, 6], dtype=float)

	# Перевірка визначника
	det_A = np.linalg.det(A)
	if det_A:
		# Розв’язання системи рівнянь
		x = np.linalg.solve(A, b)
		print("Розв’язок системи рівнянь:")
		print(x)
	else:
		print("Система не має єдиного розв’язку, матриця вироджена.")

	# Перевірка правильності
	print("Перевірка: Ax = b")
	print("Обчислене значення b:", np.dot(A, x))


if __name__ == '__main__':
	main()
