import string
def is_pangram(s):
    #remove/ignore all character in a string that are not alphabetical.
    alpha_list = []
    a = list(s)
    for cha in a:
        if cha.isalpha():
            alpha_list.append(cha.lower())
    #check if the string has all the alphabetical characters
    alphabet = list(string.ascii_lowercase)
    if len(set(alpha_list)) == len(alphabet):
        return True
    else:
        return False

   
def smart_solution(s):
    return set(string.ascii_lowercase).issubset(s.lower())

print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))
print(smart_solution("1bcdefghijklmnopqrstuvwxyz"))