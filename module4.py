s=input("Enter a string:")

char=s[0]

s=s.replace(char,'$')

s=char+s[1:]

print(s)