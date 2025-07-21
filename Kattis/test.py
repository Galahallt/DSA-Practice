def permutations_with_repetition(s):
    base = len(s)
    for n in range(base**base):
        yield "".join(s[n // base ** (base - d - 1) % base] for d in range(base))
