#################### import ######################

from colortext import colortext

def ordinare_pizza(size):
    print(colortext(f'Ordinata una pizza {size}.', 'red'))

ordinare_pizza("large")


#################### *args ######################


def ordinare_pizza(size, ingrediente1, ingrediente2):
    print(colortext(f'Ordinata una pizza {size} con i seguenti ingredienti: {ingrediente1}, {ingrediente2}.', 'red'))

ordinare_pizza("large", "salsiccia", 'peperoni')


def ordinare_pizza(size, *ingredienti):
    print(colortext(f'Ordinata una pizza {size} con i seguenti ingredienti:', 'red'))
    for ingrediente in ingredienti:
        print(f'- {ingrediente}')

ordinare_pizza("large", "tonno", "cipolla", "olive")


#################### *kwargs ######################


def ordinare_pizza(size, *ingredienti, **dettagli_ordine):
    print(colortext(f"\nOrdinata una pizza {size} con i seguenti ingredienti:", "red"))
    for ingrediente in ingredienti:
        print(f'- {ingrediente}')
    print(colortext("\nI dettagli dell'ordine sono:", "blue"))
    for key, value in dettagli_ordine.items():
        print(f"- {key}: {value}")

ordinare_pizza("large", "tonno", "cipolla", "olive", takeaway="si", mancia="5€")
