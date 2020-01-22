"""
Pracujemy z wynikiem LAB z poprzedniej lekcji.

Dodaj do klasy Cake atrybut na poziomie klasy.
Nazwij go known_types. Będą w nim przechowywane produkowane
w naszej cukierni słodkości. Przypisz do zmiennej listę np.
w następującej postaci:

['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']

Zmień __init__ tak, że jeżeli jako parametr kind zostanie
przekazana wartość znajdująca się na liście known_kinds,
to zostanie zaakceptowana, ale jeśli ktoś przekaże wartość
spoza tej listy, to do nowo tworzonego obiektu do atrybutu
kind zostanie wpisany napis other.

Przetestuj działanie nowej funkcji __init__ tworząc obiekt "wafel kakaowy":

cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')


Dodaj do klasy Cake nowy atrybut bakery_offer, który na początku
będzie pustą listą.

Zmień __init__ tak, aby po utworzeniu nowego obiektu typu Cake,
został on automatycznie dodany do listy bakery_offer

Usuń ze skryptu niepotrzebne już instrukcje tworzące listę bakery_offer
i dodające obiekty tej klasy do tej listy.

Zmień pętlę wyświetlającą informację o ofercie cukierni tak,
aby korzystała z atrybutu klasy


Sprawdź czy obiekty cake01 i inne są instancjami klasy Cake
korzystając z funkcji isinstance i type

Wyświetl informacje o instancji cake01 i o klasie Cake
korzystając z funkcji vars i dir
"""


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

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
        print(30 * '-')

    def set_filling(self, filling):  # change a filling
        self.filling = filling

    def add_additives(self, additive):  # append a additive
        self.additives.append(additive)


Cake01 = Cake('Birthday Cake', 'birthday', 'chocolate', ['white chocolate', 'raspberries'], 'none')
Cake02 = Cake('Cheesecake', 'cheesecake', 'cheese', ['twix pieces'], 'none')
Cake03 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], 'Toffifi')
Cake04 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', ['none'], 'None')
Cake05 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')


print("Is Cake01 instance of Cake class:", isinstance(Cake01, Cake))
print("Is Cake01 instance of Cake class:", type(Cake01) is Cake)

print()
print(vars(Cake01))
print(vars(Cake))
print()
print(dir(Cake01))
print(dir(Cake))

print("Today's offer:")
for c in Cake.bakery_offer:
    Cake.show_info(c)