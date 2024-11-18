# Функція для введення матриці
def input_matrix():
    print("Enter size of matrix: > ", end="")     # Введіть розмір матриці
    n, m = map(int, input().split())
    print("Enter matrix:")
    matrix = []
    for _ in range(n):
        row = list(map(float, input("> ").split()))
        matrix.append(row)
    return matrix, n, m


# Функція для додавання матриць
def add_matrices(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result


# Функція для множення матриці на константу
def scale_matrix(matrix, scalar):
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element * scalar)
        result.append(new_row)
    return result


# Функція для множення двох матриць
def multiply_matrices(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            s = 0
            for k in range(len(matrix_b)):
                s += matrix_a[i][k] * matrix_b[k][j]
            row.append(s)
        result.append(row)
    return result


# Функції для транспонування матриці
def transpose_main_diagonal(matrix):
    n, m = len(matrix), len(matrix[0])                   # Транспонування основної діагоналі
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    return result


def transpose_side_diagonal(matrix):
    n, m = len(matrix), len(matrix[0])                 # Транспонувати бічну діагональ
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - j - 1][n - i - 1] = matrix[i][j]
    return result


def transpose_vertical(matrix):
    return [row[::-1] for row in matrix]             # Транспонувати вертикально


def transpose_horizontal(matrix):
    return matrix[::-1]                                                  # Транспонувати горизонтально


# Функція для обчислення визначника
def calculate_determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for col in range(n):
        # Побудова мінору
        minor = []
        for row in range(1, n):
            minor_row = matrix[row][:col] + matrix[row][col + 1:]
            minor.append(minor_row)
        # Рекурсивний виклик
        determinant += ((-1) ** col) * matrix[0][col] * calculate_determinant(minor)
    return determinant


# Функція для знаходження зворотної матриці
def inverse_matrix(matrix):
    n = len(matrix)
    determinant = calculate_determinant(matrix)

    if determinant == 0:
        return None

    # Побудова матриці алгебраїчних доповнень
    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            # Мінор для елемента
            minor = []
            for row in range(n):
                if row != i:
                    minor_row = matrix[row][:j] + matrix[row][j + 1:]
                    minor.append(minor_row)
            cofactor = ((-1) ** (i + j)) * calculate_determinant(minor)
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)

    # Транспонування матриці алгебраїчних доповнень
    cofactors = transpose_main_diagonal(cofactors)

    # Ділення кожного елемента на визначник
    for i in range(n):
        for j in range(n):
            cofactors[i][j] /= determinant

    return cofactors


# Функція для друку матриці
def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        print(" ".join(f"{x:.2f}" for x in row))


# Основна програма
def main():
    while True:
        # Виведення меню
        print("\n1. Add matrices")                        # Додайте матриці
        print("2. Multiply matrix by a constant")         # Помножити матрицю на константу
        print("3. Multiply matrices")                     # Множення матриць
        print("4. Transpose matrix")                      # Транспонувати матрицю
        print("5. Calculate a determinant")               # Обчисліть визначник
        print("6. Inverse matrix")                        # Обернена матриця
        print("0. Exit")                                  # Вихід
        print("Your choice: > ", end="")
        choice = input().strip()

        if choice == "1":
            # Додавання матриць
            matrix_a, n_a, m_a = input_matrix()
            matrix_b, n_b, m_b = input_matrix()
            if n_a == n_b and m_a == m_b:
                result = add_matrices(matrix_a, matrix_b)
                print_matrix(result)
            else:
                print("The operation cannot be performed.")

        elif choice == "2":
            # Множення матриці на константу
            matrix, _, _ = input_matrix()
            print("Enter constant: > ", end="")
            scalar = float(input())
            result = scale_matrix(matrix, scalar)
            print_matrix(result)

        elif choice == "3":
            # Множення матриць
            matrix_a, n_a, m_a = input_matrix()
            matrix_b, n_b, m_b = input_matrix()
            if m_a == n_b:
                result = multiply_matrices(matrix_a, matrix_b)
                print_matrix(result)
            else:
                print("The operation cannot be performed.")

        elif choice == "4":
            # Транспонування матриці
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            print("Your choice: > ", end="")
            transpose_choice = input().strip()

            matrix, _, _ = input_matrix()

            if transpose_choice == "1":
                result = transpose_main_diagonal(matrix)
            elif transpose_choice == "2":
                result = transpose_side_diagonal(matrix)
            elif transpose_choice == "3":
                result = transpose_vertical(matrix)
            elif transpose_choice == "4":
                result = transpose_horizontal(matrix)
            else:
                print("Invalid choice.")
                continue

            print_matrix(result)

        elif choice == "5":
            # Обчислення визначника
            matrix, n, m = input_matrix()
            if n != m:
                print("The operation cannot be performed. Matrix must be square.")      # Операція не може бути виконана. Матриця має бути квадратною
            else:
                result = calculate_determinant(matrix)
                print("The result is:")
                print(result)

        elif choice == "6":
            # Знаходження зворотної матриці
            matrix, n, m = input_matrix()
            if n != m:
                print("The operation cannot be performed. Matrix must be square.")
            else:
                result = inverse_matrix(matrix)
                if result is None:
                    print("This matrix doesn't have an inverse.")            # Ця матриця не має оберненої матриці
                else:
                    print_matrix(result)

        elif choice == "0":
            # Вихід
            print("Goodbye!")  # пока
            break

        else:
            print("Invalid choice. Try again.")


# Виконання програми
main()
