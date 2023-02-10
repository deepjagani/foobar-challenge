#en-route-salute challenge 2 level 2
def solution_2_2(s):
    passes = salutes = 0
    for i in range(len(s)):
        if s[i] == '<':
            passes += 1
    for x in range(len(s)):
        if s[x] == '>':
            salutes += passes     
        elif s[x] == '<':
            passes -= 1
    total_salutes = salutes * 2
    return total_salutes
