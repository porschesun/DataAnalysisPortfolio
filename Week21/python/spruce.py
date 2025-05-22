# Write your solution here


def spruce(s):
 print("a spruce!")
 num=0
 emp=" "
 while num < s:
     print(emp * (s-num-1) + "*"*(2*num+1) + emp * (s-num-1))
     num +=1

 print(emp * (s-1) + "*" + emp * (-1))
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(10)