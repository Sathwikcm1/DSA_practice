#FIXME: This is extra question i got from doing gemini.
#problem: Calculate the factorial of a number. like for example: 5!= 5*4*3*2*1.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    #NOTE: because the result of factorial of zero is 1.
    else:
        result = 1 #TODO: we initiate to 1 because it is multiplication.
        for i in range(1,n+1): #TODO: we go to n+1 because we want to include the nth element in the multiplication.
            result *= i 
        return result

print(f"Factorial of 5: {factorial(5)}")

