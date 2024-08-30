#!/usr/bin/env python3

def print_fibonacci(length):
    if length < 0:
        print("Length must be a positive integer.")
        return
    
    fibonacci_sequence = []
    
    for n in range(length):
        if  n == 0:
            fibonacci_sequence.append(0)
        elif n == 1:
                fibonacci_sequence.append(1)
        else:
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    
    print(fibonacci_sequence)


print_fibonacci(9)  