# Ունենալու ենք Person superclass: Person֊ից ժառանգելու են 2 հատ` Buyer և Seller class-ները։
# Person-ը կունենա name, surname, city ատրիբուտները:
# Buyer-ը կունենա money, spent_money և bought_cars ատրիբուտները։
# Buyer-ի money-ին կփոխանցեք կամայական արժեք` Buyer օբյեկտի ստեղծման պահին,
# իսկ spent_money-ը պետք է ունենա 0 սկզբնական արժեք (այս ատրիբուտը ցույց կտա գնորդի ծախսած գումարը)։

class Person:
    def __init__(self,first_name,last_name,city):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city




