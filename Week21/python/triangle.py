# Copy here code of line function from previous exercise
def line(a,b):
    out=""
    if b== "":
        out=a*("*")
        
    else :
        out=a*b[0]
    print(out)
    
def triangle(size):
    s=0
    while s < size :
        s +=1
        line(s, "#")
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
