class employee:
    company ="google"
    #constructor -initialize the object
    #_init_-automitacally initialize
    def __init__(self,name,salary,subnit):
        self.name=name
        self.salary=salary
        self.subnit=subnit
        print("employee is created")

    def getsalary(self,signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("good morning abishek")

    @staticmethod
    def time():
        print("the time is 9 am in the morning")

abishek=employee("abishek",100000,"google")
