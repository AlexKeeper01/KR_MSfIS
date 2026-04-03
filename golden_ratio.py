import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return math.log(x) + 2 * math.sin(x)

def search(a, b, eps):
    phi = (math.sqrt(5) - 1) / 2

    x1 = b - phi * (b - a)
    x2 = a + phi * (b - a)

    f1 = f(x1)
    f2 = f(x2)
    iteration = 1

    while abs(b - a) > eps:
        print(f"Итерация {iteration}:")
        print(f"a = {a:.4f}, b = {b:.4f}")
        print(f"x1 = {x1:.4f}, f(x1) = {f1:.4f}")
        print(f"x2 = {x2:.4f}, f(x2) = {f2:.4f}")
        print("-" * 40)
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + phi * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - phi * (b - a)
            f1 = f(x1)

        iteration += 1

    xmin = (a + b) / 2
    return xmin, f(xmin)


a = 2
b = 6
eps = 0.02
xmin, fmin = search(a, b, eps)

print(f"\nx_min ≈ {xmin:.4f}")
print(f"f(x_min) ≈ {fmin:.4f}")

x_vals = np.linspace(0.01, 10, 500)
y_vals = [f(x) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f (x)")
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.scatter(xmin, fmin)

plt.axvline(x=xmin, linestyle="--")
plt.axhline(y=fmin, linestyle="--")
plt.title("Метод золотого сечения")
plt.xlabel("x")
plt.ylabel("f (x)")
plt.legend()
plt.grid()

plt.show()
