def factorial(number):
    if number == 0 or number==1:
        return 1
    else:
        fac =1    
        return number *factorial(number -1)
def factorialTraillngZeros(number):
    count=0
    fac = factorial(number)
    #print(fac)
    while (fac %10 == 0):
        count = count+1
        fac=fac /10
    return count        
if __name__ == "__main__":
    number = int(input("Enter the number :\n"))
    fac = factorial(number)
    print(f"The factorial of {number} is {fac}.")
    zero = factorialTraillngZeros(number)
    print(f"The trailing zero present in Factorial is {zero}.")