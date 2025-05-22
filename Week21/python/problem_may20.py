### sec3-4 Chessboard
def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            row = "10"*size
        else:
            row = "01"*size
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1
# Test the function
if __name__ == "__main__":
    chessboard(10)
    
### sec3-4 A word squared

def squared(characters, size):
    i = 0
    row = ""
    while i < size * size:
        if i > 0 and i % size == 0:
            print(row)
            row = ""
        row += characters[i % len(characters)]
        i += 1
    print(row)
    
    # Test the function
if __name__ == "__main__":
    squared("abc",5 )
