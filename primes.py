"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [] # Empty list to fill with prime numbers
    num = 2 # First prime number 

    if number_of_primes <= 0:
        raise ValueError("Input must be greater than zero")

    # To give the number of prime wanted
    while len(list) < number_of_primes:
        is_prime = True

        # Checks if 'num' is divisible by any number from 2 to the square root of 'num'
        for number in range(2, int(num**0.5) + 1):
            if num % number == 0:
                is_prime = False
                break
        
        # Adds prime numbers to the list
        if is_prime:
            list.append(num) 

        num += 1 # Moves to the next num

        if number_of_primes == 0:
            raise ValueError("Input is 0!!!")

    return list

print(primes(10))

