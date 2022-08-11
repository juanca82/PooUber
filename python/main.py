from car import Car

if __name__ == '__main__':
    print("Hola Mundo")
    car = Car()
    car.license = "AMS584"
    car.driver = "Juan Zapata"
    car.passegenger = 3
    print(vars(car))

    car2 = Car()
    car2.license = "OJK877"
    car2.driver = "Diego Ocampo"
    car2.passegenger = 6
    print((vars(car2)))