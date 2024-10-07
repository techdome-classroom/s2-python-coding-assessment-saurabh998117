def romanToInt(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    for i in range(len(s)):
        current = roman[s[i]]
        next_value = roman[s[i + 1]] if i + 1 < len(s) else 0

        if current < next_value:
            total -= current
        else:
            total += current

    return total

# Example usage:
# result = romanToInt('MCMXCIV')
# print(result) # Output will be 1994
