import unittest
import CalculerSalaire as cs

#méthode d'implémentation de test : module unittest
# + definition d'une classe de test qui hérite de unittest
# + utilisation de la méthode assertEqual pour comparer le retour de la fonction appelée et le résultat attendu
# exécution dans un main en appelant la méthode main sur le module unittest
class TestsSalaires(unittest.TestCase):
    def test_architecte(self):
        self.assertEqual(cs.calculerSalaire("architecte", 4), 4000)

    def test_medecin(self):
        self.assertEqual(cs.calculerSalaire("medecin", 8), 7000)

    def test_consultant(self):
        self.assertEqual(cs.calculerSalaire("consultant", 5), 5000)


if __name__ == '__main__':
    unittest.main()