"""
W tym zadaniu zbudujesz proces służący do budowy łańcucha transformacji danych liczbowych.
1. Utwórz w swoim skrypcie następujące funkcje:
    def double(x):
        return 2 *x
    def root(x):
        return x**2
    def negative(x):
        return -x
    def div2(x):
        return x/2

2. Zdefiniuj liczbę number o wartości 8
3. Zdefiniuj listę transformations składającą sie z funkcji:
    - double
    - root
    - div2
    - negative
4. Do tymczasowej zmiennej tmp_return_value wpisz wartość number
5. Napisz pętlę, która:
    - przejdzie przez wszystkie pozycje listy transformations
    - za każdym razem wywoła odpowiednią funkcję, przekazując do niej aktualną wartość argumentu tmp_return_value
    - wyświetli aktualną wartość zmiennej tmp_return_value
6. Przetestuj działanie skryptu również dla listy transformacji z operacjami:
    - root
    - root
    - div2
    - double
"""

def double(x):
    return 2*x

def root(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x/2

number = 8
transformations = [double, root, div2, negative]

tmp_retun_value = number

for transf in transformations:
    print(transf(tmp_retun_value))

print()
number=10
tmp_retun_value = number
list=[root,root,div2, double]

for transf in list:
    print(transf(tmp_retun_value))