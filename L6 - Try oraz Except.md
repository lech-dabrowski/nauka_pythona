```python
liczba = input("podaj jakiś numerek ")
try:
    ival = int(liczba)
except:
    ival = -1
if ival > 0:
    print("dobrze")
else:
    print("zjebałeś")
```

TRY sprawia, że kompilator SPRBÓJE odpalić daną linię i w sytuacji, gdyby zakończyło się to błędem, ignoruje ją i zamiast tego odpala to, co jest pod EXCEPT.

Jest to prosty sposób przygotowania się na błędy użytkownika. W tym wypadku jeżeli użytkownik proszony o liczbę (np. INT) poda coś innego (np. STRING) linijka: ival = int(liczba) zakończyłaby się błedem. Jeżeli to się zadzieje, zadziała EXCEPT, który zmieni wartość zmiennej IVAL na -1


