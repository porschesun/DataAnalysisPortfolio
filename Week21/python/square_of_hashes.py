# Copy here code of line function from previous exercise

def line(a,b):
    out=""
    if b== "":
        out=a*("*")
        
    else :
        out=a*b[0]
    print(out)

def square_of_hashes(height):
    # You should call function line here with proper parameters
    num1=0
    while num1 < height:
        line(height, "#")
        num1 +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)