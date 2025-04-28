# https://www.codewars.com/kata/55b95c76e08bd5eef100001e/train/python
    # adak_count = n // 2
    # result = "adak " * adak_count
    # if n % 2 != 0:
    #     result += "anane"
    # return result.strip()
# https://www.codewars.com/kata/67d4554cd94fdfdab4239cfa/train/python
def is_planet_mnemonic_correct(solar_system, mnemonic):
    filtered_solar_system = [planet for planet in solar_system if planet != "Asteroid"]
    
    mnemonic_initials = [word[0] for word in mnemonic.split()]

    return [planet[0] for planet in filtered_solar_system] == mnemonic_initials
# https://www.codewars.com/kata/59656c69253c365e58000046/train/python
def max_possible_score(questions, new): 
    total_score = 0
    for question, points in questions.items():
        if question in new:
            total_score += points * 2
        else:
            total_score += points
    return total_score