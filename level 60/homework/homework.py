# https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
def double_char(s):
     return ''.join([char * 2 for char in s])
# https://www.codewars.com/kata/557cd6882bfa3c8a9f0000c1
def get_age(age):
    return int(age[0])
#  https://www.codewars.com/kata/5aa736a455f906981800360d
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]
# https://www.codewars.com/kata/5a2be17aee1aaefe2a000151
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)
# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
def solution(number):
        # If the number is negative, return 0
    if number < 0:
        return 0
    
    total_sum = 0
    
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:  
            total_sum += i
    
    return total_sum
  