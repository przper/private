"""
Dlaczego warto wykonywać zadania? Bo w tym zadaniu będzie ciekawie.
Skorzystasz z 2 fantastycznych funkcji, których nie omówiłem na kursie. Ale po kolei:
Naszym zadaniem jest zapisanie na dysku informacji o wyrobach naszej cukierni.
Obiekty klasy Cake są już trochę skomplikowane, wiec do ich eksportowania na dysk
i importowania z dysku wykorzystamy moduł pickle. (Kilka słów o module
i link do dokumentacji znajdziesz poniżej), a tu krótkie streszczenie:

Moduł zaimportujesz komendą
    import pickle

Jeśli f to uchwyt do pliku, a obj to jakiś obiekt, to możesz go zapisać na dysku poleceniem:
    pickle.dump(obj, f)

A jeśli potem ten obiekt chcesz odczytać, to możesz to zrobić tak:
    new_obj = pickle.load(f)


No to do roboty.
    - Dodaj do klasy funkcję save_to_file. Funkcja ma pracować na poziomie instancji
    - Funkcja ma przyjąć argument path wskazujący na ścieżkę dostępu do pliku
    - Plik należy otworzyć do zapisu w trybie binarnym i korzystając z pikle.dump zapisać bieżący obiekt do pliku
    - Przetestuj działanie funkcji zapisując cake01 i cake02 do plików. Nadaj plikom rozszerzenie bakery
    - Dodaj do klasy funkcję read_from_file. Funkcja ma przyjmować jako argument ścieżkę do pliku
    - Funkcja ma otworzyć plik na odczyt w trybie binarnym i wczytać obiekt klasy Cake z tego pliku korzystając z pickle.load
    - Nowy obiekt należy dopisać do zmiennej klasy bakery_offer i zwrócić ten obiekt
    - Przetestuj działanie funkcji wczytując plik z poprzedniego przykłądu do nowego obiektu np. cake05.
    Aby przetestować czy wszystko się udało wywołaj dla tego nowego obiektu z funkcji show_info


No dobrze, ale jeśli znamy ścieżkę dostępu do katalogu i  w tym katalogu znajdują się pliki z rozszerzeniem
bakery, to chcielibyśmy mieć funkcję , która zwróci listę takich plików.
Odpowiednią do tego prawie gotową funkcję znajdziesz w module glob:
    import glob

Aby otrzymać listę plików z rozszerzeniem txt z katalogu c:/temp możesz wywołać funkcję:
    glob.glob('c:/temp/*.txt')

    - Dodaj do klasy Cake funkcję statyczną get_bakery_files, która jako argument przyjmie nazwę katalogu
    - Funkcja ma zwrócić listę plików z rozszerzeniem bakery z przekazanego argumentem katalogu
    - Przetestuj działanie funkcji


-----------------------------------------------------------------------------------

Krótka dokumentacja modułu pickle ze strony:

https://pl.python.org/docs/tut/node9.html

7.2.2 Moduł pickle
Napisy mogą być w łatwy sposób zapisywane i czytane z pliku. Liczby wymagają trochę więcej zachodu,
bowiem metoda read() zwraca tylko napis, który musi być poddany działaniu takiej funkcji,, jak string.atoi(),
która pobiera napis w rodzaju '123' i zwraca wartość liczbową 123. W przypadku jednak, gdy chce się przechowywać
w pliku bardziej złożone typy danych jak listy, słowniki lub instancje klas, sprawy się nieco komplikują.

Python dostarcza standardowy moduł pickle, który zaoszczędza użytkownikom pisania i śledzenia kodu służącego
do zachowywania skomplikowanych typów danych. Ten zadziwiający7.4moduł potrafi wziąć na wejściu prawie każdy
obiekt Pythona (nawet pewne formy kodu!) i przekształcić go w napis. Proces ten zwie się marynowaniem7.5.
Rekonstruowanie obiektu z formy napisowej zwie się odmarynowaniem7.6. Pomiędzy marynowaniem a odmarynowaniem,
napis reprezentujący obiekt może zostać zapisany w pliku lub w innej danej, lub przesłany połączeniem sieciowym
do jakiegoś oddalonego komputera.7.7

Jeżeli istnieje obiekt x i obiekt pliku f, który został otwarty do pisania,
to najprostszy sposób zamarynowania obiektu zajmuje jeden wiersz kodu:


    pickle.dump(x, f)

Zakładając, że f jest obiektem pliku, który został otwarty do czytania, odmarynowanie przebiega następująco:

    x = pickle.load(f)

(Istnieją warianty tego mechanizmu użyteczne w przypadku marynowania wielu obiektów, lub gdy nie chce się
zapisać danych marynaty w pliku -- skonsultuj się z pełną dokumentacją dla modułu pickle, którą znajdziesz
w «Opisie biblioteki»).

pickle jest standardowym sposobem na uczynienie obiektów Pythona trwałymi i ponownie użytymi przez inne
programy lub przyszłe wywołania tego samego programu: technicznym określeniem tego mechanizmu jest trwałośćobiektu.
Z powodu powszechnego użycia modułu pickle, wielu autorów piszących rozszerzenia do Pythona, dba o to,
aby nowe typy danych, takie jak macierze, mogły być poprawnie zamarynowane i odmarynowane.


--------------------------------------------------------------------------------------------------

https://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie/Praca_z_katalogami

Jest jeszcze inna metoda dostania się do zawartości katalogu. Metoda ta jest bardzo potężna i używa zestawu
symboli wieloznacznych (ang. wildcard), z którymi można się spotkać pracując w linii poleceń.

Przykład. Listowanie zawartości katalogu przy pomocy glob

    >>> os.listdir("c:\\music\\_singles\\")               #(1)
    ['a_time_long_forgotten_con.mp3', 'hellraiser.mp3',
    'kairo.mp3', 'long_way_home1.mp3', 'sidewinder.mp3',
    'spinning.mp3']
    >>> import glob
    >>> glob.glob('c:\\music\\_singles\\*.mp3')           #(2)
    ['c:\\music\\_singles\\a_time_long_forgotten_con.mp3',
    'c:\\music\\_singles\\hellraiser.mp3',
    'c:\\music\\_singles\\kairo.mp3',
    'c:\\music\\_singles\\long_way_home1.mp3',
    'c:\\music\\_singles\\sidewinder.mp3',
    'c:\\music\\_singles\\spinning.mp3']
    >>> glob.glob('c:\\music\\_singles\\s*.mp3')          #(3)
    ['c:\\music\\_singles\\sidewinder.mp3',
    'c:\\music\\_singles\\spinning.mp3']
    >>> glob.glob('c:\\music\\*\\*.mp3')                  #(4)

    Jak wcześniej powiedzieliśmy, os.listdir pobiera ścieżkę do katalogu i zwraca wszystkie
    pliki i podkatalogi, które się w nim znajdują.

    Z drugiej strony, moduł glob na podstawie podanego wyrażenia składającego się z symboli wieloznacznych,
    zwraca pełne ścieżki wszystkich plików, które spełniają te wyrażenie. Tutaj wyrażenie jest ścieżką do
    katalogu plus "*.mp3", który będzie dopasowywał wszystkie pliki .mp3. Dodajmy, że każdy element zwracanej
    listy jest już pełną ścieżką do pliku.

    Jeśli chcemy znaleźć wszystkie pliki w określonym katalogu, gdzie nazwa zaczyna się od "s",
    a kończy na ".mp3", możemy to zrobić w ten sposób.

    Teraz rozważ taki scenariusz: mamy katalog z muzyką z kilkoma podkatalogami, wewnątrz których są pliki .mp3.
     Możemy pobrać listę wszystkich tych plików za pomocą jednego wywołania glob, wykorzystując połączenie dwóch
      wyrażeń. Pierwszym jest "*.mp3" (wyszukuje pliki .mp3), a drugim są same w sobie ścieżki do katalogów,
      aby przetworzyć każdy podkatalog w c:\music. Ta prosto wyglądająca funkcja daje nam niesamowite możliwości!
"""

import pickle
import os
import glob


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []  # lista wszystkich instancji
    __gluten_free = False
    __text = '-'

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if self.kind == 'cake':
            self.__text = text
        elif self.__text == '':
            self.__text = text
        else:
            print("Error, cannot save 'text' attribute ({})".format(name))

    def show_info(self):
        print(self.name.upper())
        print("Kind:", self.kind)
        print("Taste:", self.taste)
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print(" -", a)
        if len(self.filling) > 0:
            print("Filling:", self.filling)
        print("Gluten free:", self.__gluten_free)
        print("Text:", self.__text)
        print(30 * '-')

    def set_filling(self, filling):  # change a filling
        self.filling = filling

    def add_additives(self, additive):  # append a additive
        self.additives.append(additive)

    # Dodaj ukrytą funkcję __get_text, która będzie zwracać wartość zapisaną w __text
    def __get_text(self):
        return self.__text

    # Dodaj ukrytą funkcje __set_text, która przyjmie dodatkowy argument new_text i zaktualizuje atrybut __text tylko dla wyrobów z kind 'cake'
    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print("Error, cannot change 'text' attribute ({})".format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on cake')

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)
        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(path):
        return glob.glob(path+'/*.bakery')


path = r'C:/Users/Admin/Desktop/Python/Udemy/Python dla średnio zaawansowanych/Sekcja 6 Klasy/Zad 7/'

Cake01 = Cake('Birthday Cake', 'cake', 'chocolate', ['white chocolate', 'raspberries'], 'none', False,
              '3 urodziny Hani')
Cake02 = Cake('Cheesecake', 'cheesecake', 'cheese', ['twix pieces'], 'none', False, 'osiem')
Cake03 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], 'Toffifi', False, 'osiem')
Cake04 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', ['none'], 'None', False, 'osiem')
Cake05 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, 'osiem')

'''
Cake01.save_to_file(
    path + 'Cake01.bakery')

Cake06 = Cake.read_from_file(
    path + 'Cake01.bakery')

Cake.show_info(Cake01)
print()
Cake.show_info(Cake06)
'''

for c in Cake.bakery_offer:
    #print(path + c.name + '.bakery')
    c.save_to_file(path + c.name + '.bakery')

for file in Cake.get_bakery_files(path):
    print(file)