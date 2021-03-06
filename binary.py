import re
class binary:
    # Encode
    def str_binary(x: str):
        return (' ').join(re.findall('.{1,8}', ''.join(format(ord(i), '08b') for i in x)))

    # Decode
    def binary_str(y: int):
        y = int(y.replace(' ', ''), 2)
        return y.to_bytes((y.bit_length() + 7) // 8, 'big').decode()

    # Decode1 (*unnessesary code)
    def binary_str1(y: chr):
        return chr(int(y, 2))


# "Menu"
opt = input(" 1 > str to binary\n 2 > binary to str\n\nOption: ")
if opt.startswith("1"):
    x = input("String: ")
    print(binary.str_binary(x))
elif opt.startswith("2"):
    y = input("Binary: ")
    print(binary.binary_str(y))
else:
    exit("Invalid Option")
