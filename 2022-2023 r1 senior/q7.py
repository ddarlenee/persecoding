exact = False
count = 0
total = 0
while not exact:
  number = int(input())
  if 1 <= number <= 10 and total < 20:
    total += number
    count += 1
    if total == 20:
      print(count)
      break
    elif total > 20:
      total = 0
      continue
    else:
      continue
