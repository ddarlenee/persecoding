difference = 1000
while True:
  n1 = int(input())
  n2 = int(input())
  if -200 <= n1 <= 200 and -200 <= n2 <= 200:
    break
  else:
    continue

if n1 + n2 > 100:
  if difference > abs((n1 + n2) - 100):
    difference = abs((n1 + n2) - 100)
else:
  if difference > abs(100 - (n1 + n2)):
    difference = abs(100 - (n1 + n2))
if n1 - n2 > 100:
  if difference > abs((n1 - n2) - 100):
    difference = abs((n1 - n2) - 100)
else:
  if difference > abs(100 - (n1 - n2)):
    difference = abs(100 - (n1 - n2))
if n2 - n1 > 100:
  if difference > abs((n2 - n1) - 100):
    difference = abs((n2 - n1) - 100)
else:
  if difference > abs(100 - (n2 - n1)):
    difference = abs(100 - (n2 - n1))
print(difference)
