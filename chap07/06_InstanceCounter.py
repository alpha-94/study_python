class InstanceCounter:
    count = 0

    def __init__(self):
        InstanceCounter.count += 1 # 인스턴스 생성 시 누적

    @classmethod
    def print_instance_count(cls):
        print(cls)
        print(cls.count)


if __name__ == '__main__':
    InstanceCounter.print_instance_count()
    InstanceCounter()
    InstanceCounter.print_instance_count()
    InstanceCounter()
    InstanceCounter.print_instance_count()
