x = 42 == 30
print(x)
#==============================
name = 'Bob'
age = 30

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo')
else:
    print('You are neither Alice nor a little kid.')
#==============================
spam = 0
while spam < 5:
    print('Hello, world!')
    spam = spam + 1
#==============================
# while True:
#     print('Please type your name')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It\'s a fish.\)')
#     password = input()
#==============================
for i in range(5):
    print('Jimmy Five Times ({})'.format(str(i+1)))