def common_letters_in_strings (string1,string2) :
    common_letters = []

    for letter in string1.lower() :

        if letter in string2.lower() :
            common_letters.append(letter.lower())
    print(f"Common letters : {', '.join(common_letters)}")      

common_letters_in_strings ("Computer","house")     