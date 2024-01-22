#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divide element by element 2 lists"""
    new_list = []
    for idx in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            new_list.append(quotient)
    return new_list


my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)