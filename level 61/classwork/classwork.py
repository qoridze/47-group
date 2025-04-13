# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144
def first_non_consecutive(arr):
    if len(arr) < 2:
        return None  
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:  
            return arr[i]
    
    return None

# https://www.codewars.com/kata/56efc695740d30f963000557/train/python
def to_alternating_case(string):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

# https://www.codewars.com/kata/577bd026df78c19bca0002c0
def correct(s):
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')

# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]

# https://www.codewars.com/kata/56f6ad906b88de513f000d96/train/python
def bonus_time(salary, bonus):
    total = salary * 10 if bonus else salary
    return f"${total}"
#  https://www.codewars.com/kata/5ad0d8356165e63c140014d4
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    
#  https://www.codewars.com/kata/559590633066759614000063/train/python
def min_max(lst):
     return [min(lst), max(lst)]