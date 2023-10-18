def fibonacci_sequence(n, sequence=None):
    if sequence is None:
        sequence = []
    
    if n <= 0:
        return sequence
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci_sequence(n - 1, sequence)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

fib_sequence = fibonacci_sequence(999)
print(fib_sequence)
