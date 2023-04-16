numlist = []
for i in range(3):
  num = int(input())
  if 1 <= num <= 10:
    numlist.append(num)
  else:
    continue

if numlist[0]%2 == 0:
  numlist[0] = numlist[0]//2
else:
  numlist[0] = numlist[0]//2 + 1
      
for x in range(1,3):
  numlist[x] += numlist[x-1]
  if numlist[x]%2 == 1:
    numlist[x] = numlist[x]//2 + 1
  else:
    numlist[x] = numlist[x]//2

print(numlist[0] + numlist[2])
