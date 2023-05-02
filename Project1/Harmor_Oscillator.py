import numpy as np
import matplotlib.pyplot as plt
# Осцилограф
def f(t):
    A, w, u = 1, 2 * np.pi, 0 #задаем амплитуду, угловую частоту и начальную фазу
    length = t.shape[0]
    x = A * np.cos(w * t + u)
    return x
#Добавляем шум
def gaus(t):
    length = t.shape[0]  # длина массива t
    u, o = 0, 0.05
    noise = np.random.normal(u, o, size=length)
    return noise


t= np.linspace(0, 2, 100) #шаг графика
t = np.linspace(0, 2, 100) #шаг графика

#x = A * np.cos(w * t + u) # вычисление координаты для каждого временного отсчета
fig, ax = plt.subplots(figsize=(8, 5))
F = f(t)
ax.plot(t, F, label='F - без шума') # построение графика
G = F+gaus(t)
ax.plot(t, G, label='G - с шумом') # построение графика с добавленым шумом
ax.set_xlabel('Время') # подпись по оси x
ax.set_ylabel('Координата') # подпись по оси y
ax.legend();

#Определяем SNR

def signaltonoise(a, ddof=0):
    u = a.mean()
    o = a.std(ddof=ddof)
    return u/o

print(f'SNR F = {signaltonoise(F)}')
print(f'SNR G = {signaltonoise(G)}')

plt.plot(t, f(t)) # построение графика
plt.plot(t, f(t)+gaus(t)) # построение графика
plt.xlabel('время') # подпись по оси x
plt.ylabel('координата') # подпись по оси y
