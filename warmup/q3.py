while True:
  num = int(input())
  if num <= 0:
    continue
  else:
    break

remainder = num%8
if num//8 == 0:
  print(8)
else:
  if remainder <= 4:
    print((num//8)*8)
  else:
    print((num//8 + 1)*8)
