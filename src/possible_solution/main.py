from src.possible_solution.engine import Engine
from src.possible_solution.brand import Brand, BrandName
from src.possible_solution.person import Person

tim = Person("Tim", 28)

tim.buy_car(Brand(BrandName.suzuki), Engine(20), "Turquoise", True)
tim_insurance_cost = tim.apply_insurance()
tim.car.drive_to("Alkmaar")
