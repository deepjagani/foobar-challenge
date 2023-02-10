#power hungry challenge 1 level 2
def solution_2_1(xs):
    if(xs.count(0) == len(xs)):   
        return (str(0))
    if(len(xs)== 1):    
        return str(xs[0])
    if(len([x for x in xs if x < 0]) == 1 and xs.count(0) == len(xs) - 1): 
        return str(str(0))
    max_product = 1
    for i in xs:
        if i != 0 and i <= 1000:
            max_product *= i
    if max_product < 0:
        big_negative_number = max([val for val in xs if val < 0])
        max_product = max_product / big_negative_number
    return str(int(max_product))
