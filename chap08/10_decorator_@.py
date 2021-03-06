#  @decorator

class MyDecorator:
    def __init__(self, f): # __init__() 메서드의 매개변수를 통해 함수를 받아들이고 데이터 속성에 저장해둠
        print('Initializing MyDecorator...')
        self.func = f # MyDecorator 의 func 데이터 속성이 print_hello 를 받아둠

    def __call__(self):
        print('Begin : {0}'.format(self.func.__name__))

        self.func() # __call__() 메서드가 호출되면 생성자에서 저장해둔 함수(데이터 속성) 를 호출 .

        print('End : {0}'.format(self.func.__name__))


@MyDecorator
def print_hello(): # call 선언 -> 함수 선언 -> 데코레이터 선언 하면 끝!
    print('hello!')


if __name__ == '__main__':

    print_hello()