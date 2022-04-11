def number_to_time(number):
    hour = 0 
    while number>=60 :
        hour += 1
        number-=60

    print_time(hour,number) 
 
def print_time (hours,minutes):

    if hours <0 or minutes <0 :
        print ("There is no negative time, Please input postive integers")

    elif hours !=1 and minutes !=1 :
        print (f"{hours} hours {minutes} minutes")

    elif hours ==1 and minutes ==1 :
        print (f"{hours} hour {minutes} minute")

    elif hours ==1 and minutes !=1 :
        print (f"{hours} hour {minutes} minutes")

    elif hours !=1 and minutes == 1 :
        print (f"{hours} hours {minutes} minute")    

number_to_time(77)

