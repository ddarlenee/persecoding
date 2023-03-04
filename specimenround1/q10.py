ingredients = input()
no_I = 0
no_M = 0
no_C = 0
no_W = 0
for i in range(6):
  if ingredients[i] == "I":
    no_I += 1
  if ingredients[i] == "M":
    no_M += 1
  if ingredients[i] == "C":
    no_C += 1
  if ingredients[i] == "W":
    no_W += 1
if no_I != 2:
  print("I")
if no_M != 1:
  print("M")
if no_C != 3:
  print("C")
if no_W != 1:
  print("W")
