#Add Digits*
def add_digits(num):
    while num >= 10:  
        sum = 0
        for digit in str(num): 
            sum = sum + int(digit)
        num = sum
    return num

print("Add digits of 38:", add_digits(38))
