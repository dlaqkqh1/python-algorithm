class NotPalindromeError(Exception):
    pass

def palindrome(word):
    word_test = word
    while len(word_test) > 1:
        if word_test[0] == word_test[-1]:
            word_test = word_test[1:-1]
        else:
            raise NotPalindromeError('회문이 아닙니다.')
    print(word)
try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)