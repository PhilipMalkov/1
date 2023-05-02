import numpy as np
import matplotlib.pyplot as plt
import math
#определение функции s(k), которая создает сигнал из случайных чисел
def s(k):
    length = k.shape[0] # длина массива k
    randoms = np.random.random((length)) # создание случайных чисел
    signal = (k > randoms).astype(float) # создание сигнала на основе сравнения k и randoms
    return signal
#Гаусовский шум
def n(k):
    length = k.shape[0]  # длина массива k
    u, o = 0, 0.05
    noise = np.random.normal(u, o, size=length)
    return noise
#Вычислить для сигналов f(k) и d(k) значения SNR и CV

def signaltonoise(a, ddof=0):
    u = a.mean()
    o = a.std(ddof=ddof)

    return u/o
def coefficient_variation(a, ddof=0):
    u = a.mean()
    o = a.std(ddof=ddof)

    return o/u * 100

#создание массива k, который начинается с -1 и заканчивается на 1, включая 100 равных промежутков
k = np.linspace(-1, 1, 100)
#Добавить к сигналу некоторое постоянное значение a=const:
a = 0.2
#Создание графиков
fig, ax = plt.subplots(figsize=(16, 9)) # создание контейнера для графика с определенным размером
S = s(k)
ax.plot(k, S, label='s(k)') # добавление графика для сигнала s(k)
D = S+(n(k))
ax.plot(k, D, label='s(k)+n(k)')
F = D+a
ax.plot(k, F, label='s(k)+n(k)+a')
ax.set_xlabel('k') # добавление подписи для оси x
ax.set_ylabel('v') # добавление подписи для оси y
ax.set_title('Константа шум s(k)') # добавление заголовка графика
ax.legend();
print(signaltonoise(D))
print(signaltonoise(F))
print(coefficient_variation(D))
print(coefficient_variation(F))
plt.show()

plt.show()

def signaltonoise(a, ddof=0):
    u = a.mean()
    o = a.std(ddof=ddof)

    return u/o
def coefficient_variation(a, ddof=0):
    u = a.mean()
    o = a.std(ddof=ddof)

    return o/u * 100


print(f'SNR(D) = {signaltonoise(D)}')
print(f'SNR(F) = {signaltonoise(F)}')
print(f'CV(D) = {coefficient_variation(D)}')
print(f'CV(F) = {coefficient_variation(F)}')
