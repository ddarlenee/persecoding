while True:
  num = input()
  if num.isdigit() == False or int(num) >= 1000:
    continue
  else:
    num = int(num)
    break

stop = False  
while not stop:
  if num > 1000:
    stop = True
  else:
    num = num**2 + 1

print(num)
