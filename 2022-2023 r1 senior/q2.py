while True:
    char1 = input()
    char2 = input()
    if len(char1) != 1 or len(char2) != 1:
        continue
    if char1.isdigit() or char2.isdigit():
        continue
    if char2 == char1:
        continue
    else:
        break
print(char2*2 + char1*6 + char2*2)
print(char1*2 + char2*6 + char1*2)
