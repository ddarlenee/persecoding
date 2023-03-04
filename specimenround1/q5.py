while True:
  n1 = int(input())
  if n1 <= -100 or n1 >= 100:
    continue
  else:
    break
while True:
  operation = input()
  if operation != '*' and operation != '+':
    continue
  else:
    break
while True:
  n2 = int(input())
  if n2 <= -100 or n2 >= 100:
    continue
  else:
    break
if operation == '+':
  print(n1+n2)
else:
  print(n1*n2)
