import mathexercises.utils as utils

N = 5

numbers, ops, res = utils.generate_numbers(N=N)

str_res = utils.build_string(numbers, ops)

utils.generate_TeX_file(str_res, res, N)

print(numbers)
print(ops)
print(res)
print(str_res)
