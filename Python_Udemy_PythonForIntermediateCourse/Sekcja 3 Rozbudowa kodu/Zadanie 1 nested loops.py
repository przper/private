"""
Na przykładzie z wpłatomatem z poprzedniego zadania postanawiasz
wraz ze swoim szefem otworzyć linie lotnicze "Flying Python". Linie będą krajowe.
Oto wykaz portów lotniczych:
    ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
             'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy.
   Wykonaj połączenie każdy-z-każdym
2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu
3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A -
   wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.
4. Policz ilość generowanych połączeń w krokach 1,2,3
"""

portsA = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ', 'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
portsB = portsA.copy()

#1 wszystkie
route = [(a,b) for a in portsA for b in portsB]
print(route)
print("Number of available destinations:",len(route))
print("-----")

#2 eliminacja WAW->WAW
route = [(a,b) for a in portsA for b in portsB if a!=b]
print(route)
print("Number of available destinations:",len(route))
print("-----")

#3 eliminacja KRK=WAW jeśli istnieje WAW->KRK
route = [(a,b) for a in portsA for b in portsB if a<b]
print(route)
print("Number of available destinations:",len(route))
print("-----")
