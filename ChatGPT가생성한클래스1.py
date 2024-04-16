class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print("ID:", self.id)
        print("Name:", self.name)


class Manager(Person):
    def __init__(self, id, name, title):
        #부모 클래스를 지청 
        super().__init__(id, name)
        self.title = title


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill


# 테스트 코드(진입점: main())
if __name__ == "__main__":
    # Person 클래스 테스트
    print("Person 클래스 테스트:")
    person1 = Person(1, "Alice")
    person1.printInfo()
    print()

    # Manager 클래스 테스트
    print("Manager 클래스 테스트:")
    manager1 = Manager(2, "Bob", "Senior Manager")
    manager1.printInfo()
    print("Title:", manager1.title)
    print()

    # Employee 클래스 테스트
    print("Employee 클래스 테스트:")
    employee1 = Employee(3, "Charlie", "Python Developer")
    employee1.printInfo()
    print("Skill:", employee1.skill)
