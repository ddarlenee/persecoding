username = []
repeated = True
while True:
  firstname = input()
  if len(firstname) > 20:
    continue
  secondname = input()
  if len(secondname) > 20:
    continue
  break

username.append(firstname[0].lower())
username.append(secondname[0].lower())
username.append(secondname[-1].lower())
username.append(len(firstname))

for x in range(len(username)):
  char = username[x]
  for y in range(len(username)):
    if y != x:
      if char == username[y]:
        repeated = False

if not repeated:
  print(''.join(str(username[z]) for z in range(len(username))) + 'x')
else:
  print(''.join(str(username[z]) for z in range(len(username))))
