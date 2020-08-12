# 데이터 속성(Field) 상속(명시적으로 표현해 주어야 함)

'''
class A:
    def __init__(self):
        print('A.__init__()')
        self.message = 'Hello'

class B(A):
    def __init__(self): # 부모 생성자를 호출해 주지 않음 (super 의 개념이 없음)
        print('B.__init__()')


if __name__ == '__main__':
    obj = B()

    #print(obj.message)
    # error 사유 :: message 는 A 의 __init__() 메서드 안에서 생성되는데, B의 인스턴스를
    #              생성하면서 B의 __init__()만 호출하고, A의 __init__()를 호출하지 않는다.


'''


# super() :: 부모 클래스의 객체 역할을 하는 프록시(proxy)를 반환하는 내장 함수
class A:
    def __init__(self):
        print('A.__init__()')
        self.message = 'Hello'

class B(A):
    def __init__(self):
        super().__init__() #A.__init__(self) #  명시적으로 표현
        print('B.__init__()')

        print('self.message is  ' + self.message)


if __name__ == '__main__':
    obj = B()

    print(obj.message)