def primecheck(n):
    if n < 2:
        return False
    for i in range(2, int(n * 0.5)+1):
        if n % i ==0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if primecheck(num)]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


prime_numbers = filter_prime(numbers)
print("Prime numbers:", prime_numbers)