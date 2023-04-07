stop = False
total = 0
count = 0
while not stop:
  num = int(input())
  if -100 <= num <= 100:
    count += 1
    total += num 
    if total == 0:
      print(count)
      stop = True
    else:
      continue
  else:
    continue
