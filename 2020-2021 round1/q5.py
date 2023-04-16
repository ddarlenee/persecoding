end = False
while True:
  minlength = int(input())
  if minlength < 1 or minlength > 30:
    continue
  maxlength = int(input())
  if maxlength < 1 or maxlength > 30:
    continue
  break
valid = 0
invalid = 0
count = 0
while not end:
  length = int(input())
  if length >= 1:
    count += 1
    if minlength <= length <= maxlength:
      valid += 1
    else:
      invalid += 1
  elif length == -1:
    end = True

print(valid)
print(invalid)
