"""
Napisz funkcję show_progress, która będzie wyświetlać linię tekstu powstałą wskutek powtórzenia zadaną ilość razy określonego znaku. Funkcja:
    - przyjmuje argument character, który określa jaki znak ma być powtarzany
    - przyjmuje argument how_many, który określa ile razy znak ma być powtórzony
    - wartość domyślna dla character to gwiazdka
"""


def show_progress(how_many, character='*'):
    print(character * how_many)


show_progress(3,3)
