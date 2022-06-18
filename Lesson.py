class WorkWithName:
    def __init__(self,name):
        print('init is worked')
        if isinstance(name,str):

            self.name = name
        else:
            raise ValueError('not correct value')
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,a):
        print("setter is worked")
        if isinstance(a, str):
            self._name = a
        else:
            raise ValueError('not correct value')

    def name_to_list(self):
        return list(self._name)

    def reverse_name(self):
        rev_name = ''
        for i in range(len(self._name)):
            rev_name += self._name[-i - 1]
        return rev_name

    def skip_chr(self,ch):
        if isinstance(ch,str):
            st = ''
            for i in self._name:
                if i != ch:
                    st += i
            return st
        else:
            raise ValueError('not correct value')
obj = WorkWithName("Davit")
obj.name = 'aram'
print(obj.name_to_list())
print(obj.reverse_name())
print(obj.skip_chr("a "))
class CarMarket:
    carpark = {}

    def add_car(self, car: Car, seller: Seller):
        CarMarket.carpark[seller.first_name] = {'model': car.model,
                                                'price': car.price,
                                                'discount': car.discount}

    def set_discount(self, seller, dis):
        CarMarket.carpark[seller]['discount'] = dis

    def get_sold_car_history(self):
        pass

    def return_car(self, seller: Seller, car: Car):
        pass

    def get_seller_available_cars(self, seller: Seller):
        for i in CarMarket.carpark:
            if i == seller.first_name:
                print(CarMarket.carpark[i])

    def get_car_available_discount(self, seller: Seller):
        print(CarMarket.carpark[seller.first_name]['discount'])

