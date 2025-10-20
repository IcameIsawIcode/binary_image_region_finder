import cv2
import numpy as np
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






image_filename = 'your_image_name.png' 
img = cv2.imread(image_filename, cv2.IMREAD_GRAYSCALE)

if img is None:
    print(f"Error: Could not load image '{image_filename}'")
    print("Make sure the image is in the same folder as the script.")
    exit()

# Threshold the image to make it binary
_, l = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY_INV)

r, c = l.shape
ans = 0  
a2 = 0   
a3 = 0   

for i in range(r):
    for j in range(c):
        
        checki = check(l, r, c, i, j)
        
        # Update the largest square size and its top-left corner
        if checki > ans:
            ans = checki
            a2 = i  # Top row
            a3 = j  # Left-most column


print(f"Found largest square of size: {ans}x{ans}")
print(f"Top-left corner at: (row={a2}, col={a3})")

# Create a displayable image: 0 becomes 0 (black), 1 becomes 255 (white)
display_image = l * 255

# Convert to a 3-channel (BGR) image so we can draw a color rectangle
display_image_color = cv2.cvtColor(display_image, cv2.COLOR_GRAY2BGR)

# Draw a red (0, 0, 255) rectangle on the image
# (a3, a2) is the top-left corner (x, y)
# (a3 + ans, a2 + ans) is the bottom-right corner (x, y)
# 2 is the thickness of the line
cv2.rectangle(display_image_color, (a3, a2), (a3 + ans, a2 + ans), (0, 0, 255), 2)

# Show the final image in a window
cv2.imshow("Largest Tissue Region (Segmentation)", display_image_color)

# Wait for a key press to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
