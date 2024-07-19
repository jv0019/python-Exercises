def num_increasing_reverse_pyramid(rows):
    for i in range(rows,0,-1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

rows = int(input("Enter the num of rows: "))
num_increasing_reverse_pyramid(rows)