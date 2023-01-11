# palindron- if u read from start or end the word will be same EG: madam
def is_palindrom(word):
    reversed_word=word[::-1]
    if word==reversed_word:
        return True
    return False
word=input("enter the word: ")
print(is_palindrom(word))