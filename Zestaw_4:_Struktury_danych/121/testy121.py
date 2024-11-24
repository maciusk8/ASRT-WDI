import unittest
import os
import sys
import importlib

from szablon121 import Zadanie_121


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2, failfast=True).run(suite)


def komenda(k: str, *args, **kwargs):
    """
    Wykonuje zadaną komendę z przekazanymi argumentami.
    Dodanie wlasnej komendy ogranicza sie do dodania pliku z funkcja o tej samej nazwie
    w folderze glownym projektu src/Komendy
    Wiecej informacji o dodaniu wlasnej komendy jak i lista komend w ReadMe projektu

    Args:
        k (str): Komenda do wykonania.
        *args: Dodatkowe argumenty do komendy.
        **kwargs: Dodatkowe argumenty kluczowe do komendy.
    """
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join(os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_121_argumenty_tablica_tablica_tablica_tablica_tablica_tablica(
        self,
    ):
        self.assertEqual(
            Zadanie_121([1, 1], [3, 1], [1, 1], [2, 3], [5, 1], [1, 1]),
            ((2, 3), (1, 9)),
        )

    def test_Nr02_Zadanie_121_argumenty_tablica_tablica_tablica_tablica_tablica_tablica(
        self,
    ):
        self.assertEqual(
            Zadanie_121([4, 2], [10, 3], [3, 3], [3, 4], [7, 1], [5, 1]),
            ((-58, 69), (37, 46)),
        )

    def test_Nr03_Zadanie_121_argumenty_tablica_tablica_tablica_tablica_tablica_tablica(
        self,
    ):
        self.assertEqual(
            Zadanie_121([1, 2], [4, 4], [3, 8], [5, -2], [3, 9], [1, 4]),
            ((3, -64), (51, 128)),
        )

    def test_Nr04_Zadanie_121_argumenty_tablica_tablica_tablica_tablica_tablica_tablica(
        self,
    ):
        self.assertEqual(
            Zadanie_121([2, 3], [5, 1], [1, 1], [1, 2], [4, 3], [8, 8]),
            ((-66, -29), (3, -29)),
        )

    def test_Nr07_Zadanie_121_argumenty_tablica_tablica_tablica_tablica_tablica_tablica(
        self,
    ):
        self.assertEqual(
            Zadanie_121([1, 2], [3, 4], [2, 5], [4, 1], [3, 7], [6, 2]),
            ((-97, -130), (-7, -195)),
        )