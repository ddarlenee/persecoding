dancemoves = ['<', '+', '&', '>']
while True:
  dancechar = input()
  if dancechar not in dancemoves:
    continue
  else:
    break
twocycle = dancechar
count = 1
index = dancemoves.index(dancechar) + 1
while count != 8:
  for i in range(7):
    if index != 4:
      twocycle += dancemoves[index]
    else:
      index = 0
      twocycle += dancemoves[index]
    index += 1
    count += 1
print(twocycle)
