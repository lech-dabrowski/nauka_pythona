Większość jest oczywista. ** podnosi do potęgi, // i % to dzielenie z resztą no a ** 0,5 to fajny sposób na wyciągnięcie pierwiastka

```python
x = input('podaj pierwszą liczbę: ')
y = input('podaj drugą liczbę: ')
result1 = int(x) + int(y)
result2 = int(x) - int(y)
result3 = int(x) * int(y)
result4 = int(x) / int(y)
result5 = int(x) ** int(y)
result6 = int(x) // int(y)
result7 = int(x) % int(y)
print('suma obu liczb to', result1)
print('różnica obu liczb to', result2)
print('iloczyn obu liczb to', result3)
print('iloraz x przez y to', result4)
print('x do potęgi y to', result5)
print('y mieści się w x tyle razy:', result6)
print('i tyle reszty: ', result7)
print('i jako ciekawostkę dodam, że pierwiastek kwadratowy z pierwszej liczby wynosi:')
print(int(x)**0.5)
print('natomiast pierwiastek kwadratowy z drugiej liczby to:')
print(int(y)**0.5)
```
