# import test_package.module_a as a
# import test_package.module_b as b

# from test_package import module_a


# from test_package.module_a import*
# from test_package.module_b import*

from test_package import *

print(module_a.variable_a)
print(module_b.variable_b)