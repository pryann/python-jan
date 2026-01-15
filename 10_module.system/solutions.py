# 1. Írj egy függvényt, ami megkérdezi a felhasználótól a születési évét, majd kiszámolja, hogy hány éves az illető az aktuális évben és visszaadja ezt az értéket! A hónappal, nappal nem kell most számolnod! Használd a `datetime` modult. Ha a jelenlegi évszámnál nagyobbat adott meg, akkor a _'Még nem járunk ebben az évben.'_ szöveggel kell a függvénynek visszatérnie.

from datetime import datetime
from list_handling import remove_duplicates, sort_list
import random


def calculate_age():
    birth_year_input = input("Kérem adja meg a születési évét: ")

    if not birth_year_input.isdigit():
        return "Érvénytelen évszám."

    birth_year = int(birth_year_input)
    current_year = datetime.now().year

    if birth_year > current_year:
        return "Még nem járunk ebben az évben."

    return current_year - birth_year


# 2. Készíts egy saját modul `list_handling` névvel!
#    A modulon belül két függvény legyen.
#    Az egyik függvény egy paraméterként kapott lista elemeiből eltávolítja a duplikációkat, és visszaadja ezt a listát, a másik a lista elemeit növekvő sorrendbe rendezi.


def handle_lists():
    sample_list = [5, 2, 3, 2, 4, 5, 1, 3]

    no_duplicates = remove_duplicates(sample_list)
    print("Duplikációk eltávolítva:", no_duplicates)

    sorted_list = sort_list(sample_list)
    print("Rendezett lista:", sorted_list)


# 3. Írj egy függvényt, ami bekér a felhasználótól egy egész számot. Ez a 6 oldalú dobókockák darabszáma lesz, amikkel dobni kell. Szimuláld le a kockadobást. Amennyiben bármelyik kockával a dobás értéke 6, azzal a kockával újra lehet dobni. Ez az újra dobás addig ismételhető, amíg a dobott érték 6, tehát nem csak egyszer Add össze a dobások eredményét, add vissza az értéket!


def roll_dice():
    dice_count_input = input("Hány darab 6 oldalú kockával szeretnél dobni? ")

    if not dice_count_input.isdigit():
        return "Érvénytelen szám."

    dice_count = int(dice_count_input)
    total_score = 0

    for _ in range(dice_count):
        roll = random.randint(1, 6)
        total_score += roll

        while roll == 6:
            # can you remove this duplication
            roll = random.randint(1, 6)
            total_score += roll

    return total_score
