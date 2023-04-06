while True:
  word = input()
  if word.isalpha() == False or len(word) != 4 or word.islower() == False:
    continue
  else:
    break
if ord(word[0]) > ord(word[-1]):
  print(word[::-1])
  print(word)
else:
  print(word)
  print(word[::-1])
