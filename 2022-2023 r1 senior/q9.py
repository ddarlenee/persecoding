while True:
  x = int(input())
  y = int(input())
  if x < 0 or y < 0:
    continue
  if 0 <= x <= 9 and 0 <= y <= 9:
    break
  else:
    continue
  
for i in range(10):
  if y != i:
    print("#"*10)
  else:
    line = ""
    for j in range(10):
      if x == j:
        line += "X"
      else:
        line += "#"
    print(line)
