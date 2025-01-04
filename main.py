# def palindrome(text):
#     '''
#     A function that takes a string as an argument and checks if it is a palindrome 
#     '''
#     def palindrome(text):
#         test = True if text == text[::-1] else False
#         print(test)
        
# palindrome('kajak')


def palindrome_sentence(txt):
    new_text = txt.replace(' ', '').replace(',','').replace('.', '').lower()
    return True if new_text == new_text[::-1] else False
    
palindrome_sentence('a, To kanapa pana kota')
palindrome_sentence('a tu mam mamuta')
palindrome_sentence('Wczora z wieczora')