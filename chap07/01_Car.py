class Car:
    def __init__(self):
        self.color = 0xFF0000 # 차량 색상
        self.wheel_size = 16 # 바퀴의 크기
        self.displacement = 2000 # 배기량

    def forward(self): # 전진
        pass

    def backward(self): # 후진
        pass

    def turn_left(self): # 좌회전
        pass

    def turn_rignt(self): # 우회전
        pass

if __name__ == '__main__':
    car = Car() # Car 클래스 객체 car 생성

    print('0x{:02X}'.format(car.color))
    # {:02X} -> 정수를 2자리 16진수로 출력하되, 2자리가 안되면 빈 자리를 0으로 채워서 출력


    car.forward()
    car.backward()
    car.turn_left()
    car.turn_rignt()