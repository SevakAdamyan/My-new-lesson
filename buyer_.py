# Buyer class-ը պետք է ունենա հետևյալ մեթոդները՝
# 1. buy - գնելու է վաճառողից մեքենա։ Լինելու է public method
# 2. return_carr - վերադարձնելու է մեքենան (դրանից բխող բոլոր update-ները պետք է կարատվեն)։ Լինելու է public method
# 3. change_money - ավելացնելու/պակասացնելու է գումարը։ Լինելու է private method
# 4. add_bought_cars - ավելացնելու է գնված մեքենան bought_cars֊ում։
# Պետք է նշվի մեքենայի մոդելը, վաճառողի անուն/ազգանուն/քաղաք, գործարքի ամիս ամսաթիվը  հետևյալ ֆորմատով՝ "տարի-ամիս֊օր"
# 5. print_my_cars - ցույց կտա գնորգի գնված մեքենաները։ Լինելու է public method
from datetime import datetime


from person import Person




class Buyer(Person):

    def __init__(self,  first_name,last_name,city,money=50000):
        super().__init__(first_name,last_name,city)
        self.money = money
        self.spent_money = 0
        self.bought_cars = {}

    def generate_key(self):
        key = 1
        while True:
            if key in list(self.bought_cars.keys()):
                key += 1
            else:
                return key

    def buy(self,car, seller):
        self.add_bought_cars(car,seller)
        self.money -= car.price - car.discount
        self.spent_money += car.price - car.discount



    def return_car(self,car):
        self.bought_cars.pop(car)
        self.money += car.price - car.discount

    def change_money(self,money):
        self.money += money

    def add_bought_cars(self, car, seller):
        key = self.generate_key()
        self.bought_cars[key] = {
            'car': car,
            'date':datetime.now().strftime("%d-%B-%Y"),
            'seller': {
            'name':seller.first_name,
            'lastname':seller.last_name,
            'city':seller.city
           }
        }

    def print_my_cars(self):
        for i in self.bought_cars:
            print(self.bought_cars[i]['car'])









