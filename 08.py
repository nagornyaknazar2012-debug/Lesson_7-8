# Example 01

# try:
#     print("Start code")
#     print(error)
#     print("No errors")
#
# except:
#     print("We have an error")
#
# print(f"\nCode after capsule")



# Example 02

# try:
#     print("Start code")
#     print(10/0)
#     print("No errors")
#
# except ZeroDivisionError:
#     print("We have an Zero Division Error")
# except NameError:
#     print("We have Name Error")
#
#
# print(f"\nCode after capsule")




# Example 03

# try:
#     print("Start code")
#     print(10/0)
#     print("No errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)
#
# print(f"\nCode after capsule")






# Example 04

try:
    x = int(input("Введіть число: "))
    res = 10 / x
    print(res)
except(ZeroDivisionError, ValueError) as e:
    print("Неправильно введене число!")

print(f"\nCode after capsule")







