import unittest
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.runner = Runner("Тест Бегун", 20)
    
    def test_runner_name(self):
        self.assertEqual(self.runner.name, "Тест Бегун")
    
    def test_runner_speed(self):
        self.assertEqual(self.runner.speed, 20)

class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.tournament = Tournament()
        self.runner1 = Runner("Бегун 1", 20)
        self.runner2 = Runner("Бегун 2", 25)
    
    def test_add_runner(self):
        self.tournament.add_runner(self.runner1)
        self.assertEqual(len(self.tournament.runners), 1)
    
    def test_get_winner(self):
        self.tournament.add_runner(self.runner1)
        self.tournament.add_runner(self.runner2)
        winner = self.tournament.get_winner()
        self.assertEqual(winner.name, "Бегун 2") 