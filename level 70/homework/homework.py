#  https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
def double_char(s):
     return ''.join([char * 2 for char in s])
#  https://www.codewars.com/kata/563e320cee5dddcf77000158/train/python
def get_average(marks):
    return sum(marks) // len(marks)
#  https://www.codewars.com/kata/515e188a311df01cba000003/train/python
def get_planet_name(id):

    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    
    return planets.get(id, "Invalid planet number")
#  https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif a == "":
        return b
    elif b == "":
        return a
    else:
        return str(int(a) + int(b))
#  https://www.codewars.com/kata/5899642f6e1b25935d000161/train/python
def merge_arrays(arr1, arr2):
    combined = set(arr1 + arr2)      
    return sorted(combined) 