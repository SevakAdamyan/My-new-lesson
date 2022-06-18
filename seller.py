# Seller class-ը պետք է ունենա հետևյալ մեթոդները՝
# 1․  sell - վաճառելու է մեքենան: Լինելու է public method
# 2. change_money - ավելացնելու/պակասացնելու է գումարը։ Լինելու է private method
# 3. return_car - ընդունելու է վերադարձի մեքենան։ Այստեղ պետք է նվազի վաճառողի գումարը, ավլանա գնորդի գումարը,
# CarMarket֊ում փոխվի մեքենայի ստատւսը (պետք է գրվի վերադառձի մասին ինֆօ)։ Լինելու է public method
# 4. get_available_cars - CarMarket֊ից (get_seller_available_cars) կվերցի կոնկրետ Seller֊ի հասանելի մեքենաների ցուցակը։
# Լինելու է protected method
# 5. check_discount - կստուգի արդյոք գնորդի մեքենայի համար կա զեղչ, թե ոչ։ Լինելու է protected method
# 6. add_sold_car - կավեալցնի վաճառված մեքենան Seller֊ի sold_cars֊ում։ Պետք է նշվի մեքենայի մոդելը,
# գնորդի անուն/ազգանուն/քաղաք, գործարքի ամիս ամսաթիվը  հետևյալ ֆորմատով՝ "տարի-ամիս֊օր"
from datetime import datetime


from car import Car
from carmarket import CarMarket
from person import Person


class Seller(Person):
    def __init__(self, first_name, last_name, city, car_park, money=50000):
        super().__init__(first_name, last_name, city)
        self.money = money
        self.car_park = car_park.get(self.first_name)
        self.sold_cars = {}

    @staticmethod
    def generate_key(carpark, name):
        key = 1
        while True:
            if key in list(carpark[name].keys()):
                key += 1
            else:
                return key

    def sell(self, car: Car):
        for i in self.car_park:
            if self.car_park[i] == car:
                self.car_park.pop(i)

                money = car.price - car.discount
                self.change_money(money)
                break
        else:
            print('not available car ')

    def change_money(self, money, car_sell=True):
        if car_sell:
            self.money += money
        else:
            self.money -= money

    def return_car(self, car: Car, buyer, carpark):
        status = 'returned car'
        cars = carpark[self.first_name]
        self.money -= car.price - car.discount
        buyer.money += car.price - car.discount
        key = self.generate_key(carpark, self.first_name)
        carpark[self.first_name][key] = {
            'car': car,
            'status': status
        }

    def get_available_cars(self):

        return self.car_park

    @staticmethod
    def check_discount(car):
        return car.discount

    def sold_bought_cars(self, car, buyer):
        key = self.generate_key(self.car_park)
        self.sold_cars[key] = {
            'car': car,
            'date': datetime.now().strftime("%d-%B-%Y"),
            'seller': {
                'name': buyer.first_name,
                'lastname': buyer.last_name,
                'city': buyer.city
            }
        }



