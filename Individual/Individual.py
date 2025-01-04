import numpy as np


def main():
	# Введення даних
	print("Введіть матрицю A (у вигляді рядків через кому, наприклад: 1 2, 3 4):")
	A = np.array([list(map(float, row.split())) for row in input().split(",")])

	print("Введіть вектор b (у вигляді чисел через пробіл, наприклад: 5 6):")
	b = np.array(list(map(float, input().split())))

	# Перевірка, чи квадратна матриця
	is_square = A.shape[0] == A.shape[1]
	if not is_square:
		print("Матриця A не є квадратною. Система рівнянь не може бути вирішена.")
		exit()

	# Обчислення визначника
	det_A = np.linalg.det(A)
	if det_A == 0:
		print("Матриця вироджена, система не має єдиного розв’язку.")
	else:
		# Розв’язання системи рівнянь
		x = np.linalg.solve(A, b)
		print("Розв’язок системи рівнянь (x):")
		print(x)

		# Перевірка точності розв’язку
		Ax = np.dot(A, x)
		if np.allclose(Ax, b):
			print("Розв’язок перевірено: Ax ≈ b")
		else:
			print("Розв’язок неточний.")


if __name__ == '__main__':
	main()
