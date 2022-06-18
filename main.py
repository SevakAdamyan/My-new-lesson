from buyer_ import Buyer
from car import Car
from carmarket import CarMarket
from seller import Seller

if __name__ == '__main__':
    carpark = CarMarket.carpark

    seller_1 = Seller('aram', 'shahbazyan', 'yerevan', carpark)
    carmarket = CarMarket
    car_1 = Car('BMW', 5000, 1000)
    print(carpark)
    buyer_1 = Buyer('meliq', 'harutyunyan', 'yerevan')
    carmarket.add_car(car_1,seller_1)
    print(seller_1.get_available_cars())


