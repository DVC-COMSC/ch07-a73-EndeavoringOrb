

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))

for i in range(len(numbers)):
    if insval > len(numbers):
        continue
    else:
        numbers.insert(i,insval)
# ******************************
# Make your Code
# ******************************

print (numbers)
