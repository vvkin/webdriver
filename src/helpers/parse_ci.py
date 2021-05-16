scales = {
    'K': 10**3, 
    'M': 10**6
}

def prepare_literal(literal: str) -> str:
    return literal.strip().replace(',', '')

def scale_number(number: float) -> int:
    if (number < 10**3): return int(number)
    scale = 'M' if number > 10**6 else 'K'
    return int(number - (number % scales[scale]))

def parse_int(literal: str) -> int:
    prepared_literal = prepare_literal(literal)
    last_char = prepared_literal[-1]
    
    if last_char in scales:
        result = float(prepared_literal[:-1]) * scales[last_char]
    else: result = float(prepared_literal)
    
    return scale_number(result)
