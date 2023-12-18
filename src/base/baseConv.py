base64_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890+/"


def encode(number:int) -> str:
    base64_representation = ""
    while number > 0:
        rem = number % 64
        base64_representation += base64_char[rem]
        number //= 64
    return base64_representation
def decode(rep:str) -> int:
    num = 0
    for i in rep:
        num = num*64 + base64_char.index(i)
    return num
