import unittest
from contextlib import redirect_stdout
import io

from szablon145 import Zadanie_145


def odpal_testy():
    suite = unittest.TestLoader().loadTestsFromTestCase(testy)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


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
    import os
    import sys
    import importlib
    sciezka_pliku_wykonalnego = os.path.abspath(sys.argv[0])
    srt_dir = os.path.join( os.path.dirname(sciezka_pliku_wykonalnego), "../../srt")
    sys.path.append(srt_dir)
    nr_zadania = os.path.basename(os.path.dirname(sciezka_pliku_wykonalnego))
    return importlib.import_module("WykonajKomende").wykonaj_komende(
        k, sciezka_pliku_wykonalnego, nr_zadania, *args, **kwargs
    )


class testy(unittest.TestCase):

    def test_Nr01_Zadanie_145(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_145([1, 2, 3, 4, 5, 6], 6)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[1, 2, 3]\n[1, 6]\n[2, 3]')

    def test_Nr02_Zadanie_145(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_145([1, 1, 1, 1, 1], 1)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[1, 1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1]\n[1, 1, 1, 1]\n[1, 1, 1]\n[1, 1, 1]\n[1, 1]\n[1, 1, 1, 1]\n[1, 1, 1]\n[1, 1, 1]\n[1, 1]\n[1, 1, 1]\n[1, 1]\n[1, 1]\n[1, 1, 1, 1]\n[1, 1, 1]\n[1, 1, 1]\n[1, 1]\n[1, 1, 1]\n[1, 1]\n[1, 1]\n[1, 1, 1]\n[1, 1]\n[1, 1]\n[1, 1]')

    def test_Nr03_Zadanie_145(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_145([2, 3, 5], 6)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[2, 3]')

    def test_Nr04_Zadanie_145(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_145([3, 6, 8, 1, 3, 4, 6], 8)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[8, 1]')

    def test_Nr05_Zadanie_145(self):
            f = io.StringIO()
            with redirect_stdout(f):
                Zadanie_145([2, 1, 3, 7, 6, 9, 8, 4], 12)
            wynik = f.getvalue().strip()

            self.assertEqual(wynik, '[2, 1, 6]\n[2, 6]\n[1, 3, 4]\n[3, 4]')


