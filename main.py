# Check if the given number is an Armstrong number or not.

number = int(input("Enter a number: "))
# 132 - 1 3 2

number = str(number)

raised = 0
for i in number:
    print(i)
    i = int(i)
    raised+= i**len(number)

print(raised)
number = int(number)

if raised == number:
    print(f"The number {number} is an Armstrong number.")
else:
    print(f"The number {number} isn't an armstrong number.")