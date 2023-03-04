output = ''
while True:
    word = input()
    if len(word) >= 50:
        continue
    else:
      break
word = word.lower()
length = 0
while length < 31:
  output += word
  length += len(word)
print(output)
