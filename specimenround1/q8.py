while True:
  days = int(input())
  if days < 1 or days > 100:
    continue
  else:
    break
for i in range(days+1):
  if i == 0:
    print("\./")
  else:
    print(".|.")
