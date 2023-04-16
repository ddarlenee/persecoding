firstname = input()
surname = input()
if ord(surname[0]) < ord('H'):
  print(firstname, surname)
else:
  print(surname + ', ' + firstname)
