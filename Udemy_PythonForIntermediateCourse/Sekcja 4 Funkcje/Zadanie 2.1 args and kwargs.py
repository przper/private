"""
Przygotowujesz program dla sklepu z farbami. Klienci pytają czasami ile farby potrzeba do pomalowania mieszkania.
Napisz funkcję calculate_paint, która:
    - przyjmuje argument efficency_ltr_per_m2 - określającą ile farby trzeba do pomalowania metra kwadratowego
    - przyjmuje dowolną ilość kolejnych argumentów odpowiadających za powierzchnie do pomalowania dla pokoi mieszkania, które ma być pomalowane
    - funkcja ma zwracać informację o ilości potrzebnej farby

Przetestuj funkcję na dwa sposoby:
    - przekazując powierzchnie do pomalowania w poszczególnych pokojach po prostu po przecinku wywołując funkcję
    - definiując listę z powierzchniami, a następnie przekazując do funkcji tą listę
"""


def calculate_paint_int(efficency_ltr_per_m2,area):
    volume=float(efficency_ltr_per_m2)*float(area)
    print("Do pomalowania jest łącznie {} metrów kwadratowych".format(area))
    print("Potrzeba {} litrów farby".format(volume))

def calculate_paint_list(efficency_ltr_per_m2,list_of_areas):
    area=sum(list_of_areas)
    volume = float(efficency_ltr_per_m2) * float(area)
    print("Do pomalowania jest łącznie {} metrów kwadratowych".format(area))
    print("Potrzeba {} litrów farby".format(volume))

#to glupie, ale zostawiam dla potomnych
def start():
    yes_or_no = input("1 Czy chcesz rozpocząć tworzenie listy pokoi? <y/n> ")
    bool = False
    if yes_or_no == 'y':
        bool = True
    elif yes_or_no=='n':
        bool = False
    else:
        print("Musisz użyć 'y' lub 'n'")
    print('1',bool,type(bool))
    return bool

def create_list(list):
    bool = True
    while bool:
        data = input("Podaj powierzchnie pokoju w m2: ")
        if data:
            list.append(float(data))
            print("Dodano powierzchnie pokoju:", data)
        else:
            bool = False
            print("Zakończono dodawanie")
    return(list)


"""
#1 pierwsze podejscie
efficiency = input("Podaj wydajność farby: ")
meters = input("Podaj ilość metrów do pomalowania: ")
calculate_paint_int(efficiency,meters)
"""

#2 chce stworzyc petle ktora tworzy liste, proszac o podanie kolejnego pokoju


#start()
#print('2',bool)





list_of_rooms = []
#print(list_of_rooms)
create_list(list_of_rooms) #dodajemy pokoje do listy
print("Podane powierzchnie to: ",list_of_rooms) #pokazujey pokoje

efficiency = input("Podaj wydajność farby: ")
calculate_paint_list(efficiency, list_of_rooms)

