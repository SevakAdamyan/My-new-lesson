class Person:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age


    def conceive(self):
        if self.sex == 'woman' and self.age > 18:
            print('SHe can have baby')
        else:
            print('It is malignant')



    def sound(self):
        if self.sex == 'man':
           print('have a surly sound')
        else:
            print('have a limp')


davit = Person('davit', 'man', 20)
anna = Person('Anna', 'woman', 25)

print(anna.name)
anna.conceive()
anna.sound()
