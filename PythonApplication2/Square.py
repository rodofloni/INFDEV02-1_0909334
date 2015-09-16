size = int(input("Enter a number: "))
startsize = size
space = ' '
n = 0

while size != 1:
    print ('*' * size + space * n + '*')
    size = size-1
    n = n+1
print ('*' * size + '*')