"""
Oto kod pewnego programu
    cake_01_taste = 'vanilia'
    cake_01_glaze = 'chocolade'
    cake_01_text = 'Happy Brithday'
    cake_01_weight = 0.7

    cake_02_taste = 'tee'
    cake_02_glaze = 'lemon'
    cake_02_text = 'Happy Python Coding'
    cake_02_weight = 1.3


    def show_cake_info(taste, glaze, text, weight):
        print('{} cake with {} glaze with text "{}" of {} kg'.format(
            taste, glaze, text, weight))

    show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
    show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)

Zmień go stosując następujące techniki:
    - zmień definicję zmiennych na słownik z właściwościami
    - zmień definicję funkcji, tak aby przyjmowała jeden parametr
      i nadal wyświetlała informacje przekazane parametrem
    - utwórz listę tortów i przechodząc przez nią wyświetl informacje
      zwracane przez funkcje show_cake_info

"""


def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))


cake01 = {
    'taste': 'vanilia',
    'glaze': 'chocolate',
    'text': 'Happy Birthday',
    'weight': 0.7
}

cake02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Python Coding',
    'weight': 1.3
}

cakes = [cake01, cake02]

show_cake_info(cake01)
show_cake_info(cake02)

print()

for c in cakes:
    show_cake_info(c)
