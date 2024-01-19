import unittest

from tire.octoprime import Octoprime


class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [0.9, 0.5, 1.2, 1]
        tire = Octoprime(sensors)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensors = [0.8, 0.5, 0.2, 0.1]
        tire = Octoprime(sensors)
        self.assertFalse(tire.needs_service())