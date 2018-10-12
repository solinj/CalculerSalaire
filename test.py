import unittest
import CalculerSalaire as cs
#si l'expression "from module import *" ne marche pas, écrire "import module"

#méthode d'implémentation de test : il faut utiliser le module unittest
# + definition d'une classe de test qui hérite de unittest
# + utilisation de la méthode assertEqual pour comparer le retour de la fonction appelée et le résultat attendu
# exécution dans un main en appelant la méthode main sur le module unittest


class TestsSalaires(unittest.TestCase): #classe qui hérite de unittest
    def test_architecte(self):
        self.assertEqual(cs.calculerSalaire("architecte", 4), 4000)

    def test_medecin(self):
        self.assertEqual(cs.calculerSalaire("medecin", 8), 7000)

    def test_consultant(self):
        self.assertEqual(cs.calculerSalaire("consultant", 5), 5000)


if __name__ == '__main__':
    unittest.main()
    # print("Le salaire d'un architecte après 4 années d'expérience est de " + str(cs.calculerSalaire("architecte", 4)))
    # print("Le salaire d'un médecin après 8 années d'expérience est de " + str(cs.calculerSalaire("medecin", 8)))
    # print("Le salaire d'un consultant après 5 années d'expérience est de " + str(cs.calculerSalaire("consultant", 5)))