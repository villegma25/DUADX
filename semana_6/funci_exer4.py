a = 'Hello world'
count = 0
for letter in a:
    count += 1

b = ''
for letter in a:
    b += a[count-1]
    count -= 1

print(b)