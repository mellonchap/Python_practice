#부모폴더인 module_example과 형제 폴더인 module_package의 모듈 import
import sys

#방법1
sys.path.append("..")

from module_package.test_package import test_module2

output = test_module2.number_input()
print(test_module2.get_circle_area(output))
print(test_module2.get_circumference(output))