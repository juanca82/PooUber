class Main {
    public static void main(String[] args) {
        Car car = new Car("AMQ123", new Account("Camilo Ocampo", "55487703L" ));
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car("FGO587", new Account("Diego Ocampo", "69523655N"));
        car.passenger = 8;
        car2.printDataCar();
  
    }
} 