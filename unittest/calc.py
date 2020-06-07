


class Calculator:

    def add(self, x, y):
        try:
            return x + y
        except TypeError as e:
            print(e)


    def minus(self, x, y):
        try:
            return x - y
        except TypeError as e:
            print(e)


    def multi(self, x, y):
        try:
            return x * y
        except TypeError as e:
            print(e)

    def div(self, x, y):
        try:
            return x / y
        except (TypeError, ZeroDivisionError) as e:
            print(e)



if __name__=='__main__':
    ob = Calculator()

    print(ob.add(5,0)) 
    print(ob.div(5,0)) 
    print('hello')