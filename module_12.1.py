import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.runner = Runner("TestRunner")
        self.runner.distance = 0

    def test_run(self):
        initial_distance = self.runner.distance
        self.runner.run()
        self.assertEqual(self.runner.distance, initial_distance + 10)

    def test_walk(self):
        initial_distance = self.runner.distance
        self.runner.walk()
        self.assertEqual(self.runner.distance, initial_distance + 5)

    def test_challenge(self):
        self.runner1 = Runner("TestRunner1")
        self.runner2 = Runner("TestRunner2")
        for _ in range(10):
            self.runner1.run()
            self.runner2.walk()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)


if __name__ == '__main__':
    unittest.main()