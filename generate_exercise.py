import argparse
import mathexercises.utils as utils

parser = argparse.ArgumentParser(description='Build math exercise')
parser.add_argument('-N', '--number_of_steps',
                    help='How many steps should the exercise have', default=8, type=int)
parser.add_argument(
    '-m', '--max', help='What is the maximum of addition operations', default=40, type=int)
parser.add_argument(
    '--min', help='What is the minimum for operations', default=0, type=int)
parser.add_argument(
    '-t', '--TeX_template', help='Location and filename of TeX template', default='./template.tex')
parser.add_argument(
    '-T', '--TeX_output', help='Location and filename of TeX output', default='./output/exercise.tex')
args = parser.parse_args()

N = args.number_of_steps

numbers, ops, res = utils.generate_numbers(
    N=N, MAX=args.max, MIN=args.min)

str_res = utils.build_string(numbers, ops)

utils.generate_TeX_file(str_res, res, N, template_filename=args.TeX_template,
                        output_filename=args.TeX_output)

print(str_res)
print(res)
print(N)
