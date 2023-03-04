namelist = []
for i in range(5):
  name = input()
  namelist.append(name)
  if name == "Ellie":
    position = i+1
if position == 1:
  print("1st")
elif position == 2:
  print("2nd")
elif position == 3:
  print("3rd")
elif position == 4:
  print("4th")
else:
  print("5th")
