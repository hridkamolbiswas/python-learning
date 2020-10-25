from typing import List
class Student:

    SCHOOL_NAME: str = "RGHS"

    def __init__(self,name, age):
        self.name: str = name
        self.age: int = age
        self.seat_number:  list[int] = []
        self.parents: dict[str, str] ={'mother':'m', 'father':'f'}

    def show_info(self):
        print(self.name, self.age, self.SCHOOL_NAME, self.parents['father'])

    def get_row(self):
        return self.seat_number[0]

    def get_col(self):
        return self.seat_number[1]

    def set_seat_number(self,x,y):
        self.seat_number.append(x)
        self.seat_number.append(y)

    def _private_method(self):
        return 5

    def set_age(self,value):
        self.__setattr__("age",value)

if __name__=='__main__':
    ob = Student('student',15)
    ob.set_seat_number(10,'hrid')
    print(ob.get_row())
    print(ob.get_col())
    ob.show_info()
    print(ob.name)
    getattr(ob,"name")
    print(dir(ob))
    print(ob.__class__)
    ob.__setattr__("age",500)
    ob.show_info()
    ob.set_age(1000)
    ob.show_info()
    
   
