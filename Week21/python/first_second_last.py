# Write your solution here
# You can test your function by calling it within the following block

def first_word(str1):
    
    if " " in str1:
        space = str1.find(" ")
        first = str1[0 : space]
        return first
        
        
def second_word(str1):
    
    if " " in str1:
        first_space = str1.find(" ")
        second_space = str1.find(" ", first_space + 1)
        second_word = str1[first_space + 1 : second_space]
        return second_word       

def last_word(str1) :
    if " " in str1: 
        space1 = str1.rfind(" ")
        last = str1[space1+1 : len(str1)+1 ]
        return last
        
        
        
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))