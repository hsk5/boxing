#튜플을 이용하여서 두 점 사이의 거리 계산하기

a = (1.0,3.0)
b = (1.5,4.5)

from math import sqrt
#인덱스를 이용해서 튜플의 값에 접근해서 구하기
#하지만 이는 튜플의 정확한 인덱스를 알아야 해서 좋은 방법이 아니다.``
len_l = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

print(len_l)
print(2^2)


#namedtuple을 사용하기 위해서 우선 라이브러리 필요
#선언할 튜플 이름 = namedtuple('튜플이름','튜플안에 키의 이름을 띄어쓰기로 구분함')
#튜플 객체이름    = 위에서 선언한 튜플이름(*인수)
from collections import namedtuple

Point = namedtuple('point', 'x y')
pt3   = Point(1.0,3.0)
pt4   = Point(1.5,4.5)

len_l2 = sqrt((pt3.x - pt4.x)**2 + (pt3.y - pt4.y)**2)
print(len_l2)
print(len_l ==len_l2 )

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default=False

# 출력
print(Point1, Point2, Point3, Point4)

#딕셔너리를 namedtuple로 만들기
#named tuple클래스(**딕셔너리명)
#**를 쓰면 키가 호출된다.

di = {'x' : 12,'y': 15}

p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**di)

print(p5.x,p5.y)

# Unpacking
# 그냥 변수에 객체를 할당하면 된다.
x, y = p3
x,y = p5

# 네임드 튜플 메소드

temp = [52, 38] 

# _make() : 새로운 객체 생성
# 리스트를 네임드 튜플로 만드는 메소드
p4 = Point1._make(temp)

print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
print(p1._asdict(), p4._asdict())




#실습 - a b c d 4개의 반에 각각 20명의 학생들
#키 = 반,이름 >> 2개의 키가 있음!!
#키를 rank와 번호로
#(a,10) 이런식으로 표현

#처음
#얘는 오류남 field 이름은 읽을 수 있는 키여야 하는데 숫자가 나와서
#clses = namedtuple("clses", "1 2 3 4 5 6 7 8 9 10 11 12 131 14 15 16 17 18 19 20")


#답안
classes = namedtuple('classes', ['rank','numbers'])
rank = 'a b c d'.split()
numbers = [str(i) for i in range(1,21)]

classes_1 = [classes(i,j) for i in rank for j in numbers]



print(classes_1)


# 추천
students2 = [Classes(rank, number) 
                    for rank in 'A B C D'.split() 
                        for number in [str(n) 
                            for n in range(1,21)]]