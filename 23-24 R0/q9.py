validno = 0
for i in range(12):
  num = input()
  if int(num[-1]) - int(num[0]) == 1 or int(num[0]) - int(num[-1]) == 1:
    validno += 1
print(validno)
