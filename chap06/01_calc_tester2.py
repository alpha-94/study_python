# 따로 import하기 - 방법1
# from calculator import plus
# from calculator import minus

# 한번에 import하기 - 방법2
#from calculator import plus, minus  # 콤마(,)를 이용해서 연속적으로 여러 함수(변수) 선언 가능.

# 모든 기능을 가져다 사용 - 방법3
from calculator import *

result = plus(10,5)
print(result)

result = minus(10,5)
print(result)


