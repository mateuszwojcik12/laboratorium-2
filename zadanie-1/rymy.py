#!/usr/bin/python3

import collections
import re
import sys

# (?:...) oznacza grupę, której nie zostanie nadany numer.
SPÓŁGŁOSKA = '(?:ch|cz|dz|dź|dż|rz|sz|[^aęeęioóuy])'
SAMOGŁOSKA = '[aąeęioóuy]'

# Wewnątrz tzw. f-napisów można używać wyrażeń w nawiasach klamrowych.
# Zostaną one zastąpione przez wartości tych wyrażeń.
RYM_ŻEŃSKI = re.compile(
        f'.*({SAMOGŁOSKA}{SPÓŁGŁOSKA}+(i)?{SAMOGŁOSKA}+{SPÓŁGŁOSKA}*)$')

# test
def main():
    licznik_wyrazów = 0
    licznik_rymów = collections.Counter()
    nazwa_pliku = "test_rymy.txt"
    with open(nazwa_pliku, 'rt', encoding="utf-8") as plik:
        print('open')
        for wyraz in plik:
            # Usuń końcowy znak nowego wiersza.
            wyraz = wyraz.strip()
            wyraz = wyraz.split(";")[0]
            m = RYM_ŻEŃSKI.match(wyraz)
            if m:
                 licznik_wyrazów += 1
                 licznik_rymów[m.group(1)] += 1
        for rym, ile_razy in licznik_rymów.most_common(25):
            # :5.2f oznacza "typ float, 5 znaków, 2 cyfry po przecinku".
            print(f'{100*ile_razy/licznik_wyrazów:5.2f}% -{rym}')


if __name__ == '__main__':
    main()
