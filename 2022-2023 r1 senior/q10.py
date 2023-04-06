horse0_stepcount = 0
horse1_stepcount = 0

while True:
  bindigit = int(input())
  if bindigit != 0 and bindigit != 1:
    continue
  if horse0_stepcount == 11 or horse1_stepcount == 11:
    if horse0_stepcount == 11:
      print("|..........H")
      loserposition = ""
      for i in range(12):
        if i == loserposition:
          loserposition == "H"
        elif i == 0 or i == 11:
          loserposition += "|"
        else:
          loserposition += "."
    else:
      print("|..........H")
      loserposition = ""
      for i in range(12):
        if i == loserposition:
          loserposition == "H"
        elif i == 0 or i == 11:
          loserposition += "|"
        else:
          loserposition += "."
    print(loserposition)
    break
  else:
    if bindigit == 0:
      horse0_stepcount += 1
    else:
      horse1_stepcount += 1
