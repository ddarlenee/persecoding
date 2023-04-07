horse0_stepcount = 0
horse1_stepcount = 0

def endposition(horse0_stepcount, horse1_stepcount):
  if horse0_stepcount == 11:
    if horse1_stepcount == 0:
      line = "H..........|"
    else:
      line = "|"
    for j in range(1, 11):
      if j == horse1_stepcount:
        line += "H"
      else:
        line += "."
    line += "|"
    print("|..........H")
    print(line)
  else:
    if horse0_stepcount == 0:
      line = "H..........|"
    else:
      line = "|"
    for j in range(1, 11):
      if j == horse0_stepcount:
        line += "H"
      else:
        line += "."
    line += "|"
    print(line)
    print("|..........H")
    
# main
for i in range(22):
  while True:
    bindigit = int(input())
    if bindigit != 0 and bindigit != 1:
      continue
    if horse1_stepcount == 11:
      if bindigit == 1:
        continue
    if horse0_stepcount == 11:
      if bindigit == 0:
        continue
    if bindigit == 0:
      if horse1_stepcount != 11:
        horse0_stepcount += 1
    else:
      if horse0_stepcount != 11:
        horse1_stepcount += 1
    break

endposition(horse0_stepcount, horse1_stepcount)
