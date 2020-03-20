#!/usr/bin/python3

import collections
import readline
import sqlite3

import normalizacja
import utils


Zapytanie = collections.namedtuple('Zapytanie', 'kolumny tekst_warunku')


# TU(1): Uzupełnić synonimy.
SYNONIMY = {
    'doktor': 'dr',
    'habilitowan': 'hab',
}

PRACOWNIK = 'pracownik'
JEDNOSTKA = 'jednostka'
TELEFON = 'telefon'
EMAIL = 'email'

# TU(2): Uzupełnić synonimy.
KOLUMNY = {
    'gd': JEDNOSTKA,
    'jednostk': JEDNOSTKA,
    'katedr': JEDNOSTKA,
    'numer': TELEFON,
    'telefon': TELEFON,
}

ZNACZĄCE_WYRAZY = set()
connection = sqlite3.connect(utils.BAZA_DANYCH)
for wiersz in connection.execute('SELECT * FROM PracownicyFTS'):
    for pole in wiersz:
        ZNACZĄCE_WYRAZY.update(pole.split())


def przetwórz_pytanie(pytanie):
    """Zwraca `Zapytanie`, którego pola są wypełnione zgodnie z `pytanie`.

    >>> przetwórz_pytanie('Gdzie pracuje Jerzy?')
    Zapytanie(kolumny={'pracownik', 'jednostka'}, tekst_warunku='jer OR jerz')
    """
    kolumny = {PRACOWNIK}
    warunek = []
    for fragment in utils.podziel_i_odetnij_końcówki(pytanie):
        w = []
        for element in fragment:
            if element in SYNONIMY:
                warunek.append(SYNONIMY[element])
            elif element in KOLUMNY:
                kolumny.add(KOLUMNY[element])
            elif element in ZNACZĄCE_WYRAZY:
                w.append(element)
        if w:
            warunek.append(' OR '.join(w))
    return Zapytanie(kolumny=kolumny, tekst_warunku=' '.join(warunek))


def odpowiedz(zapytanie):
    """Odpowiada na dane `zapytanie`."""

    # TU(3): Uzupełnić funkcję.
    zapytanie_sql = f"""
        """


def main():
    while True:
        pytanie = input('> ')
        if not pytanie:
            break
        pytanie = normalizacja.normalizuj_kody_jednostek(pytanie)
        pytanie = normalizacja.normalizuj_numery_telefonów(pytanie)
        zapytanie = przetwórz_pytanie(pytanie)
        odpowiedz(zapytanie)


if __name__ == '__main__':
    main()
