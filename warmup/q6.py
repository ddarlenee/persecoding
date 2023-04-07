over100 = 0
total = 0
stop = False
while not stop:
  num = int(input())
  if num > 0:
    total += num
  if num >= 1000000:
    continue
  elif num > 100:
    over100 += 1
  elif num < 0:
    stop = True
  else:
    continue
print(total)
print(over100)
