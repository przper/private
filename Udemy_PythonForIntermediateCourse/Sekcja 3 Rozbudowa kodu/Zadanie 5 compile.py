"""
Nadal pracujemy w zwariowanym ośrodku badawczym.
Ponieważ profesorowie mieli problem z umieszczaniem
swoich skryptów w odpowiednich katalogach, od tej pory
dostarczają tylko wzory, które podlegają przeliczeniom.
W tym zadaniu wielokrotnie wyliczysz wartości wyliczane wzorami,
a następnie porównasz czasy wykonania w zależności
od sposobu interpretacji kodu.

1. Zaimportuj moduł math i time
2. Utwórz listę ze wzorami:
    formulas_list = [
         "abs(x**3 - x**0.5)",
         "abs(math.sin(x) * x**2)"
         ]
3. Przygotuj listę argumentów (jeżeli pętla trwa zbyt długo zmniejsz ilość elementów na tej liście):
    argument_list = []
    for i in range (1000000):
        argument_list.append(i/10)
        i += 1
3. Dla każdej formuły z listy formuł:
    - Utwórz pustą listę results_list = []
    - Wyświetl formułę nad jaką teraz pracuje pętla
    - W zmiennej start zapisz czas bieżący
    - Dla każdego argumentu z listy argument_list wylicz wartość formuły i dodaj go do listy wyników results_list
    - Wyświetl informację o minimalnej i maksymalnej wyliczonej wartości znajdującej się w liście results list
    - W zmiennej stop zapisz czas bieżący
    - Wyświetl informacje o czasie trwania obliczeń
4. Przetestuj skrypt
5. Skopiuj pętlę z punktu (3) i dokonaj modyfikacji:
    - Przed pętlą liczącą wartość formuły wstaw instrukcję zapamiętującą w zmiennej compiled_formula skompilowany kod
    - W pętli liczącej wartość formuły skorzystaj z prekompilowanego kodu ze zmiennej compiled_formula
6. Uruchom program i porównaj czasy przed i po optymalizacji
"""
import math
import time

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]
argument_list = []
for i in range (1000000):
    argument_list.append(i/10)
    i += 1 #niepotrzebne
#print(argument_list)

for formula in formulas_list:
    #print(formula)
    results_list=[]
    #print(results_list)
    print("Formula: ",formula)
    start = time.time()
    for x in argument_list:
        #print(x)
        #print(eval(formula))
        results_list.append(eval(formula))
    #print(results_list)
    print("Min: {0:3.1f}, Max: {1:6.2f}".format(min(results_list), max(results_list)))
    stop = time.time()
    print("Calculations time:",(stop-start))

"""
5. Skopiuj pętlę z punktu (3) i dokonaj modyfikacji:
    - Przed pętlą liczącą wartość formuły wstaw instrukcję zapamiętującą w zmiennej compiled_formula skompilowany kod
    - W pętli liczącej wartość formuły skorzystaj z prekompilowanego kodu ze zmiennej compiled_formula
6. Uruchom program i porównaj czasy przed i po optymalizacji
"""


for formula in formulas_list:
    results_list=[]
    print("Formula: ",formula)
    start = time.time()

    compiled_formula = compile(formula,formula,'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print("Min: {0:3.1f}, Max: {1:6.2f}".format(min(results_list), max(results_list)))
    stop = time.time()
    print("Calculations time:",(stop-start))
