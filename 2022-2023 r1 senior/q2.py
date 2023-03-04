char1 = input()
while True:
    char2 = input()
    if char2 == char1:
        continue
    else:
        break
line1 = char1*2 + char2*6 + char1*2
print(line1)
line2 = char2*2 + char1*6 + char2*2
print(line2)
    
    
    
