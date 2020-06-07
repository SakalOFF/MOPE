import random


def print_array(array, form=False):
    for element in array:
        print('\t', end='')
        for x in element:
            if form:
                print('{:^8.3}'.format(x), end='')
            else:
                print('{:^4}'.format(x), end='')
        print('\n')


def x_0(array):
    return (max(array) + min(array)) / 2


def dx(array):
    return x_0(array) - min(array)


def xn(array, el):
    return (el - x_0(array)) / dx(array)


a = [1, 2, 3, 4]
X = [[random.randrange(1, 21, 1) for _ in range(8)] for _ in range(3)]
y = [a[0] + a[1] * X[0][i] + a[2] * X[1][i] + a[3] * X[2][i] for i in range(8)]


print("\nЗначення факторів у точках експерименту:\n")
print_array(X)

print('Значення функції відгуку:\n')
for i in y:
    print(i, end=' ')
print('\n')


average_y = sum(y)/len(y)
y_etalon = a[0] + a[1] * x_0(X[0]) + a[2] * x_0(X[1]) + a[3] * x_0(X[2])


t_p = min(y)
for i in y:
    if t_p < i <= average_y:
        t_p = i

print("\nТочка плану = ", t_p)
print("\nСереднє значення у = ", average_y)

print("\nНормування факторів:\n")
print(f"X(0)1 = {x_0(X[0])}\n"
      f"dx1 = {dx(X[0])}\n"
      f"X(0)2 = {x_0(X[1])}\n"
      f"dx2 = {dx(X[1])}\n"
      f"X(0)3 = {x_0(X[2])}\n"
      f"dx3 = {dx(X[2])}\n")
print(f"Y(et) = {y_etalon}\n")

Xn = [[] for _ in range(3)]
for i in range(3):
    for x in X[i]:
        Xn[i].append(xn(X[i], x))

print("Значення віднормованих факторів:\n")
print_array(Xn, True)

y_norm = [a[0] + a[1] * Xn[0][i] + a[2] * Xn[1][i] + a[3] * Xn[2][i] for i in range(8)]
print("Функція відгуку віднормованих факторів:")
for i in y_norm:
    print(f"{i:^8.3f}", end=" ")
