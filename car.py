class Car:
    def __init__(self, model, year, engine_volume, price, mileage):
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.num_wheels = 4

    def description(self):
        return (f"Модель: {self.model}, Год выпуска: {self.year}, Объем двигателя: {self.engine_volume} л, " 
                f"Цена: {self.price} рублей, Пробег: {self.mileage} км, Количество колес: {self.num_wheels}")

car1 = Car("Toyota", 2020, 2.0, 1600000, 30000)
print("Автомобиль 1:")
print(car1.description())

class Truck(Car):
    def __init__(self, model, year, engine_volume, price, mileage):
        super().__init__(model, year, engine_volume, price, mileage)
        self.num_wheels = 8

truck1 = Truck("Volvo", 2018, 3.5, 700000, 150000)
print("\nГрузовик 1:")
print(truck1.description())