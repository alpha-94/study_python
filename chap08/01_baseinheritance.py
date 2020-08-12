class Base:
    def __init__(self):
        print(self)
        self.message = "Hello, World"

    def print_message(self):
        print(self.message)

class Derived(Base):  # 상속하고 싶은 부모클래스를 명시
    pass

if __name__ == "__main__":
    base = Base()
    base.print_message()

    derived = Derived()
    derived.print_message()