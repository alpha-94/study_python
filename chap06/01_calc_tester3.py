# 주로 추천하는 방법 !!
# import chap06.calculator as c  : 이렇게 패키지명까지 붙이면 빨간 밑줄이 나타나지 않음.
import calculator as c # 기본 모듈에 새이름 부여 사용 가능.

# chap06.calculatordmfh 붙여야 빨간 밑줄이 없음
# 그러나 같은 폴더 위치에 있을 때는 모듈 이름만으로 가능.
result = c.plus(10,5)
print(result)

result = c.minus(10,5)
print(result)

result = c.multiply(10,5)
print(result)

result = c.divide(10,5)
print(result)