
def maximum (*number):
    
    if len (number)>0:
        max = number[0]
    else : 
        return ("Please Enter Function Arguments e.g maximum(2,4)")

    for i in range(1,len(number)):
        if number[i]>max:
            max = number[i]
    return max      

print( maximum(1,2,3) )
        