"""
Main module with class car

Attributes:
    NUMBER_OF_CARS (int): number of available cars

"""

# absolute import
# from project_structure.package1 import module2
# from project_structure.package1.subpackage1 import module3
# from project_structure.package2 import module4

# relative import
# from . import module2
# from .subpackage1 import module3
# from ..package2 import module4


NUMBER_OF_CARS = 1


class Car:
    """
    Class for cars

    Args:
        model (str): name of car model

    Attributes:
        model (str): name of car model
        status (str): parking, driving or crashed. Default=parking
        speed (int): speed of the car. Default = 0

    """

    def __init__(self, model):
        self.model = model
        self.status = "parking"
        self.speed = 0

    def drive(self, speed):
        """
        Function to start the car with desired speed.

        Args:
            speed (int): speed of the car. How fast the car will drive.

        Returns:
            None

        """

        if self.status == "parking":
            self.status = "driving"
            self.speed = speed
        elif self.status == "driving":
            self.speed = speed
        else:
            print("car crashed")

    def get_speed(self):
        """
        Function to determines speed of the car.

        Returns:
            int : speed of the car

        """

        return self.speed
