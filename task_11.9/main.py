import math

def factorial(n):
    return math.factorial(n)

# 11.9 a 
def finite_sequence_11_9_a(n):
    for i in range(2, n + 1):
        yield (1 - 1 / (i ** 2))

def infinite_sequence_11_9_a():
    i = 2
    while True:
        yield (1 - 1 / (i ** 2))
        i += 1

# 11.9 b 
def finite_sequence_11_9_b(n):
    for i in range(1, n + 1):
        yield (2 + 1 / factorial(i))

def infinite_sequence_11_9_b():
    i = 1
    while True:
        yield (2 + 1 / factorial(i))
        i += 1

# 11.9 c
def finite_sequence_11_9_c(n):
    for i in range(1, n + 1):
        yield (i + 1) / (i + 2)

def infinite_sequence_11_9_c():
    i = 1
    while True:
        yield (i + 1) / (i + 2)
        i += 1

def print_sequence(seq_type, finite_gen, infinite_gen):
    print(f"\n11.9 {seq_type} - Кінцева послідовність (n={n}):")
    print(list(finite_gen))
    
    m = int(input(f"Скільки елементів вивести для нескінченної послідовності {seq_type}? "))
    print(f"Перші {m} елементів нескінченної послідовності {seq_type}:")
    inf_gen = infinite_gen()
    print([next(inf_gen) for _ in range(m)])

# MAIN #
if __name__ == "__main__":
    n = int(input("Введіть кількість елементів n для кінцевих послідовностей: "))
    
    print_sequence('a', finite_sequence_11_9_a(n), infinite_sequence_11_9_a)
    print_sequence('b', finite_sequence_11_9_b(n), infinite_sequence_11_9_b)
    print_sequence('c', finite_sequence_11_9_c(n), infinite_sequence_11_9_c)
