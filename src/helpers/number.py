SCALES = {
    'K': 10**3,
    'M': 10**6,
}


def scale_int(number: int) -> int:
    if (number < 10**3): return int(number)
    scale = 'M' if number > 10**6 else 'K'
    return int(number - (number % SCALES[scale]))


def parse_int(string: str) -> int:
    literal = string.strip().replace(',', '')
    if (last_char := literal[-1]) in SCALES:
        return int(literal[:-1]) * SCALES[last_char]
    else: return int(literal)
