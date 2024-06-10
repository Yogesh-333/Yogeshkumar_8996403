def concatenate_strings(str1, str2):
    return str1 + str2

def capitalize_string(s):
    return s.capitalize()

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
