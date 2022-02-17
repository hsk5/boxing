class Car():
    """
    Car class
    author : Choi
    date : 2022/02/14
    """
    # 클래스 변수
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('id : {}'.format(id(self)))
        print('detail_info : {}, {}'.format(self._company,self._details.get('price')))

    def __del__(self):
        print('del?')
        Car.car_count -= 1
        
    

car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})


#인스턴스 메소드에서는 첫번째 변수가 self이다.

#id확인 id()
#객체의 고유한 값을 가지고 있다. 따라서 각각의 고유한 접근을 위해 self가 필요하다.
print(id(car1))
print(id(car2))
print(id(car3))

#id가 달라서 false
#따라서 self는 자기 자신의 고유한 변수에 접근하기 위한 것
print(car1._company == car2._company)
print(car1 is car2) 


#dir()
#object객체를 상속받아서 가지고있는 모든 속성을 보여줌(내가 만든 변수포함)
print(dir(car1))
print(dir(car2))

#__dict__
#상속받은거 말고 내가 만든 속성만 나옴
print(car1.__dict__)

print(car2.__dict__)


#__doc__
#doctring
#클래스 정의에 적어놓은 설명을 볼 수 있음 

print(car1.__doc__)


car1.detail_info()
car2.detail_info()
car3.detail_info()



#__class__
#어떤 클래스로 만들어 졌는지!
#이건 같은 클래스이기 때문에 true가 나온다.
print(car1.__class__ is car2.__class__)


#에러
#원래 self가 필요한데 쓰지않음
#Car.detail_info()
Car.detail_info(car1)


#클래스 변수
#클래스 선언에서 선언하고 모든 객체에서 공통으로 사용하는 변수
#일반적으로 인스턴수 변수는 앞에 _을 붙이고 클래스 변수는 안붙힌다.
#인스턴스에서 호출시 클래스.클래스변수명 이렇게 써야한다.

#__dict__로 하면 인스턴스 속성만 나옴
print(car1.__dict__)
print(car1.car_count)

del car2
print(car1.car_count)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
# 먼저 인스턴스 생성자에서 검색했는데 있으면 얘를 리턴하고 없으면 상위로 가면서 검색한다.
