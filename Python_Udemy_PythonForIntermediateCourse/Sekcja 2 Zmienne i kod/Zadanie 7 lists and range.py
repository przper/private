"""
Budujesz moduł generujący wykresy. Chcesz samodzielnie wpływać na to,
jakie kolory będą wykorzystane na wykresie.
Definiujesz na początku listę kolorów:
["red", "orange", "green", "violet", "blue", "yellow"]

Czasami na wykresie będą prezentowane tylko 3 kategorie
i wtedy chcesz wykorzystać tylko 3 pierwsze kolory,
innym razem wykres ma mieć 5 kategorii i potrzebujesz listę 5 kolorów.

Napisz funkcję, która przyjmuje dwa argumenty:
listę kolorów i liczbę n.

Funkcja ma zwracać nową kopię listy kolorów
o długości n korzystając z przekazanej listy argumentów.

Napisz pętlę, która wygeneruje wszystkie możliwe
zestawy kolorów dostępne w liście. Pętla powinna radzić
sobie z wyświetleniem wszystkich zestawów, nawet jeżeli
do początkowej listy zostanie kiedyś dodany następny kolor
(nie korzystaj z wpisywania na stałe wartości liczbowej).

Napis też można "kroić". Wytnij z poniższego tekstu
pochodzącego z https://nonsa.pl/wiki/Korporacja (dawniej nonsensopedia.pl)
fragment tłumaczący pochodzenie słowa "Korporacja" -
- fragment znajduje się w nawiasach (same nawiasy pomiń):

Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura)
– organizacja, która pod przykrywką prowadzenia biznesu
włada dzisiejszym światem. Wydawać się może utopijnym miejscem
realizacji pasji zawodowych. W rzeczywistości jednak nie jest
wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka
w imię postępu. Rządzi w niej prawo dżungli.
"""

def color_set (color_list, n):
    result = list(range(n))
    for i in range(n):
        result[i] = color_list[i]
        #print(result[i])
    #print(result)
    return result

"""
def get_list_of_colors(colors, n):
    return colors[:n]
"""

x=3
color_list= ["red", "orange", "green", "violet", "blue", "yellow"]
print(color_set(color_list,x))
print("Color list id:",id(color_list))
print("Color set id:",id(color_set(color_list,x)))

print()
print("Możliwe zestawy kolorów:")
for i in range(len(color_list)):
    print("Zestaw {}: {}".format(i+1,color_list[:i+1]))

print()
print("---------")
Korporacja = "(z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. "

#print("Korporacja -",Korporacja[1:57])
print("Korporacja:",Korporacja[Korporacja.index('(')+1:Korporacja.index(')')])