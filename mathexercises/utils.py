import numpy as np
import jinja2
import os


OPS_NOTATION = {
    np.subtract: '-',
    np.add:      '+',
    np.multiply: '*'
}


def generate_numbers(N=8, MIN=0, MAX=50, MUL_MIN=2, MUL_MAX=4):
    numbers = []
    ops = []
    n = np.random.randint(MIN, MAX)
    res = n
    numbers.append(n)
    for i in range(N):
        op = np.random.choice([np.add, np.subtract, np.multiply], size=1)[0]
        ops.append(op)
        if op == np.subtract:
            n = np.random.randint(MIN, res)
        elif op == np.multiply:
            n = np.random.randint(MUL_MIN, MUL_MAX)
        else:
            n = np.random.randint(MIN, MAX)
        res = op(res, n)
        numbers.append(n)
    numbers = [str(x) for x in numbers]
    return (numbers, ops, res)


def build_string(numbers, ops):
    str_res = numbers[0] + OPS_NOTATION[ops[0]] + numbers[1] + ','
    for n, o in zip(numbers[2:], ops[1:]):
        str_res += OPS_NOTATION[o] + n + ','
    return str_res[:-1]


def generate_TeX_file(numbers_str, res,  N,
                      template_filename='template.tex',
                      output_filename='test.tex'):
    latex_jinja_env = jinja2.Environment(
        block_start_string='\BLOCK{',
        block_end_string='}',
        variable_start_string='\VAR{',
        variable_end_string='}',
        comment_start_string='\#{',
        comment_end_string='}',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.abspath('.'))
    )
    template = latex_jinja_env.get_template(template_filename)
    with open(output_filename, 'w') as f:
        f.write(template.render(num_list=numbers_str, res=res, N=N))
