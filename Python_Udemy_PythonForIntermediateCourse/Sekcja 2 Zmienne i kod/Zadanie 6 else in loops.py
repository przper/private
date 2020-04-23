"""
W tym zadaniu należy zapisać na dysku zawartość kilku stron www.
Po zakończeniu pobierania należy wyświetlić komunikat o powodzeniu.
Jednak w przypadku błędu należy wyświetlić informację o błędzie i przerwać pętlę.
Jeśli taki opis Ci wystarcza - do działa!

A oto opis "krok po kroku"
    zaimportuj moduły os i urllib.request
    w zmiennej data_dir zapisz ścieżkę do katalogu, w którym mają być zapisywane strony
    w zmiennej pages zapisz informacje o stronach do pobrania. Może to być np. LISTA SŁOWNIKÓW:
pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

    dla każdej strony z pages:
        * zapisz w zmiennej path ścieżkę to pliku powstałą z połączenia data_dir,
        nazwy strony pobranej z  pages i ".html"
        * korzystając z  funkcji urllib.request.urlretrieve(<adres strony>, <sciezka do pliku>)
        zapisz stronę na dysku
        * (na tym etapie przetestuj sobie działanie programu)
        * wewnątrz pętli while dodaj blok try/except, który w przypadku błędu zakończy wykonywanie pętli,
        wyświetlając komunikat o błędzie
        *zakończ pętlę while poleceniem, które wykona się tylko wtedy gdy pętla
        nie została w żaden sposób przerwana. Wyświetl tu komunikat o powodzeniu
"""
import os
import urllib.request

data_dir = r'C:\Users\Admin\Desktop\Python\Udemy\Sekcja 2 Zmienne i kod\Zadanie 6'
pages = [ #lista słowników, lol
    {'name':'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name':'GOG','url':'https://www.gog.com/'},
    {'name':'JEBZDZIDY','url':'https://jbzdy.net'}
]

for page in pages: #page to pojedynczy słownik
    try:
        #print(page) #test
        file_name="{}.html".format(page['name'])
        path=os.path.join(data_dir,file_name)

        print("Processing... {} -> {}".format(page['url'],file_name))
        urllib.request.urlretrieve(page['url'],path)
        print("Done!")

    except:
        print("Failure!")
        break
else:
    print("All pages downloaded succesfully.")