from urllib import request

target = request.urlopen("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Jo_Yuri_%28%EC%A1%B0%EC%9C%A0%EB%A6%AC%29_of_IZONE_%28%EC%95%84%EC%9D%B4%EC%A6%88%EC%9B%90%29_in_Gaon_chart_Kpop_Award_2019.png/220px-Jo_Yuri_%28%EC%A1%B0%EC%9C%A0%EB%A6%AC%29_of_IZONE_%28%EC%95%84%EC%9D%B4%EC%A6%88%EC%9B%90%29_in_Gaon_chart_Kpop_Award_2019.png")
output = target.read()
# print(output)


file = open("output.png", "wb")
file.write(output)
file.close()