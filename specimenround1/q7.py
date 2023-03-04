char1 = input()
char2 = input()
if ord(char1.upper()) < ord(char2.upper()):
  print(char1 + char2)
else:
  print(char2 + char1)
