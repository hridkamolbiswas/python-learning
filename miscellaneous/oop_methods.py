class Student:

    SCHOOL = "UNIPB"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.email = self.get_email()

    def __str__(self):
        return f"{self.name} with {self.roll} object"


    def __repr__(self):
        return f"{self.name} has roll number {self.roll} with repr"

    def get_email(self):
        self.first = self.name.split()[0]
        try:
            self.last = self.name.split()[1]
        except Exception as e:
            self.last = ""
            #raise IndexError ("please give second name")
        return self.first+"."+self.last+"@gmail.com"+self.SCHOOL

    def set_roll(self, roll):
        self.roll = roll

    @classmethod
    def get_uni(cls):
        #ob = Student("yasemin fonk")
        #print(ob)
        return cls.SCHOOL

    @staticmethod
    def static_mathod():
        # not allowed to sue the self or cls attributes
        return "this is a static method" 

def feature_branch_func:
    print(" iam from feature branch")





ob = Student("hrid Biswas", 200916047)
print(ob)
print(repr(ob))
print(ob.static_mathod())
# print(ob.email)
# #print(ob.get_email())
# print(Student.get_uni())


def summ(x, y):
    return x + y