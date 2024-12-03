import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем TestSuite и loader
suite = unittest.TestSuite()
loader = unittest.TestLoader()

# Используем loader.loadTestsFromTestCase() вместо makeSuite
suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

if __name__ == '__main__':
    # Создаем TextTestRunner с verbosity=2
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite) 