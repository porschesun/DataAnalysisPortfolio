# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(a,b):
    out=""
    if b== "":
        out=a*("*")
        
    else :
        out=a*b[0]
    print(out)

def triangle(size, s1):
    s=0
    while s < size :
        s +=1
        line(s, s1)


def shape(n1, s1, n2, s2):
    s=0
    triangle(n1, s1)
    while s < n2 :
        line(n1,s2)
        s +=1
    
    

if __name__ == "__main__":
    shape(5, "y", 2, "o")