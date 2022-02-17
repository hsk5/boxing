class Vector:
    """
    2022/02/16
    author : youngwoochoi
    making vector class
    """
    
    def __init__(self,*args):
        """
        example : Vector(1,2)
        """
        if len(args) == 0:
            self._x,self._y = 0,0
        else:
            self._x,self._y = args 

    def __repr__(self):
        '''Returns the vector infomations'''
        return 'Vector(%r, %r)' % (self._x, self._y)


    def __add__(self,x):
        return self._x + x._x,self._y + x._y

    def __sub__(self,x):
        return self._x - x._x,self._y - x._y

    def __mul__(self,x):
        return self._x * x._x,self._y * x._y

    

    

#*args 여러개의 매개변수를 쓸때 쓰임
#튜플형태로 값이 들어가서 리턴도 튜플형태임




v1 = Vector(1,1)
v2 = Vector(10,3)

# print(v1)
# print("({},{})".format(v1._x,v1._y))
# print(v1 * v2)
# print(Vector.__init__.__doc__)
print(v1.__repr__)