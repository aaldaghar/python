#count duplicate characters

def duplicate_count(s):
    #first create a dictionary that stores each character and the number of it's dups
    chars = {}
    for char in s.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    #then only store the dups in a dict w/ a value of the characters repeated.
    duplicate = {}

    for char, count in chars.items():
        if count > 1:
            duplicate[char] = 1
    return sum(duplicate.values())

    
print(duplicate_count("abcd"))

