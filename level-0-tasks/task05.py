

def area_of_triangle (length1,length2,length3):

    semiperimeter = (length1 + length2 + length3 ) /2

    area = (semiperimeter*(semiperimeter - length1) *(semiperimeter - length2) * (semiperimeter - length3)) ** (1/2)
    return area

traiangle_area = area_of_triangle (3,4,5)

print(traiangle_area)

        