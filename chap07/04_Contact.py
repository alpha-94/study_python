class ContactInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print('{0}:{1}'.format(self.name, self.email))


if __name__ == '__main__':
    con1 = ContactInfo('홍길동','abc@aaa.aaa')
    con1.print_info()

    con2 = ContactInfo('이순신','abc@bbb.bbb')
    con2.print_info()