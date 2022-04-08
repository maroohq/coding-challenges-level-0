def vowels_in_string (string) :
    vowels =['a','e','i','o','u']
    in_string =[]

    for letter in string :
        if letter.lower() in vowels :
            in_string.append(letter.lower())
    
    print ("Vowels : " + ", ".join(set(in_string)) )

vowels_in_string("Umuzi")     