import string     

def find_missing_letter(chars):
    alphabet=list(string.ascii_lowercase) if str(chars[0]).islower() else list(string.ascii_uppercase)
    for a,c in zip(alphabet[alphabet.index(chars[0]):],chars):
        if a!=c:
            return a

print('the missing letter is:',find_missing_letter(['a','b','c','d','f']))
print(30*'-')
print(find_missing_letter(['O','Q','R','S']))
