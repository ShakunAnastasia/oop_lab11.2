def finite_sequence_11_8_a(n):
    for k in range(1, n + 1):
        yield (-1) ** (k + 1) * k

def infinite_sequence_11_8_a():
    k = 1
    while True:
        yield (-1) ** (k + 1) * k
        k += 1

def finite_sequence_11_8_b(n):
    for k in range(1, n + 1):
        yield 1 / (k * (k + 1))

def infinite_sequence_11_8_b():
    k = 1
    while True:
        yield 1 / (k * (k + 1))
        k += 1

def finite_sequence_11_8_c(n):
    for k in range(2, n + 1):
        yield ((-1) ** k) * (k - 1) / k

def infinite_sequence_11_8_c():
    k = 2
    while True:
        yield ((-1) ** k) * (k - 1) / k
        k += 1

def print_sequence(seq_type, finite_gen, infinite_gen):
    print(f"\n11.8 {seq_type} - Кінцева послідовність (n={n}):")
    print(list(finite_gen))
    
    m = int(input(f"Скільки елементів вивести для нескінченної послідовності {seq_type}? "))
    print(f"Перші {m} елементів нескінченної послідовності {seq_type}:")
    print([next(infinite_gen) for _ in range(m)])

# MAIN #
if __name__ == "__main__":
    n = int(input("Введіть кількість елементів n для кінцевих послідовностей: "))
    
    print_sequence('a', finite_sequence_11_8_a(n), infinite_sequence_11_8_a())
    print_sequence('b', finite_sequence_11_8_b(n), infinite_sequence_11_8_b())
    print_sequence('c', finite_sequence_11_8_c(n), infinite_sequence_11_8_c())
