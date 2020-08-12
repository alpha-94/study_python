class InstanceVar:
    def __init__(self):
        self.text_list = []

    def add(self, text): # 인스턴스 멤버
        self.text_list.append(text) # 맨 끝(인덱스)에다가 저장

    def print_list(self,index): # 인스턴스 멤버
        print(self.text_list.pop(index))

    def print_all(self):
        print(self.text_list)


if __name__ == '__main__':
    cv1 = InstanceVar()
    cv1.add('1234')
    cv1.add('4567')
    cv1.add('0101')
    cv1.print_all()

    cv2 = InstanceVar()
    cv2.add('a')
    cv2.add('n')
    cv2.add('d')
    cv2.print_all()
