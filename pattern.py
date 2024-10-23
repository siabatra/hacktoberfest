def hello_world_pattern(rows):
    for i in range(1, rows + 1):
        print('Hello World ' * i)

# Get user input for the number of rows
try:
    rows = int(input("Enter the number of rows for the pattern: "))
    if rows > 0:
        hello_world_pattern(rows)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input! Please enter an integer.")
