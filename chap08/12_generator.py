def generator(): # 복귀하지 않고 값만 반환
    yield 0 # 하나의 자료형으로 생각 __iter__호출된 것 처럼
    yield 1
    yield 2
    yield 3

iterator = generator()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
## print(iterator.__next__()) # StopIteration

############################################
# 위와 동일 기능의 정의
def YourRange(start, end):
    current = start
    while current <end:
        yield current
        current += 1

    return

for i in YourRange(0,4):
    print(i)