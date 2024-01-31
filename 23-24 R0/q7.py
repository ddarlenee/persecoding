wordlearn = int(input())
total = 0
interactions = 0 
day = 1
while interactions < wordlearn:
  if wordlearn - interactions < 5:
    interactions = wordlearn
  else:
    interactions = 5 * day
  total += interactions
  day += 1
print(total)
