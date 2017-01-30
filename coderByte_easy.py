# Reverse the string
def FirstReverse(str): 

    return str[::-1]
 
# keep this function call here  
print FirstReverse("Hello Worl!")

#------------------------------------------------------------------------
# First Factorial
def FirstFactorial(num): 

    if (num == 0):
        return 1
    else:
        return num*FirstFactorial(num -1)

# keep this function call here  
print FirstFactorial(5)

#------------------------------------------------------------------------
# Longest word in String
def LongestWord(sen): 

    sen = sen.translate(None, "~!@#$%^&*()-_+={}[]:;'<>?/,.|`")
    arr = sen.split(" ")
    
    return max(arr, key=len)
# keep this function call here  
print LongestWord("This is just a demo")

#------------------------------------------------------------------------
# sum of integers
def SimpleAdding(num): 

    # code goes here 
    return num*(num+1)/2
    
# keep this function call here  
print SimpleAdding(5)