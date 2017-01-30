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


#------------------------------------------------------------------------
# Letter Capitalize (1st character of each word)
def LetterCapitalize(str): 

    words = str.split(" ")
    
    for i in range(0, len(words)):
        words[i] = words[i][0].upper() + words[i][1:]
        
    return " ".join(words)
    
# keep this function call here  
print LetterCapitalize("this is just a demo")


#------------------------------------------------------------------------
# Simple Symbols (if a char has + before and after it is true else false)
def SimpleSymbols(str): 

    for i in range(0, len(str)):
        if str[i].isalpha():
            if str[i-1] != '+' or str[i+1] != '+':
                return 'false'
    return 'true'
        
    
# keep this function call here  
print SimpleSymbols("+a+-++b+")


#------------------------------------------------------------------------
# Time convert (convert mints into hours:mints)
def TimeConvert(num): 

    hour = (num/60)
    minute = (num % 60)
    
    return (str(hour) + ':' +str(minute))
    
# keep this function call here  
print TimeConvert(119)
#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------

#------------------------------------------------------------------------