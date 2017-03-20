
def convert_int_to_binary_array(num):
    binary = [item for item in bin(num)]
    binary = binary[2:]  # remove the 0b
    return binary


def gen_gray_code(base_ten):
    base_ten = convert_int_to_binary_array(base_ten)
    stuff = [int(i) ^ int(j) for i, j in zip(base_ten, base_ten[1:])]
    stuff.insert(0, int(base_ten[0]))
    return stuff


def gen_gray_code_of_bitlength(bit_length):

    index = 0
    while True:
        value = gen_gray_code(index)
        if len(value) <= bit_length:
            index += 1
            yield ''.join(str(v) for v in value).zfill(bit_length)
        else:
            break


if __name__ == "__main__":
    length = 2
    codes = gen_gray_code_of_bitlength(length)
    print('GrayCodes of {} bit length'.format(length))
    for code in codes:
        print(code)
