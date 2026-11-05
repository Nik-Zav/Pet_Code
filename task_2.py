from decimal import Decimal, getcontext

def pi_chudnovsky(precision: int) -> Decimal:
    """Вычисляет π с точностью до `precision` знаков после запятой."""
    getcontext().prec = precision + 10
    # Константы Чудновского
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = Decimal(L)

    for i in range(1, precision // 14 + 2):
        M = (K**3 - 16*K) * M // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    # Округляем до нужного количества знаков после запятой
    return +pi.quantize(Decimal(10) ** -precision)

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

    result = pi_chudnovsky(n)
    print(f"\nπ с точностью до {n} знаков после запятой:\n{result}")

if __name__ == "__main__":
    main()