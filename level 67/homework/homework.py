# 1. რიცხვების გაორმაგება
#    დაწერეთ lambda-ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის გაორმაგებულ მნიშვნელობას.  
double = lambda x: x * 2
print(double(5)) 

# 2. სტრინგის სიგრძის გამოთვლა
#    დაწერეთ lambda-ფუნქცია, რომელიც იღებს სტრინგს და აბრუნებს მის სიმბოლოების რაოდენობას.  
string_length = lambda s: len(s)
print(string_length("გამარჯობა")) 

# 3. კენტ და ლუწი რიცხვების ამოცნობა
#    დაწერეთ lambda-ფუნქცია, რომელიც ამოწმებს, რიცხვი კენტია თუ არა.  
is_odd = lambda x: x % 2 != 0
print(is_odd(7))  
print(is_odd(4))  

# 4. რიცხვების კვადრატში აყვანა
#    დაწერეთ lambda-ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს მის კვადრატს.  
square = lambda x: x ** 2
print(square(6))  

# 5. ლუწი რიცხვების კვადრატში აყვანა სიიდან
#    დაწერეთ ფუნქცია, რომელიც lambda-ფუნქციას გამოიყენებს, რათა სიიდან ლუწი რიცხვები ამოარჩიოს და თითოეული მათგანი
# კვადრატში აიყვანოს.
def even_squares(numbers):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))


