import unittest
from equipes import distribuir

class EquipesTest(unittest.TestCase):
    def test_cada_pessoa_uma_vez_e_tamanhos(self):
        for n in range(1,30):
            nomes=[f'Pessoa {i}' for i in range(n)]
            for k in range(1,n+1):
                e=distribuir(nomes,k,42)
                self.assertEqual(sorted(x for g in e for x in g),sorted(nomes))
                self.assertEqual(len(e),k)
                self.assertLessEqual(max(map(len,e))-min(map(len,e)),1)
                self.assertEqual(nomes,[f'Pessoa {i}' for i in range(n)])
    def test_semente(self):
        nomes=['A','B','C','D','E']
        self.assertEqual(distribuir(nomes,2,7),distribuir(nomes,2,7))
    def test_duplicatas_normalizadas(self):
        for nomes in [[' Ana ','ANA'],['José','Jose\u0301'],['Ana  Maria','Ana Maria']]:
            with self.assertRaises(ValueError): distribuir(nomes,1)
    def test_invalidos(self):
        for nomes,k in [([],1),(['A'],0),(['A'],2),(['A'],True),([''],1),([3],1),({},1)]:
            with self.assertRaises(ValueError): distribuir(nomes,k)

if __name__ == '__main__': unittest.main()
