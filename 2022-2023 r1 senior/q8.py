while True:
  word = input()
  if len(word)%2 != 0 or len(word) < 2 or len(word) > 30 or word.isalpha() == False:
    continue
  else:
    break
  
noofpeels = middle = len(word)//2
count = 0

while True:
  if noofpeels != count:
    charlist = [*word]
    middle = len(word)//2 - 1
    charlist[0], charlist[1:middle+1], charlist[-1], charlist[middle+1:-1] = charlist[middle], charlist[:middle], charlist[middle+1], charlist[middle+2:]
    word = "".join(charlist)
    count += 1
    print(word)
  else:
    break
