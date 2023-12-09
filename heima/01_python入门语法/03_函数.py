"""
def 函数名(传入参数)
    函数体
    return 返回值
"""


def my_len(data):
    print(f"data={data}")


def say_hi():
    print("执行say hi")


say_hi()


def add(x, y):
    result = x + y
    print(f"result={result}")
    return result


add_num = add(1, 2)
print(f"add_num={add_num}")
str_str = "success2"
if str_str:
    print(f"str_str={str_str}")

if __name__ == '__main__':
    add(1, 2)


def _add_num_1_():
    print()
