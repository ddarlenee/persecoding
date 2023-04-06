while True:
  n1 = int(input())
  n2 = int(input())
  n3 = int(input())
  if n1 <= 0 or n2 <= 0 or n3 <= 0:
    continue
  if n1 < n2 and n1 < n3:
    sidelength = n1
    if n1**2 == n2:
      area = n2
      perimeter = n3
    else:
      area = n3
      perimeter = n2
  elif n2 < n3 and n2 < n1:
    sidelength = n2
    if n2**2 == n1:
      area = n1
      perimeter = n3
  else:
    sidelength = n3
    if n3**2 == n2:
      area = n2
      perimeter = n1
  break
print(sidelength)
print(perimeter)
print(area)
