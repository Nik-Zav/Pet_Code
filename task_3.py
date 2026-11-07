from decimal import Decimal, getcontext

def compute_e(precision: int) -> Decimal:
    """Вычисляет e с точностью до `precision` знаков после запятой."""
    getcontext().prec = precision + 10

    ONE = Decimal(1)
    e = ONE
    term = ONE
    k = 0

    threshold = Decimal(10) ** -(precision + 5)

    while term > threshold:
        k += 1
        term /= k
        e += term

    return +e.quantize(Decimal(10) ** -precision)

def main():
    MIN_PRECISION = 1
    MAX_PRECISION = 10_000

    try:
        n = int(input(f"Сколько знаков после запятой (от {MIN_PRECISION} до {MAX_PRECISION})? ").strip())
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    if not (MIN_PRECISION <= n <= MAX_PRECISION):
        print(f"Ошибка: число должно быть в диапазоне {MIN_PRECISION}..{MAX_PRECISION}.")
        return

    result = compute_e(n)
    print(f"\ne с точностью до {n} знаков после запятой:\n{result}")

if __name__ == "__main__":
    main()