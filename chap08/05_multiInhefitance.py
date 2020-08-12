# 다중 상속
class A:
    pass

class B:
    pass

class C:
    pass

class D(A,B,C):
    pass

##########################################

# 다중 상속시 주의사항 - 죽음의 다이아몬드

class K:
    def method(self):
        print('K')


class L(K):
    def method(self):
        print('L')

class M(K):
    def method(self):
        print('M')

class N(L,M):
    pass

if __name__ == '__main__':
    obj = N()
    obj.method()