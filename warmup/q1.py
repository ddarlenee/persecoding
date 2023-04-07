amount = []
total = 0
for i in range(5):
  while True:
    num = int(input())
    if num <= 0:
      continue
    else:
      break
  total += num
  amount.append(num)

while True:
  lost = int(input())
  if 1 <= lost <= 5:
    total -= amount[lost-1]
    del amount[lost-1]
    break
  else:
    continue

print("$" + str(total))
