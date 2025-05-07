# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python 
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
def find_smallest_int(arr):
    return min(arr)
# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]