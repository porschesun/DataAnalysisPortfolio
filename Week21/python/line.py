# Write your solution here
# You can test your function by calling it within the following block
def line(a,b):
    out=""
    if b== "":
        out=a*("*")
        
    else :
        out=a*b[0]
    print(out)
if __name__ == "__main__":
    line(5, "xyz")
    
    