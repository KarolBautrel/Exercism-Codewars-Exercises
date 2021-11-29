def palindrome_counter(min_factor, max_factor):
    myList = []
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for a in (range(min_factor, max_factor+1)):
        for b in range(min_factor, max_factor+1):
            palindrome = a*b
            if str(palindrome) == str(palindrome)[::-1]:
                palindromeWithFactors = (palindrome, (a, b))
                yield palindromeWithFactors


print(palindrome_counter(1, 9))


def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    return max(palindrome_counter(min_factor, max_factor))


print(largest(1, 9))


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    return min(palindrome_counter(min_factor, max_factor))
