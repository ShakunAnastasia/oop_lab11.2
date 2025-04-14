def finite_continued_fraction(n):
    for k in range(1, n + 1):
        result = 4 * k + 2
        for i in range(k - 1, 0, -1):
            result = 4 * i + 2 + 1 / result
        yield 2 + 1 / result


def infinite_continued_fraction():
    k = 1
    while True:
        result = 4 * k + 2
        for i in range(k - 1, 0, -1):
            result = 4 * i + 2 + 1 / result
        yield 2 + 1 / result
        k += 1


# MAIN #
if __name__ == "__main__":
    n = int(input("Введіть n для кінцевої послідовності: "))
    m = int(input("Скільки елементів вивести для нескінченної послідовності? "))
    
    print(f"\nКінцева послідовність (n={n}):")
    for value in finite_continued_fraction(n):
        print(f"{value:.10f}", end=" ")
    
    print(f"\n\nПерші {m} елементів нескінченної послідовності:")
    infinite_gen = infinite_continued_fraction()
    for _ in range(m):
        print(f"{next(infinite_gen):.10f}", end=" ")
