```python
def Pozdrowienia(jezyk):
    if jezyk == 'polski':
        return 'Witaj'
    elif jezyk == 'niemiecki':
        return 'Heil Hitler'
    elif jezyk == 'francuski':
        return 'Baguette'
    else:
        return 'Hello'

print(Pozdrowienia('polski'), 'Gamoniu')
print(Pozdrowienia('niemiecki'), 'Schweinhund')
print(Pozdrowienia(input('podaj język ')), 'My Darling')
```

Okazało się, że umieszczanie polecenia PRINT wewnątrz zdefiniowanej funkcji nie nalezy do dobrych praktyk i niepotrzebnie się wtedy rozszalałem. Dużo lepiej jest skorzystać z polecenia RETURN, które ZWRACA wynik do wykorzystania.

```
    if jezyk == 'polski':
        return 'Witaj'
```

To na górze oznacza, że jeżeli parametrem funkcji Pozdrowienia będzie ‘polski’, wtedy cała funkcja da wynik ‘Witaj’, ale nic się nie zadzieje dopóki nie wywołamy funkcji np. poprzez PRINT.
