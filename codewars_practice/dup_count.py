# take a string and count the duplicate characters. 
# Create an empty list, and add characters only if duplicate. 
# then count the length of the list. 

def duplicate_count(s):
    #first create a dictionary
    chars = {}
    for char in s.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    
    duplicate = {}

    for char, count in chars.items():
        if count > 1:
            duplicate[char] = 1
    return sum(duplicate.values())

    
    

print(duplicate_count("abcd"))

