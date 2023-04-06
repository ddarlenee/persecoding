while True:
  initial = input()
  if initial.isdigit() == False:
    continue
  else:
    initial = int(initial)
  if initial <= 0 or initial > 10000:
    continue
  goodvalue = initial
  for i in range(5):
    while True:
      newprice = input()
      if newprice.isdigit() == False:
        continue
      else:
        newprice = int(newprice)
      if newprice < 0 or newprice > 10000:
        continue
      else:
        break
    if goodvalue < newprice:
      goodvalue = newprice
    else:
      if initial > newprice:
        print(initial - newprice)
      else:
        print(newprice - initial)
      break
  break
