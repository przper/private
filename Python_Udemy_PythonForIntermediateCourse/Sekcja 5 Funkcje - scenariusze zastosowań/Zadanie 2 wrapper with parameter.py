"""
Pracujesz nad aplikacją, która intensywnie pracuje z plikami. Klient zażyczył sobie, aby każda taka operacja została dodatkowo zalogowana. Log powinien mieć postać mniej więcej taką:
    Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:29:17
    Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:33:18
    Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:39:57
    Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:44:18
Wiadomo, że:
    - wszystkie te funkcje przyjmują jeden parametr path (więc mogą korzystać z takiego samego wrappera)
    - klient może chcieć zapisać dane logowania oddzielnie do innego pliku dla każdej funkcji (więc wrappery jednak czymś będą się nieznacznie różnić)
Chcesz rozwiązać problem stosując wrapper. Idealnie będzie napisać jedną funkcję  przyjmującą jako parametry:
    - logged_action określającą wykonywaną czynność np. FILE_CREATE lub FILE_DELETE
    - log_file_path określającą do jakiego pliku zapisywać informacje
Oto przykład funkcji, których praca ma podlegać logowaniu:
    import os

    def create_file(path):
        print('creating file {}'.format(path))
        open(path,"w+")

    def delete_file(path):
        print('deleting file {}'.format(path))
        os.remove(path)

    create_file(r'c:\temp\dummy_file.txt')
    delete_file(r'c:\temp\dummy_file.txt')
    create_file(r'c:\temp\dummy_file.txt')
    delete_file(r'c:\temp\dummy_file.txt')

Proponowana kolejność to:
    zaimportuj moduł os, functools, a z modułu datetime zaimportuj  datetime aliasując go jako dt
    Napisz funkcję wrapper_with_log_file, która:
        przyjmuje parametry logged_action, log_file_path
        w tej funkcji napisz funkcję wrapper_with_log_to_known_file, która:
            przyjmie parametr func - określający dla jakiej funkcji ma być utworzony wrapper
            w tej funkcji napisz funkcję the_real_wrapper, która przyjmie argument path określający plik,  na jakim ma być wykonywana operacja tworzenia lub usuwania plików, która:
                otworzy plik log_file_path dopisując do niego dane
                zapisze informację o wykonywanej czynności logged_action, na jakim pliku była wykonywana ta akcja path, oraz datę i godzinę, kiedy to się stało dt.now().strftime("%Y-%m-%d %H:%M:%S")
                funkcja the_real_wrapper zwróci wynik wywołania funkcji func z parametrem path
            funkcja wrapper_with_log_to_known_file ma zwróć funkcję the_real_wrapper
        funkcja wrapper_with_log_file ma zwróć funkcję wrapper_with_log_to_known_file
    Oznacz funkcje:
        create_file - dekoratorem tworzącym wrapper z parametrami FILE_CREATE i ścieżką pliku log r'c:/temp/file_create.txt'
        delete_file - dekoratorem tworzącym wrapper z parametrami FILE_DELETE i ścieżką pliku log r'c:/temp/file_delete.txt'
    Przetestuj funkcje i sprawdź czy powstały odpowiednie pliki z odpowiednimi wpisami
"""
import os
import functools
from datetime import datetime as dt


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with(open(log_file_path,'a')) as f:
                f.write("Action {} executed on {} on {}\n".format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))
            return func(path)

        return the_real_wrapper
    return wrapper_with_log_to_known_file

@wrapper_with_log_file('FILE CREATE',r'C:\Users\Admin\Desktop\Python\Udemy\Python dla średnio zaawansowanych\Sekcja 5 Funkcje - scenariusze zastosowań\log_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")

@wrapper_with_log_file('FILE DELETE',r'C:\Users\Admin\Desktop\Python\Udemy\Python dla średnio zaawansowanych\Sekcja 5 Funkcje - scenariusze zastosowań\log_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


create_file(r'C:\Users\Admin\Desktop\Python\Udemy\Python dla średnio zaawansowanych\Sekcja 5 Funkcje - scenariusze zastosowań\dummy_file.txt')
delete_file(r'C:\Users\Admin\Desktop\Python\Udemy\Python dla średnio zaawansowanych\Sekcja 5 Funkcje - scenariusze zastosowań\dummy_file.txt')
create_file(r'C:\Users\Admin\Desktop\Python\Udemy\Python dla średnio zaawansowanych\Sekcja 5 Funkcje - scenariusze zastosowań\dummy_file.txt')
delete_file(r'C:\Users\Admin\Desktop\Python\Udemy\Python dla średnio zaawansowanych\Sekcja 5 Funkcje - scenariusze zastosowań\dummy_file.txt')
