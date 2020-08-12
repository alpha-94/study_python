list = [1,2,3]
for i in list:
    print(i) # 1 2 3


# Iterator 와 순회 가능한 객체

iterator = range(3).__iter__() # 자바 :: 리스트나 헤시셋 이런것들 객체를 꺼내올때

print(iterator.__next__()) # 0
print(iterator.__next__()) # 1
print(iterator.__next__()) # 2
#  print(iterator.__next__()) # StopIteration :: 자바에서는 hasnext 할때 False 리턴

################################################################################

class MyRange: # range() 함수와 같은 일을 하는 클래스 정의
    def __init__(self,start,end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration() # 자바 :: throw


if __name__ == '__main__':
    for i in MyRange(0,5): # iter 주소값 반환 next 호출
        print(i)
