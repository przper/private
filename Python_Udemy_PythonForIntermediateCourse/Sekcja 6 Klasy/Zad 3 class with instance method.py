"""
Do klasy z poprzedniego zadania dodaj 3 metody:
    show info, która
        - wyświetli wielkimi literami nazwę produktu
        - wyświetli informację o smaku
        - jeśli produkt ma jakieś dodatki to je wyświetli
        - jeśli produkt ma nadzienie to je wyświetli
        (oczywiście przetestuj działanie funkcji po jej zaimplementowaniu)

    set_filling, która
        - jako argument przyjmie nazwę nadzienia ciasta
        - zapisze ją w atrybucie filling dla ciasta
        (oczywiście przetestuj działanie funkcji)

    add_additives, która
        - jako argument przyjmie listę dodatków
        - wartości z listy doda do aktualnej listy dodatków
        - (tę funkcję też przetestuj)

Następnie dodaj do muffinki nadzienie kremowe,
a do bezy dodaj kokos i posypkę kakaową.
Tak zmodyfikowane wypieki wyświetl.
Poniżej zobacz spodziewany efekt:

    Today in our offer:
    VANILLA CAKE
    Kind:    cake
    Taste:   vanilla
    Additives:
    	chocolade
    	nuts
    Filling: cream
    --------------------
    CHOCOLADE MUFFIN
    Kind:    muffin
    Taste:   chocolade
    Additives:
    	chocolade
    Filling: vanilla cream
    --------------------
    SUPER SWEET MARINGUE
    Kind:    meringue
    Taste:   very sweet
    Additives:
    	cocoa powder
    	coconuts
    --------------------

"""


class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

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

#Cake03.show_info()
Cake03.set_filling('Chocolate')
Cake03.add_additives('posypka')
#Cake03.show_info()

bakery_offer = [Cake01,Cake02,Cake03,Cake04]

print("Today in our offer:")
for c in bakery_offer:
    c.show_info()