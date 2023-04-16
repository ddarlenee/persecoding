situation = [0]
empty = 0
for i in range(20):
  seat = int(input())
  if seat != 0 and seat != 1:
    continue
  else:
    situation.append(seat)

situation.append(0)

for x in range(1, 21):
  if situation[x] == 0 and situation[x-1] == 0 and situation[x+1] == 0:
    empty += 1
    situation[x] = 1

print(empty)
