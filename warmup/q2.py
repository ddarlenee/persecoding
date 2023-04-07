while True:
  age = input()
  if age.isdigit() == False or len(age) > 3:
    continue
  else:
    break

while True:
  char = input()
  if len(char) != 1:
    continue
  else:
    break

if len(age) == 1:
  print(char*3)
elif len(age) == 2:
  print(char*4)
else:
  print(char*5)
print(char + str(age) + char)
if len(age) == 1:
  print(char*3)
elif len(age) == 2:
  print(char*4)
else:
  print(char*5)
