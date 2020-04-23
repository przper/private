"""
W tym zadaniu nadal pracujemy nad klasą "Ciastko"
    - Dodaj do klasy Cake ukryty atrybut gluten_free.
    (To jedna z ważniejszych informacji o wypiekach,
    dlatego staramy się, żeby ten atrybut można było
    ustawić tylko raz podczas tworzenia obiektu,
    dzięki czemu później podczas pracy programu nie
    zmienimy przypadkowo wartości w tym polu)
    - Zmień funkcję __init__ oraz show_info tak,
    aby obsługiwały nowy atrybut klasy
    - Tworząc nowe obiekty wypieków przekazuj wartość
    True lub False wskazującą na to czy wypiek jest
    bezglutenowy (o ile wiem jajka nie zawierają glutenu,
    więc bezy są bezglutenowe)
    - Przetestuj działanie programu
    - Spróbuj w kodzie programu (np. po wyświetleniu oferty ciastkarni)
    zmienić atrybut __gluten_free
    - Czy po uruchomieniu masz błąd? Dlaczego?
    Korzystając z polecenia dir(cake03) zobacz jakie atrybuty
    ma ten obiekt
    - Zmień wartość atrybutu korzystając ze specjalnie
    i automatycznie utworzonego atrybutu o specyficznej budowie
    tak, jak to było zrobione w materiale video
    - Wyświetl ponownie informacje o cake03 (beza) - czy teraz stała
    się wyrobem glutenowym?
"""


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []
    __gluten_free = False

    def __init__(self, name, kind, taste, additives, filling, gluten_free):
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
        print(30 * '-')

    def set_filling(self, filling):  # change a filling
        self.filling = filling

    def add_additives(self, additive):  # append a additive
        self.additives.append(additive)


Cake01 = Cake('Birthday Cake', 'birthday', 'chocolate', ['white chocolate', 'raspberries'], 'none', False)
Cake02 = Cake('Cheesecake', 'cheesecake', 'cheese', ['twix pieces'], 'none', False)
Cake03 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], 'Toffifi', False)
Cake04 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', ['none'], 'None', False)
Cake05 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True)

print("Today's offer:")
for c in Cake.bakery_offer:
    Cake.show_info(c)

print(dir(Cake05))
Cake05._Cake__gluten_free = False

Cake.show_info(Cake05)
print(dir(Cake05))