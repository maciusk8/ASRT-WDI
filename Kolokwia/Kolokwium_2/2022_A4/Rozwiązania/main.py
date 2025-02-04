# ====================================================================================================>
# Zadanie A4, 20.12.2022
# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# skoczków. Położenie skoczka w tablicy oznaczono liczbą 1, puste pola oznaczono liczbą 0. Część pustych pól
# na szachownicy jest szachowana przez znajdujące się na niej skoczki. Proszę zaproponować funkcję place(T),
# która znajdzie na szachownicy puste pole położone najbliżej środka szachownicy, takie że umieszczenie tam
# skoczka maksymalnie zwiększy liczbę szachowanych pustych pól. Do funkcji przekazujemy tablicę T zawierającą położenie skoczków.
# Funkcja powinna zwrócić pole (wiersz, kolumna), na którym należy umieścić
# skoczka. Odległość pomiędzy polami: (w1, k1) i (w2, k2) jest równa max(abs(w1 − w2), abs(k1 − k2))
# ====================================================================================================>


def place(T):
    N = len(T)
    center = (N // 2, N // 2)  # Środek szachownicy

    knight_moves = [ (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N

    def count_newly_attacked(x, y):
        """Funkcja do liczenia nowych szachowanych pól z danego pola"""
        res = 0

        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and T[nx][ny] == 0:
                res += 1

        # Jeśli pole było już szachowane, tracimy jedno pole
        if T[x][y] == 2:
            res -= 1
        return res

    # zmien pola atakowane na 2
    for i in range(N):
        for j in range(N):
            if T[i][j] == 1:
                for dx, dy in knight_moves:
                    nx, ny = i + dx, j + dy

                    if is_valid(nx, ny) and T[nx][ny] == 0:
                        T[nx][ny] = 2

    best_position = None
    max_new_attacked = -1
    min_distance_to_center = N

    for i in range(N):
        for j in range(N):
            if T[i][j] != 1:  # Pole musi być puste
                new_attacked = count_newly_attacked(i, j)
                distance_to_center = max(abs(i - center[0]), abs(j - center[1]))

                # Maksymalizujemy nowe szachowane pola, a przy remisie minimalizujemy odległość
                if new_attacked > max_new_attacked or ( new_attacked == max_new_attacked and distance_to_center < min_distance_to_center):
                    best_position = (i, j)
                    max_new_attacked = new_attacked
                    min_distance_to_center = distance_to_center

    return best_position


