# ====================================================================================================>
# Zadanie 111
# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
# przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
# wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
# ====================================================================================================>
# return tuple(wiersz1,kolumna1, wiersz2,kolumna2)


def Zadanie_111(tab): ...


if __name__ == "__main__":
    from testy111 import odpal_testy

    Zadanie_111(int(input('Podaj tab: ')))

    # odpal_testy()
