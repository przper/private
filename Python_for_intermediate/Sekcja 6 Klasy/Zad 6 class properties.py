"""
W tym LAB pracujemy z klasą z poprzedniej lekcji (jeśli nie masz
rozwiązania skopiuj sobie moją propozycję rozwiązania z poprzedniej lekcji)

   -  Do klasy należy dodać atrybut ukryty __text. Odpowiada on za napis umieszczony na torcie.
    - W funkcji __init__ przyjmij nowy argument text
    - Zapisz go w zmiennej __text przeprowadzając kontrolę: napis można zapisać w instancji
    tylko jeżeli kind jest 'cake' lub text jest napisem pustym. Jeśli te warunki nie są
    spełnione wyświetl diagnostyczny komunikat (print dla Ciebie, żeby było wiadomo co się dzieje)
    - Dodaj ukrytą funkcję __get_text, która będzie zwracać wartość zapisaną w __text
    - Dodaj ukrytą funkcje __set_text, która przyjmie dodatkowy argument new_text
    i zaktualizuje atrybut __text tylko dla wyrobów z kind 'cake'
    - Zdefiniuj właściwość Text korzystającą z powyższych funkcji.
    - Tworząc obiekty klasy Cake przekaż dodatkowy argument text - umieść napisy puste lub inne
    typowo  "tortowe", część poprawnych (czyli napis na torcie) i część niepoprawnych (np. napis na waflu)
    - Wyświetl wszystkie informacje o wszystkich wypiekach
    - Spróbuj wstawić do właściwości Text napis na torcie i na innym wypieku nietortowym - prześledź
    poprawność tych operacji ponownie wyświetlając ofertę cukierni
"""


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []
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


Cake01 = Cake('Birthday Cake', 'cake', 'chocolate', ['white chocolate', 'raspberries'], 'none', False,
              '3 urodziny Hani')
Cake02 = Cake('Cheesecake', 'cheesecake', 'cheese', ['twix pieces'], 'none', False, 'osiem')
Cake03 = Cake('Chocolate Muffin', 'muffin', 'chocolate', ['chocolate'], 'Toffifi', False, 'osiem')
Cake04 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', ['none'], 'None', False, 'osiem')
Cake05 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, 'osiem')

Cake.show_info(Cake01)
Cake01.Text = "3 urodziny Haneczki"
Cake.show_info(Cake01)

'''
print("Today's offer:")
for c in Cake.bakery_offer:
    Cake.show_info(c)
'''
