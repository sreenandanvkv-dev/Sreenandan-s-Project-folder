n = int(input("enter number of rows: "))

for i in range(n): #outer loops for now
    for j in range(i+1): #inner loops for column
        print("*", end=" ")

    print()