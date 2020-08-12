# 오버라이딩

class A:
    def method(self):
        print('A')

class B(A):
    def method(self):
        print('B')

class C(A):
    def method(self):
        print('C')


if __name__ == '__main__':
    A().method()
    B().method()
    C().method()
