# 单行注释
import random

print("heima")

'''
基本类型展示
'''
money = 50
money -= 10
money -= 5
print(money)
print(type(money))  # type查看类型信息

# 类型转换
print("类型转换")
number = 10
num_str = str(number)
print(type(num_str), num_str)
print(5 // 3)
print(5 // 2)
str1 = "199"
# 字符串的定义扩展
print("打印数据" + str1 + "")
# % (data1, data2) 将数字转换为字符串进行拼
print("打印数据%d" % number)

# 精度控制 %m.nd
print(f"我是{number}, 我的类型为:{num_str}")

name = "bytedance"
stock_price = 19.99
stock_code = 1000
stock_price_daily_growth_factor = 1.2
growth_days = 7

print(f"公司: {name}, 股票代码: {stock_code}, 当前股价为: {stock_price}")
print("增长系数:%.1f, 经过%d的增长之后，股价达到了: %.2f" % (stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor ** growth_days))

# input语句的基本使用

# number = int(input("请输入数据："))
# print("input: %d" % number)

print("欢迎来到游乐场...")
age = int(input("请输入年龄: "))
if age > 18:
    print("您已经成年需要补票10元")
else:
    print("您为学生，不需要补票")
print("祝你生活愉快")


num = random.randint(1, 10)
guess_num = int(input("第一次猜数字:"))
if guess_num == num:
    print("第一次就猜中了...")
elif guess_num < num:
    print("猜小了...")
else:
    print("猜大了")

i = 3
while i > 0:
    num = random.randint(1, 10)
    guess_num = int(input("第一次猜数字:"))
    if guess_num == num:
        print("第一次就猜中了...")
    elif guess_num < num:
        print("猜小了...")
    else:
        print("猜大了")
    i -= 1
