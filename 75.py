def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

s = input("Enter a string: ")
print(f"'{s}' is {'a palindrome' if is_palindrome(s) else 'not a palindrome'}")
