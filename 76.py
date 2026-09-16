def count_vowels(s):
    if len(s) == 0:
        return 0
    first = 1 if s[0].lower() in 'aeiou' else 0
    return first + count_vowels(s[1:])

s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))
