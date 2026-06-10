# write a program to print number pyramid.
def print_pattern(rows):
    for i in range(1, rows + 1):
        # Print increasing sequence
        for j in range(1, i + 1):
            print(j, end="")
        
        # Print decreasing sequence
        for j in range(i - 1, 0, -1):
            print(j, end="")
            
        print() # Move to the next line

# Generate the pattern for 5 rows
print_pattern(5)