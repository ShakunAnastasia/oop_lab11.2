import math

def factorial(n):
    return math.factorial(n)

# 11.7 a
def finite_sequence_11_7_a(n):
    x = 1
    yield x
    for k in range(1, n+1):
        x /= factorial(2*k + 1)
        yield x

def infinite_sequence_11_7_a():
    x = 1
    yield x
    k = 1
    while True:
        x /= factorial(2*k + 1)
        yield x
        k += 1

# 11.7 b
def finite_sequence_11_7_b(n):
    x = 1
    yield x
    for k in range(2, n+1):
        x = ((-1)**k) * x / k
        yield x

def infinite_sequence_11_7_b():
    x = 1
    yield x
    k = 2
    while True:
        x = ((-1)**k) * x / k
        yield x
        k += 1

# 11.7 c 
def finite_sequence_11_7_c(n):
    x = 1
    yield x
    for k in range(1, n+1):
        x = ((-1)**k) * x / factorial(k*k + k)
        yield x

def infinite_sequence_11_7_c():
    x = 1
    yield x
    k = 1
    while True:
        x = ((-1)**k) * x / factorial(k*k + k)
        yield x
        k += 1

# 11.7 d 
def finite_sequence_11_7_d(n):
    x = 1
    yield x
    for k in range(1, n+1):
        x = (k + 1) * x / factorial(k)
        yield x

def infinite_sequence_11_7_d():
    x = 1
    yield x
    k = 1
    while True:
        x = (k + 1) * x / factorial(k)
        yield x
        k += 1

def print_sequence(seq_type, finite_gen, infinite_gen):
    print(f"\n11.7 {seq_type} - Кінцева послідовність (n={n}):")
    print(list(finite_gen))
    
    m = int(input(f"Скільки елементів вивести для нескінченної послідовності {seq_type}? "))
    print(f"Перші {m} елементів нескінченної послідовності {seq_type}:")
    print([next(infinite_gen) for _ in range(m)])

# MAIN #
if __name__ == "__main__":
    n = int(input("Введіть кількість елементів n для кінцевих послідовностей: "))
    
    print_sequence('a', finite_sequence_11_7_a(n), infinite_sequence_11_7_a())
    print_sequence('b', finite_sequence_11_7_b(n), infinite_sequence_11_7_b())
    print_sequence('c', finite_sequence_11_7_c(n), infinite_sequence_11_7_c())
    print_sequence('d', finite_sequence_11_7_d(n), infinite_sequence_11_7_d()) 
