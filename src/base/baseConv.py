base64_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890+-"


def encode(number:int) -> str:
    base64_representation = ""
    while number > 0:
        rem = number % 64
        base64_representation += base64_char[rem]
        number //= 64
    return base64_representation
def decode(rep:str) -> int:
    exp= 0
    total = 0
    for i in rep:
        quotient = base64_char.index(i)
        total += quotient*(64**exp)
        exp += 1
    return total
