"""
Utwórz plik i wpisz do niego kilka słów, np co widzisz za oknem :)
Utwórz funkcję, która jako parametr przyjmuje ścieżkę dostępu do pliku i zwraca ilość słów w tym pliku, jeśli potrzebujesz kroków pomocniczych oto i one:
    Otwórz plik poleceniem open (możesz skorzystać z parametru encoding="utf-16" jeżeli trzeba)
    Wczytaj plik do zmiennej korzystając z funkcji read()
    "Rozbij" wczytaną zawartość korzystając z funkcji split()
    Policz ile elementów jest zwracanych przez funkcję split()
    Zwróć tą wartość
W głównym skrypcie:
    zadeklaruj zmienną path i przypisz jej wartość wskazującą na plik utworzony na początku
    napisz polecenie warunkowe, które sprawdzi czy plik istnieje
        jeśli tak, wywoła funkcję, policzy ilość słów w pliku i wyświetli o tym informację
    napisz wyrażenie logiczne, które wykona te same czynności, co wcześniej napisana instrukcja if
"""
import os
"""
Moje #1 podejscie:
def CountWords(path):
    file=open(path,'r')
    content=file.read()
    count=len(content.split())
    file.close()
    return count
"""

#tak jest ładniej:
def CountWords(path):
    with open(path,'r') as file:
        content=file.read()
        count=len(content.split())
    return count

path = r'C:\Users\Admin\Desktop\Python\Udemy\Sekcja 2 Zmienne i kod\Plik zadanie 4.txt'

if os.path.isfile(path):
    print("Liczba słów w pliku to: ", CountWords(path))

os.path.isfile(path) and print("Liczba słów w pliku to: ",CountWords(path))
