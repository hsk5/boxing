
#데이터 타입들도 사실은 전부 클래스이다.

print(10)
print(int)
n  = 10
print(type(n))

#따라서 내부에 스페셜메소드들이 있다.
#dir()을 통해서 안에 가지고 있는 상속 포함 모든 메소드를 보여줌
#print(dir(n))

print(n + 10)
print(n.__add__(10))

#단 이 메소드를 사용할때는 매개변수 타입이 정해져 잇어서 다른 타입을 넣을경우 안된다.
print(n + 0.5)
print(n.__add__(0.5))

#클래스 실습
#클래스끼리 더할수는 없지만 매직매소드를 수정하여서 클래스끼리 더할수도 있다.
#__add__의 경우 +로 랩핑되어서 그냥 클래스 + 클래스 하면 자동 __add__가 호출된다.
class Fruit:
    def __init__(self,name,price):
        self._name  = name
        self._price = price

    def __str__(self):
        return 'class info : {} , {}'.format(self._name,self._price) 


    def __add__(self,x):
        return self._price + x._price

    def __le__(self,x):
        print("call magic method! __le__")
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self,x):
        print("call magic method! __ge__")
        if self._price >= x._price:
            return True
        else:
            return False
    def __sub__(self,x):
        return self._price - x._price
    

s1 = Fruit('orangebanana', 15)
s2 = Fruit('apple', 10)

print(s1.__str__())
print(s1 + s2)
print(s1 <= s2)
print(s1 - s2)