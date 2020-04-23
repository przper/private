"""
Piszesz program, który będzie obsługiwał wpłatomat.
To będzie super nowoczesny wpłatomat, do którego można też wpłacać monety.
Ilekroć ktoś wpłaca pieniądze należy policzyć ile banknotów
lub monet danego nominału znajduje się w kasie.

Zacznij od poniższej listy, która definiuje dostępne nominałyL

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

Dowolną metodą utwórz słownik, który jako klucz będzie przechowywał wartość nominału,
a jeśli chodzi o wartości słownika, to póki co mają być zerowe.
Proponuję nazwać ten słownik dict_denominations.

Teraz do bankomatu podchodzą klienci i wpłacają:

    dict_denominations[100] += 1
    dict_denominations[20] += 1
    dict_denominations[5] += 1
    dict_denominations[0.5] += 1

    dict_denominations[50] += 1
    dict_denominations[20] += 2
    dict_denominations[5] += 1
    dict_denominations[2] += 2

    dict_denominations[100] += 1
    dict_denominations[50] += 1
    dict_denominations[2] += 1

Napisz polecenie for, które wyświetli ile mamy pieniędzy w określonych
monetach lub banknotach. Zestawienie ma zacząć sie od najmniejszych nominałów,
a skończyć na największych. Jeśli masz ochotę, to zadbaj o ładne formatowanie wyniku:

-nominał na 6 znakach, w tym 2 po przecinku

-ilość monet/banknotów - liczba całkowita maksymalnie 5-cyfrowa

możesz skorzystać z artykułu: https://www.python-course.eu/python3_formatted_output.php
(skocz do części dot. polecenia format - jeśli link nie byłby
aktualny daj znać w Q&A - z góry dzięki!)
"""

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
dict_denominations = {}

for i in banknotes_coins: #i jest wartością kolejnych komórek listy
    #print(i)
    dict_denominations[i] = 0

#wpłaty banknotów:
dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1


for d in dict_denominations: #iteruje po keys słownika (0.01, 0.02, itd)
    if dict_denominations[d]!=0: #jeśli value dla danego key jest !=0
        print('Nominał "{0:6.2f}" znajduje się {1:5} raz(y) we wpłatomacie'.format(d,dict_denominations[d]))
    else:
        pass

