# Function to check the size of the largest square of 1's starting at (i, j)
def check(l, r, c, i, j):
    # If the current cell is 0, return 0 
    if l[i][j] == 0:
        return 0
    else:
        # Initialize variables to track the number of rows (`lr`) and columns (`lc`) in the square
        lr = 0  
        lc = 0  
        lc2 = 0 
        j1 = j  
        i1 = i  

        # Outer loop to iterate through rows while the square is valid
        while i < r and j < c and l[i][j] == 1:
            # Inner loop to iterate through columns in the current row
            while i < r and j < c and l[i][j] == 1:
                i += 1  
                lc2 += 1  
            
            # Update the minimum column count (`lc`) for the square
            if j != j1:
                lc = min(lc, lc2)  
            else:
                lc = lc2  
            
            lr += 1  
            j += 1  
            lc2 = 0  
            i = i1  

        # The size of the largest square is the minimum of the row and column counts
        ans = min(lr, lc)
        return ans

# Input 
r, c = map(int, input().split())


l = [list(map(int, input().split())) for _ in range(r)]


ans = 0  
a2 = 0   
a3 = 0   

# Iterate through each cell in the grid
for i in range(r):
    for j in range(c):
        
        checki = check(l, r, c, i, j)
        
        # Update the largest square size and its top-left corner if a larger square is found
        if checki > ans:
            ans = checki
            a2 = i
            a3 = j


print(ans)


print(a2, a3)
