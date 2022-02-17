class Car():
    """
    Car class
    author : Choi
    date : 2022/02/14
    description : class,static,instance method
    """
    # 클래스 변수
    car_count = 0
    price_per_raise = 1.0


    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('id : {}'.format(id(self)))
        print('detail_info : {}, {}'.format(self._company,self._details.get('price')))


    def get_price(self):
        return 'Before price : {} , {}'.format(self._company,self._details.get('price'))

    def get_price_culc(self):
        return "after price : {} , {}".format(self._company,Car.price_per_raise*self._details.get('price'))


    @classmethod
    def raise_price(cls,per):
        if per <= 1:
            print("wrong assign, please code more than 1.0")
        cls.price_per_raise = per
        return 'Succeed! price increased.'



car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})


#인스턴스 메소드를 이용해서 속상값 출력
car1.detail_info()

print(car1.__dict__)

#직접적인 접근 - 변수의 돌발적인 변경을 막기위해 지양함(캡슐화)
print(car1._details.get('price'))

#따라서 직접 print하는 메소드를 주로 만드는 편
print(car1.get_price())
print(car2.get_price())

#클래스 변수를 수정
#이것도 캡슐화를 위해서 클래스 변수를 수정하는 클래스 메소드를 만들자
Car.price_per_raise = 1.2

print(car1.get_price_culc())
print(car2.get_price_culc())

#클래스 메소드
car1.raise_price(1.15)
print(car1.get_price_culc())
print(car2.get_price_culc())
