class ClassVar:
    text_list = [] # 생성자 외부에 적용된 필드 -> static ( 클래스 맴버 :; 인스턴스가 공유하는 맴버로 사용)

    def add(self, text): # 인스턴스 멤버
        self.text_list.append(text) # 맨 끝(인덱스)에다가 저장

    def print_list(self,index): # 인스턴스 멤버
        print(self.text_list.pop(index))

    def print_all(self):
        print(self.text_list)

if __name__ == '__main__':
    cv = ClassVar()
    cv.add('1234')
    cv.add('4567')
    cv.add('0101')

    cv.print_all()

    cv2 = ClassVar()
    cv2.add('a')
    cv2.add('n')
    cv2.add('d')

    cv2.print_all()