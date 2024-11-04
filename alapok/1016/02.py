size = int(input("Kérlek adj meg egy számot! "))
for x in range(size):
    for y in range(size):
        if x == y or (x + y) == size - 1:
            print("O", end=" ")
        else:
            print(".", end=" ")
    print()
