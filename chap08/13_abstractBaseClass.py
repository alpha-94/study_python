from abc import ABCMeta
from abc import abstractmethod

class AbstractDuck(metaclass=ABCMeta):

    @abstractmethod
    def Quack(self):
        pass


class Duck(AbstractDuck):
    def Quack(self): # 이 메서드 정의 안하면 오류남
        print('[Duck] Quack')


if __name__ == '__main__':

    duck = Duck() # 오버라이딩을 해야함
    duck.Quack()