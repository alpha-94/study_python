class YourClass:
    pass

class MyClass:
    def __init__(self):
        self.message = "hello"

    def some_method(self):
        print(self.message)


obj = MyClass()
obj.some_method()

#############################################
class HasPrivate:
    def __init__(self):
        self.public = "Public."
        self.__private = "Private."#별도 키워드 없으나, 변수의 이름을 지정할 때 __를 붙여 정보은닉 구분
        self.__public__ = "__public_"#뒤에 언더바 __를 다시 붙이면 public으로 다시 돌아감

    def print_from_internal(self):
        print(self.public)
        print(self.__private)

if __name__ == '__main__':
    obj = HasPrivate()
    obj.print_from_internal()
    #클래스를 불러오면 public, private 둘 다 불러오기 가능

    print(obj.public) # 불러오기 가능
    #print(obj.__private) #error - private 변수 접근 불가능. 'HasPrivate' object has no attribute '__private'
    # 변수로 지정해서 불러오기 하면 에러 발생.

    print(obj.__public__)