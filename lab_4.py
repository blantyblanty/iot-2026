class Airplane:

    def __init__(self, fuel_capacity=0.0, name="Невідомо", passengers=0,
                 year=0, country="Невідомо"):
        self.__fuel_capacity = fuel_capacity
        self.__name = name
        self.__passengers = passengers

        self.year = year
        self.country = country

    def get_fuel_capacity(self):
        return self.__fuel_capacity

    def get_name(self):
        return self.__name    

    def get_passengers(self):
        return self.__passengers

    def set_fuel_capacity(self, fuel_capacity):
        self.__fuel_capacity = fuel_capacity

    def set_name(self, name):
        self.__name = name

    def set_passengers(self, passengers):
        self.__passengers = passengers

    def __str__(self):
        return (f"Літак \"{self.__name}\": баки {self.__fuel_capacity} л, "
                f"пасажирів {self.__passengers}, "
                f"рік {self.year}, країна {self.country}")

    def __repr__(self):
        return (f"Airplane(fuel_capacity={self.__fuel_capacity!r}, "
                f"name={self.__name!r}, passengers={self.__passengers!r}, "
                f"year={self.year!r}, country={self.country!r})")

    def __del__(self):
        print(f"Об'єкт \"{self.__name}\" видалено")


def main():
    plane1 = Airplane()
    plane2 = Airplane(23860, "Boeing 737", 189, 2015, "США")
    plane3 = Airplane(320000, "Airbus A380", 555, 2010, "Франція")
     
    plane4 = Airplane(name="bbb")
    print(plane4.get_name())
   
    for plane in (plane1, plane2, plane3):
        print("Назва:             ", plane.get_name())
        print("Об'єм баків (л):   ", plane.get_fuel_capacity())
        print("Пасажирів:         ", plane.get_passengers())
        print("Рік випуску:       ", plane.year)
        print("Країна:            ", plane.country)
        print("str :", str(plane))
        print("repr:", repr(plane))
        print("-" * 40)


if __name__ == "__main__":
    main()