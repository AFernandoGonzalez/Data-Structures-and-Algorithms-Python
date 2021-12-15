

# Strings

greet = 'hello world'
print(greet[1])
print(greet[0:8])
print(greet[0:8:2])
print(greet[0::2])
print(greet[1+2])
print(greet[len(greet)-1])
# print(len(greet)-1)

print('For Loop String')
for i in enumerate(greet[0:5]):
    print(i)