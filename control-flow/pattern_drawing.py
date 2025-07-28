size = int(input("Enter the size of the pattern: "))
x = 1
while x <= size:
    for y in range(size):
        print("*", end="")
    print()
    x += 1