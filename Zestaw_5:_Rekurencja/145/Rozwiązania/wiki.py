# ====================================================================================================>
# Zadanie 145
# Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.
# ====================================================================================================>
# Dla [1, 2, 3, 4, 5, 6], 6 wynik to '[1, 2, 3]\n[1, 6]\n[2, 3]' kolejnosci printowania nie ma znaczenia


# Juliusz Wasieleski
def Zadanie_145(A, x):
    res = []
    rek(A, x, [], res)
    for r in res:
        print(r)


def rek(A, x, tmp_tab, final_tab, i=0, curr=1, dig_mult=0):
    if curr == x and i == len(A) and dig_mult > 1:
        final_tab.append(tmp_tab)
        return
    if curr > x or curr == 0 or i == len(A):
        return
    rek(A, x, [*tmp_tab, A[i]], final_tab, i + 1, curr * A[i], dig_mult + 1)
    rek(A, x, tmp_tab, final_tab, i + 1, curr, dig_mult)
    return


