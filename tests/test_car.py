import os
import sys
import unittest

# add root_path/src to sys.path
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PATH_TO_ADD = os.path.abspath(os.path.join(DIR_PATH, "../src/"))
sys.path.append(PATH_TO_ADD)

# import source code
from project_structure.package1 import module1


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = module1.Car("test")

    def test_drive_from_parking(self):
        self.car.drive(10)
        self.assertEqual(self.car.speed, 10)
        self.assertEqual(self.car.status, "driving")

    def test_drive_from_driving(self):
        self.car.status = "driving"
        self.car.drive(20)
        self.assertAlmostEqual(self.car.speed, 20)

    def test_drive_from_crashed_car_return(self):
        self.car.status = "crashed"
        self.car.drive(15)
        self.assertNotEqual(self.car.speed, 15)
