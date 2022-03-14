from os import sep

def create_student(name, korean, math, english, science):
    return{
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }
   
def get_sum(st):        
    return st["korean"]+st["math"]+st["english"]+st["science"]


def get_avg(st):
    avg = get_sum(st)/4
    return avg

def st_print(st):
    return ("{}\t{}\t{}".format(st["name"],get_sum(st), get_avg(st)))

students = [
    create_student("윤인성", 87, 98, 88,95),
    create_student("연하진", 92, 98, 96,98),
    create_student("구지연", 76, 96, 94,90),
    create_student("나선주", 98, 92, 96,92),
    create_student("윤아린", 95, 98, 98,98),
    create_student("윤명월", 64, 88, 92,92)
]

print("이름","총점","평균", sep="\t")
for st in students:
    print(st_print(st))
