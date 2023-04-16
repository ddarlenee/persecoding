a = int(input())
b = int(input())
c = int(input())

a_eats = a // 2
b_gets = b + a - a_eats
b_eats = b_gets // 2
c_gets = c + b_gets - b_eats
c_eats = c_gets // 2

print(c_gets - c_eats + a_eats)
