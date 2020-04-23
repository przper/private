"""
LAB - Klasy i atrybuty instancji klasy

Szef cukierni w której pracujesz poprosił Cię
o napisanie programu, który koniecznie ma działać obiektowo!
Zaczynamy od zdefiniowania klasy Cake, która ma posiadać atrybuty:

-name opisujące nazwę produktu
-kind opisujący rodzaj wypieku np. torty, ciastka, muffinki, bezy
-taste z głównym smakiem
-addictions - zawierający listę dodatków do danego ciasta,
 np. owoce, posypki, polewy itp, jeżeli ciasto nie ma dodatków, to będzie to pusta lista
-filling - opis nadzienia, jeżeli dane ciasto nie ma nadzienia, to ma to być pusty napis
-... możesz dodać dalsze własne pomysły :)

Po zdefiniowaniu klasy utwórz kilka instancji tej klasy,
to dobry moment na wzbogacenie słownictwa w zakresie słodkości
w języku angielskim, ale jak wolisz - możesz to robić po polsku

Utwórz listę bakery_offer i dodaj do niej instancje
wcześniej utworzonych obiektów klasy Cake


Napisz pętlę przechodzącą przez wszystkie instance klasy znajdujące
się na liście bakery_offer i wyświetl coś w rodzaju (dane pochodzące
z instancji zostały wytłuszczone):

Today in our offer:
Vanilla Cake - (cake) main taste: vanilla with additives of ['chocolade', 'nuts'], filled with cream

Chocolade Muffin - (muffin) main taste: chocolade with additives of ['chocolade'], filled with

Super Sweet Maringue - (meringue) main taste: very sweet with additives of [], filled with
"""


class Cake:
    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions.copy()
        self.filling = filling


Cake01 = Cake('BirthdayCake', 'birthday', 'chocolate', ['white chocolate'], 'none')
Cake02 = Cake('Cheesecake', 'cheesecake', 'cheese', ['twix pieces'], 'none')
Cake03 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], 'none')
Cake04 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', ['none'], 'none')

Bakery_offer = [Cake01, Cake02, Cake03, Cake04]

print("Today in our offer:")
for c in Bakery_offer:
    print(
        "{} - ({}) main taste: {} with additives of {}, filled with {}".format(c.name, c.kind, c.taste, c.addictions,
                                                                                 c.filling))
"""
UWAGA: w kolejnych lekcjach i kolejnych zadaniach będę kontynuował temat cukierni.
W większości przypadków zadanie będzie polegało na rozbudowaniu tej klasy.
Jeżeli chcesz wykonać wiecej zadań pozwalających Ci lepiej opanować tematykę klas,
podrzucam kilka pomysłów poniżej. Do tych pomysłów nie publikuję propozycji rozwiązań.
Za to możesz takie własne rozwiązania i propozycje publikować w sekcji Q&A .
Możesz też próbować budowania klas z takimi tematami jak sam zechcesz.

"Sklep z używanymi telefonami komórkowymi"
"Warsztat wulkanizacyjny"
"Inwentaryzacja sprzętu komputerowego w firmie"
"Studio fitness"
"Karty gwarancyjne"
"Firma przewozowa - taxi bagażowe"
"Biuro podróży"
"""
