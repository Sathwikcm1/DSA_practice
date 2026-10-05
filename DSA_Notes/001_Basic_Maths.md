## Reverse a Number

### Problem Statement

Reverse the digits of a given integer (handle negative numbers).

```python
def reverse_Num(n):
    rev_no = 0
    if n < 0:
        return -reverse_Num(-n)
    while n:
        ld = n % 10
        rev_no = rev_no * 10 + ld
        n = n//10
    return rev_no if rev_no <= 0x7fffffff else 0
```

**Explanation:**

- Convert negative to positive, reverse it, and then reapply `-`.
    
- `%` gets the last digit.
    
- `rev_no * 10 + ld` builds the reversed number.

- Handles overflow for 32-bit int. the 0x7fffffff is the maximum value of 32-digit number. 
- In python, the overflow does not happen because in python integers can grow arbitrarily large. python won´t crash like c or c++/java. 
- But in platforms like leetcode, it is expected to return a zero if x the provided is integer reverse is greater than 2147483647.
    

>[!SUMMARY]
>- Uses modulus and integer division.
-Recursive handling for negative input.
-Overflow condition check. **Time complexity**: O(log x) where x is the integer provided in the question. 





    

> [!TIP]  
> Check overflow and negatives **before** reversing.

---

## Palindrome Number

### Problem Statement

Check whether an integer is a palindrome.

```python
def isPalindrome(x):
    if x < 0:
        return False
    rev = 0
    if x >= 0 and x < 10:
        return True
    copy = x
    while copy:
        last_digit = copy % 10
        rev = rev * 10 + last_digit
        copy = copy//10
    return x == rev
```

- The above code will reverse the entire number, digit by digit. 
- Each iteration strips off one digit using copy%10 and `copy//10`
- For an n digit number, you do n iterations. So the ==time complexity would be **O(log X)**== where x is the given integer. 

#### Optimal Solution: 
This would involve just reverse the half of the original integer x and compare the reversed half with second half of the original integer.

```python

Class Solution: 
	def isPalindrome(self, x:int) -> int: 
		if x < 0 or (x %10 == 0 and x!= 0):
			return false
		rev_half = 0
		while x > rev_half: 
			rev_half = rev_half * 10 + x % 10
			x//=10
			
		return x == rev_half or x == rev_half //10 #for odd numbered integers, (rev no will be greater than the original integer x)
```

- So the above code only reverses the half of the given integer rather than reverse the whole given integer. 
- But still the time complexity remains the same because we ignore constants like it could have been like O(log x)/2 but that half is ignored. 
- So the time complexity is still O(log x) where x is the given integer. 
- log x reflects the number of digits in the given integer. So basically the number of digits is directly proportional to the logarithmic of the integer to the base of 10. 

```python
def isPlanidrome_string_method(x):
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]
```

**Explanation:**

- Reverse number using digits and compare.
    
- String method uses slicing (`[::-1]`) for simple solution.
    

>[!SUMMARY]
Two methods: digit reversal & string slicing.
-Handles negative check upfront.
    

> [!TIP]  
> For quick check, use string reversal. For optimized performance, go with integer math.

---

## Armstrong Number

### Problem Statement

Check if a number is Armstrong: sum of digits^number_of_digits = number.

```python
def basic_is_Armstrong(n):
    if n < 0:
        return False
    og_n = n
    num_digits = 0
    temp_n = n
    if temp_n == 0:
        num_digits = 1
    else:
        while temp_n:
            temp_n//=10
            num_digits+=1
    sum_of_powers = 0
    temp_n = og_n
    while temp_n:
        last_digit = temp_n % 10
        sum_of_powers += last_digit ** num_digits
        temp_n //= 10
    return sum_of_powers == og_n
```

```python
def string_Armstrong(n):
    if n < 0:
        return False
    s = str(n)
    num_digits = len(s)
    sum_of_powers = 0
    for char_digits in s:
        digit = int(char_digits)
        sum_of_powers += digit ** num_digits
    return n == sum_of_powers
```

**Explanation:**

- Count digits, raise each digit to that power, sum them.
    
- Return true if equal to original number.
    

>[!SUMMARY]
Works using both string and math methods.
Armstrong check involves digit powers.
    

> [!TIP]  
> Convert to string for simpler implementation.

---

## Prime Number

### Problem Statement

Check if a number is prime.

```python
def brute_force(n):
    cnt = 0
    for i in range(1,n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        print(f"The number {n} is prime number.")
    else:
        print(f"The number {n} is not a prime number.")
```

```python
def optimal_approach(n):
    print("This is the optimal_approach:")
    cnt = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt+=1
            if n//i != i:
                cnt+=1
    if cnt == 2:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
```

**Explanation:**

- Brute: check every number up to `n`.
    
- Optimal: check up to `sqrt(n)`.
    

>[!SUMMARY]
Prime has only two divisors.
Efficient check with square root.
    

> [!TIP]  
> Always reduce the loop to `sqrt(n)` for better performance.

---

## GCD and LCM

### Problem Statement

Find the GCD and LCM of two numbers.

```python
def brute_force(n,m):
    gcd = 1
    for i in range(1,min(m,n)+1):
        if n % i == 0 and m % i == 0:
            gcd = i
    return gcd
```

```python
def better_approach(n,m):
    for i in range(min(n,m),0,-1):
        if n % i == 0 and m % i == 0:
            return i
    return 1
```

```python
def optimal_approach(n,m):
    while n > 0 and m > 0:
        if n > m:
            n %= m
        else:
            m %= n
    return max(n,m)
```

```python
def brute_force_lcm(n,m):
    gcd = brute_force(n,m)
    lcm = abs(n * m) // gcd
    return lcm
```

**Explanation:**

- GCD: highest common factor.
    
- LCM = (n * m) // GCD
    
- Euclidean algo is the optimal method for GCD.
    

>[!SUMMARY]
3 methods for GCD: brute, better, optimal.
LCM is derived from GCD.
    

> [!TIP]  
> Use Euclidean method for GCD, then derive LCM.

---

## Divisors of a Number

### Problem Statement

Print all divisors of a number.

```python
def brute_force(n):
    print("\n Brute Force Approach: ")
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end = " ")
```

```python
def optimal(n):
    print("\n Optimal Approach: ")
    for i in range(1,int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(i, end=" ")
            if i != n//i:
                print(n//i, end= " ")
```

**Explanation:**

- Brute: check all numbers.
    
- Optimal: only till sqrt(n), print both divisors.
    

>[!SUMMARY]
Time reduced from O(n) to O(sqrt(n)).
    

> [!TIP]  
> Use sqrt(n) method and remember to check for symmetric divisors.

---

## Factorial of a Number

### Problem Statement

Find factorial of a number (n!).

```python
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1,n+1):
            result *= i
        return result
```

**Explanation:**

- Multiply all numbers from 1 to `n`.
    
- 0! = 1 by definition.
    

>[!SUMMARY]
-Factorial grows fast.
-Defined for non-negatives.


> [!TIP]  
> Use loops for efficiency; recursion may hit stack limit.

---

## Trailing Zeros in Factorial

### Problem Statement

Count trailing zeros in `n!`.

```python
def trailing_zeroes_in_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    count = 0
    i = 5
    while n//i >=1 :
        count += n//i
        i *= 5
    return count
```

**Explanation:**

- Count how many 5s are in the prime factorization.
    
- 2s are abundant; 5s decide zeros.
    

[!SUMMARY]

- Check powers of 5.
    
- Loop till `n//i` < 1.
    

> [!TIP]  
> Trailing zeros come from 2×5, and 5s are fewer. Count 5s.

---

## Nth Fibonacci Number

### Problem Statement

Find the nth Fibonacci number.

```python
def nth_fibonacci(n):
    if n < 0:
        return "Input cannot be negative number for fibonacci sequence."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b = 0,1
        for _ in range(2,n+1):
            a,b= b,a+b
        return b
```

**Explanation:**

- Fibonacci series starts with 0 and 1.
    
- Next number = sum of previous two.
    

[!SUMMARY]

- Iterative solution is memory efficient.
    

> [!TIP]  
> Use iteration to avoid recursive stack overflow for large n.