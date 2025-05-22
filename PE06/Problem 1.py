#Reduce to zero*
def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:  
            num = num // 2
        else:             
            num = num - 1
        steps = steps + 1
    return steps

print("Steps to reduce 14 to zero:", number_of_steps(14))
