import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Usain", speed=10)
        self.andrey = Runner("Andrey", speed=9)
        self.nick = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results):
            print(f"{key}: {cls.all_results[key]}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results.update(results)
        self.assertTrue(results[max(results.keys())] == "Nick")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results.update(results)
        self.assertTrue(results[max(results.keys())] == "Nick")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results.update(results)
        self.assertTrue(results[max(results.keys())] == "Nick")


if __name__ == '__main__':
    unittest.main()
    