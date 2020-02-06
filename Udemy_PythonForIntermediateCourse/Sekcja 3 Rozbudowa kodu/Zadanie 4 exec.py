"""
Tym razem pracujesz w zwariowanym ośrodku badawczym...
Profesorowie przygotowują swoje skrypty i umieszczają je
w określonym katalogu. Twój skrypt ma za zadanie przeczytać
te skrypty i je po kolei wykonywać.

Poniżej znajdują się dwa przykładowe skrypty. Każdy z nich
skopiuj i zapisz w osobnym pliku (jeżeli wykonanie skryptu
miało by być zbyt długie, możesz zmienić ilość iteracji w
zmiennej for, ale nie powinno być tak źle):

#1
    import math

    argument_list = []
    results_list = []

    for i in range (1000000):
        argument_list.append(i/10)
        i += 1

    for x in argument_list:
        results_list.append(abs(math.sin(x) * x**2))

    print('min = {}  max = {}'.format(min(results_list), max(results_list)))

#2
    import math

    argument_list = []
    results_list = []

    for i in range (1000000):
        argument_list.append(i/10)
        i += 1

    for x in argument_list:
        results_list.append(abs(x**3 - x**0.5))

    print('min = {}  max = {}'.format(min(results_list), max(results_list)))

Utwórz listę zawierającą ścieżki dostępu do skryptów:

    files_to_process = [
        r"C:\Python\math_sin_square.py",
        r"C:\Python\math_square_root.py"
        ]

Dla każdego pliku:
    - wyświetl nazwę pliku
    - otwórz dany plik i wczytaj go do zmiennej source
    - Wykonaj ten skrypt
"""
import os

data_dir = r'C:\Users\Admin\Desktop\Python\Udemy\Python dla średnio zaawansowanych\Sekcja 3 Rozbudowa kodu'
files_to_process = [
    r"Zadanie 4.1.py",
    r"Zadanie 4.2.py"
]
"""
MOJE:
for file in files_to_process:
    print(file)
    path = os.path.join(data_dir,file)
    #print(path) #TEST
    exec(open(path, 'r').read())
    open(path, 'r').close()
"""
for file in files_to_process:
    with open(os.path.join(data_dir, file), 'r') as f:
        print("File {} ...".format(file))
        source = f.read()
        exec(source)
