"""
Utwórz następujące listy:
    projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
    leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

Korzystając ze "sprytnej" metody pracy z for wyświetl komunikaty w postaci:
The leader of "...nazwa projektu..." is ...imię i nazwisko lidera...

Utwórz kolejną listę z datami rozpoczęcia projektów:
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... is ...imię i nazwisko lidera...

Korzystając ze "sprytnego" złożenia enumerate i zip - dodaj do komunikatu
dodatkowo numer kolejny projektu rozpoczynając od 1:

...numer kolejny... - The leader of "...nazwa projektu..."  started
...data rozpoczęcia projektu... is ...imię i nazwisko lidera...
"""

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for project, leader in zip(projects, leaders):
    print("The Leader of {} is {}".format(project, leader))

print()
print("----------")
print()
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for project, date, leader in zip(projects, dates, leaders):
    print("The Leader of {} started {} is {}".format(project, date, leader))

print()
print("----------")
print()

for pos, (project, date, leader) in enumerate(zip(projects, dates, leaders)):
    print("[{}] The Leader of {} started {} is {}".format(pos + 1, project, date, leader))

print()
print(list(enumerate(leaders)))
print(list(enumerate(zip(projects, dates, leaders))))