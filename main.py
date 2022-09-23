def foo(n: int) -> int:
    """ Return difference between product and sum of digits in given integer """
    n_str = str(n)

    total, product = 0, 1
    for c in n_str:
        num = int(c)
        total += num
        product *= num

    return product - total 


if __name__ == "__main__":
    n = 234
    print(foo(n))
