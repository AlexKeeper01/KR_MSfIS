import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.log(x) + 2 * math.sin(x)

def df(x):
    return 1/x + 2 * math.cos(x)

def search(a, b, eps):
    iteration = 1

    while True:
        x_mid = (a + b) / 2
        f_mid = f(x_mid)
        df_mid = df(x_mid)

        print(f"Итерация {iteration}:")
        print(f"a = {a:.4f}, b = {b:.4f}")
        print(f"x_mid = {x_mid:.4f}, f(x_mid) = {f_mid:.4f}, f'(x_mid) = {df_mid:.4f}")
        print("-" * 40)

        if abs(df_mid) < eps:
            break

        if df_mid > 0:
            b = x_mid
        else:
            a = x_mid

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
plt.plot(x_vals, y_vals, label="f (x)", color="green")
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.scatter(xmin, fmin, color='green')
plt.text(xmin + 0.1, fmin, f"({xmin:.2f}, {fmin:.2f})", color='red', fontsize=12)

plt.axvline(x=xmin, linestyle="--", color='green')
plt.axhline(y=fmin, linestyle="--", color='green')

plt.title("Метод средней точки")
plt.xlabel("x")
plt.ylabel("f (x)")
plt.legend()
plt.grid()
plt.show()
