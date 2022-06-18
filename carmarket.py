# CarMarket class-ը պետք է ունենա հետևյալ մեթոդները՝
# 1․  add_car - ավելացնում է նոր մեքենա մեքենաների ցուցակ։
# 2. remove_car - ջնջելու է մեքենա/մեքենաներ։ Լինելու է private method
# 3. set_discount - զեղչ է դնելու մեքենայի/մեքենաներ վրա։ Լինելու է protected method
# 4. get_sold_car_history- վերադարձնելու է կոնրետ վաճառողի վաճառած մեքենաները։
# Յուրաքանչյուր մեքենայի գինը, գործարքի օր/ամիս/ամսաթիվը, գնորդի անունը/ազգանուն/քաղաք,
# եթե մեքենան ունեցել է զեղչ, ապա նաև զեղչը, եթե մեքենայի վերադարձ է կարարվել, ապա նաև վերադարձի մասին ինֆոն։
# Լինելու է private method
# 5. return_car - մեքենայի վերադարձ գնորդի կողմից, այս դեպքում վաճարքի պատմություն մեջ՝ վերադարձրած մեքենայի համար գրվում է,
# որ այն վերադարձվել է և վերադարձի պատճառը։ Լինելու է private method
# 6. get_seller_available_cars - վերադարձնելու է Seller-ի մոտ ներկա պահին վաճառվող մեքենաները։ Լինելու է protected method
# 7․ get_car_available_discount -  կվերադարձնի մեքենայի համար հասանելի զեղչը:
from datetime import datetime

from car import Car



class CarMarket:
    carpark = {}

    @staticmethod
    def generate_key(seller):
        key = 1
        while True:
            if  CarMarket.carpark.get(seller.first_name):
               if key in list(CarMarket.carpark.get(seller.first_name).keys()):
                key += 1
               else:
                   return key

            return key
    @classmethod
    def add_car(cls,car, seller):
        key = cls.generate_key(seller)

        car  = {key:{
            "car":car,
            'status':None
        }}
        CarMarket.carpark.update({seller.first_name:car})


    def remove_car(cls,car,seller):
        if cls.carpark.get(seller.first_name):
            for i in cls.carpark.get(seller.first_name):
                if cls.carpark.get(seller.first_name)[i] == car:
                    cls.carpark.get(seller.first_name).pop(i)
                    break

        else:
            print('not seller in carmarket')

    def set_discount(cls, discount,car):
        for i in cls.carpark:
            for j in cls.carpark[i]:
               if cls.carpark[i][j] == car:
                   car.discount = discount


    def get_sold_car_history(self, car, buyer,seller):

        self.seller.first_name = {
            'car': car,
            'date': datetime.now().strftime("%d-%B-%Y"),
            'seller': {
                'name': buyer.first_name,
                'lastname': buyer.last_name,
                'city': buyer.city
            }
        }


    def get_seller_available_cars(self):
        return self.carpark







