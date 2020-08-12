class Calculator:

    @staticmethod
    def plus(a, b):
        print('plus :: '+'{0} + {1}'.format(a,b))
        return a + b

    @staticmethod
    def minus(a, b):
        print('minus :: ' + '{0} - {1}'.format(a, b))
        return a - b

    @staticmethod
    def multiply(a, b):
        print('multiply :: ' + '{0} * {1}'.format(a, b))
        return a * b

    @staticmethod
    def divide(a, b):
        print('divide :: ' + '{0} / {1}'.format(a, b))
        print('**뒷값이 0이 되면 0으로 출력됩니다.')
        if b == 0:
            return b

        else:
            return a / b

if __name__ == '__main__':
    Calculator.plus(1,2)