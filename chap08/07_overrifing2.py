class Car:
    def ride(self):
        print('Run')

class Flying(Car):
    def ride(self):
        super().ride()
        print('Fly')