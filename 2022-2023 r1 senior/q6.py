while True:
  initial = input()
  if initial.isdigit() == False:
    continue
  else:
    initial = int(initial)
  if initial <= 0 or initial > 10000:
    continue
  goodvalue = initial
  break

while True:
  newprice = input()
  if newprice.isdigit() == False:
    continue
  else:
    newprice = int(newprice)
  if newprice < 0 or newprice > 10000:
    continue
  if goodvalue < newprice:
    goodvalue = newprice
    continue
  else:
    print(newprice - initial)
    break
