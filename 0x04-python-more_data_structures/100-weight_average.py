#!/usr/bin/python3

def weight_average(my_list=[]):
    mul = []
    final = []
    multi = 1.0
    if my_list:
        for element in my_list:
            for i in range(len(element)):
                multi *= element[i]
                if i + 1 == len(element):
                    final.append(element[i])
            mul.append(multi)
            mul = 1
        return float(sum(mul)) / float(sum(final))
    else:
        return 0
