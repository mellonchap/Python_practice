
class Student:
    def __init__(self, name, korean, math, english, science):        
        self.name = name,
        self.korean=korean,
        self.math=math,
        self.english=english,
        self.science=science
    

students = [
    Student("윤인성", 87, 98, 88,95),
    Student("연하진", 92, 98, 96,98),
    Student("구지연", 76, 96, 94,90),
    Student("나선주", 98, 92, 96,92),
    Student("윤아린", 95, 98, 98,98),
    Student("윤명월", 64, 88, 92,92)
]
for i in range(6):
    print(students[i].name)