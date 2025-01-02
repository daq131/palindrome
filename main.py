def palindrome(text):
    '''
    A function that takes a string as an argument and checks if it is a palindrome 
    '''
    if text == text[::-1]:
        return True
    else:
        return False

print(palindrome('kajak'))
