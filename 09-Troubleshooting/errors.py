
# print('Questo è un errore di sintassi perchè l'apostrofo spezza la stringa')

x = 2
y = 0
result = x / y

try:
    result = x / y
    print(result)
except ZeroDivisionError:
    print("\nNon puoi dividere un numero per zero")

print('Continua con il resto del codice...\n')


print("#######################################################")


try:
    result = x / y
except ZeroDivisionError:
    print("\nNon puoi dividere un numero per zero")
else:
    print(result)
finally:
    print('La sezione finally viene sempre eseguita.')

print('Continua con il resto del codice...\n')
