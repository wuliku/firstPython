"""
循环练习
"""
import random

# sum = 0
# i = 1
# while i < 100:
#     sum += i
#     print(f"i={i}, sum={sum}")
#     i += 1
# print("sum=", sum)

# num = random.randint(1, 100)
# print("num=", num)
# flag = True
# i = 1
# while flag:
#     guess_num = int(input("请输入猜测的数字:"))
#     if guess_num == num:
#         print(f"猜中了，一共猜测了{i}次")
#         flag = False
#     else:
#         if guess_num < num:
#             print("猜错了，小了")
#         else:
#             print("猜错了，大了")
#     i += 1
# print("猜测完成...")

# t_str = "bytedance"
# for i in range(1, 10):  # 一般情况下不能针对基本的大于等于
#     print("i=", i)
t_list = ["a", "b"]
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{i} * {j} = {i * j}", end="\t")
#         continue
#     print()
sum_salary = 10000
for i in range(1, 21):
    if sum_salary <= 0:
        break
    score_num = int(input("绩效: "))
    if score_num < 5:
        print(f"{i}号员工绩效分为{score_num}, 无法领工资")
        continue
    else:
        sum_salary -= 3000
        print(f"剩余工资{sum_salary}元")
        print(f"{i}号员工领取工资3000元，绩效分为{score_num}分")