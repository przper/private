"""
Piszesz funkcję log_it, która ma zapisać w pliku tekstowym
np. c:\temp\log_it.txt przesłane do funkcji argumenty.
Funkcja będzie wykorzystywana w innych miejscach programu,
gdzie będzie wywoływana w strategicznych momentach, dokumentując
działanie programu. Jeśli nie masz innych pomysłów to zadbaj o to aby:
    - można było przesłać dowolną ilość argumentów
    - podczas dopisywania informacji do pliku poszczególne argumenty rozdzielaj spacją
    - na końcu w pliku zapisz ENTER, aby kolejne wywołanie funkcji dopisywało od nowej linijki

Przetestuj działanie funkcji wywołując ją np w taki sposób:
    log_it('Starting processing forecasting')
    log_it('ERROR', 'Not enough data', 'invoices', '2020')
"""

path = r'C:\Users\Admin\Desktop\Python\Udemy\Python dla średnio zaawansowanych\Sekcja 4 Funkcje\Zadanie 2.2 log.txt'


def log_it(*args):
    with open(path, 'a') as f:
        for line in args:
            f.write(line)
            f.write(' ')
        f.write("\n")

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')