while True:
  n1 = int(input())
  if n1 < 0 or n1 > 1000:
    continue
  else:
    break
while True:
  n2 = int(input())
  if n2 <= 0 or n2 > 1000:
    continue
  if n2 == n1:
    continue
  else:
    break
if n1>n2:
  print(n1-n2)
else:
  print(n2-n1)
