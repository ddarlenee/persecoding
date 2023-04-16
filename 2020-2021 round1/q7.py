num = int(input())
names = []
for i in range(num):
  name = input()
  if name.isupper() == False:
    continue
  else:
    names.append(name)

eliminator = None
names.sort()

while len(names) > 1:
    if not eliminator:
        eliminator = list(names.pop(0))
    if len(names) == 1:
        break
    letter = eliminator.pop(0)
    names = [name for name in names if (letter not in name)]

if len(names) == 1:
    print(names[0])
else:
    print("NO RESULT")
