abc = "абвгдежзийклмнопрстуфхцчшщьыъэюя"

tableMagma = [
    [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2],
    [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
    [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
    [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
    [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
    [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
    [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
    [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1]
]

key = "1223344556677fedcba987658899aabbccddeeff001432100123456789abcdef"


def GOST_Magma_Expand_Key(key):
    result = []
    for _ in range(3):
        result.extend(list(key[i:i + 8] for i in range(0, len(key), 8)))
    result.extend(list(reversed([key[i:i + 8] for i in range(0, len(key), 8)])))

    return result


def GOST_Magma_Add(masA, masB):
    result = []
    for i in range(4):
        result.append(str(hex(int(masA[i], 16) ^ int(masB[i], 16))))
    return result


def GOST_Magma_Add_32(masA, masB):
    result = []
    rest = 0
    for i in range(3, -1, -1):
        elem = int(masA[i], 16)
        key = int(f"0x{masB[i * 2:(i * 2) + 2]}", 16)
        rest = int(bin(elem + key + rest)[2::])
        if len(str(rest)) < 9:
            result.append(hex(int(f"0b{str(rest)}", 2)))
            rest = 0
        else:
            result.append(hex(int(f"0b{str(rest)[1::]}", 2)))
            rest = int(f"0b{str(rest)[0:1]}", 2)

    return list(reversed(result))


def GOST_Magma_T(masA):
    result = []

    for i in range(4):
        if len(masA[i][2::]) == 2:
            first_part_byte = f"{str(bin(int(masA[i][2:3], 16)))}"
            sec_part_byte = f"{str(bin(int(masA[i][3:4], 16)))}"
        else:
            first_part_byte = '0'
            sec_part_byte = f"{str(bin(int(masA[i][2:3], 16)))}"
        first_part_byte = tableMagma[i * 2][int(first_part_byte, 2)]
        sec_part_byte = tableMagma[i * 2 + 1][int(sec_part_byte, 2)]
        result.append(hex(int(f"0b{first_part_byte:>04b}{sec_part_byte:>04b}", 2)))

    return result


def GOST_Magma_g(key, masA):
    masB = GOST_Magma_Add_32(masA, key)
    masB = GOST_Magma_T(masB)

    masB = ''.join([f"{int(masB[i], 16):08b}" for i in range(4)])
    masB = masB[11::] + masB[0:11]
    masB = [hex(int(masB[i:i + 8], 2)) for i in range(0, len(masB), 8)]
    return masB


def GOST_Magma_G(key, masA):
    result = ['0', '0', '0', '0', '0', '0', '0', '0']
    a_0 = masA[4::]
    a_1 = masA[0:4]

    mas = GOST_Magma_g(key, a_0)
    mas = GOST_Magma_Add(a_1, mas)

    for i in range(4):
        a_1[i] = a_0[i]
        a_0[i] = mas[i]

    for i in range(4):
        result[i] = a_1[i]
        result[4 + i] = a_0[i]

    return result


def GOST_Magma_G_Fin(key, masA):
    result = ['0', '0', '0', '0', '0', '0', '0', '0']
    a_0 = masA[4::]
    a_1 = masA[0:4]

    mas = GOST_Magma_g(key, a_0)
    mas = GOST_Magma_Add(a_1, mas)

    for i in range(4):
        a_1[i] = mas[i]

    for i in range(4):
        result[i] = a_1[i]
        result[4 + i] = a_0[i]

    return result


def GOST_Magma_Encript(masA):
    keyAdd = GOST_Magma_Expand_Key(key)
    masA = GOST_Magma_G(keyAdd[0], masA)
    for i in range(1, 31, 1):
        masA = GOST_Magma_G(keyAdd[i], masA)
    return GOST_Magma_G_Fin(keyAdd[31], masA)


def GOST_Magma_Decript(masA):
    keyAdd = GOST_Magma_Expand_Key(key)
    masA = GOST_Magma_G(keyAdd[31], masA)
    for i in range(30, 0, -1):
        masA = GOST_Magma_G(keyAdd[i], masA)
    return GOST_Magma_G_Fin(keyAdd[0], masA)


def inc_ctr(masA):
    result = []
    rest = 0
    masB = '0000000000000001'
    for i in range(7, -1, -1):
        elem = int(masA[i], 16)
        key = int(f"0x{masB[i * 2:(i * 2) + 2]}", 16)
        rest = int(bin(elem + key + rest)[2::])
        #print(rest)
        if len(str(rest)) < 9:
            result.append(hex(int(f"0b{str(rest)}", 2)))
            rest = 0
        else:
            result.append(hex(int(f"0b{str(rest)[1::]}", 2)))
            rest = int(f"0b{str(rest)[0:1]}", 2)

    return list(reversed(result))


def add_xor(masA, masB):
    result = []
    for i in range(8):
        result.append(str(hex(int(masA[i], 16) ^ int(masB[i], 16))))
    return result


def CTR_Crypt(masA, masB):
    result = []
    for i in masB:
        mas = GOST_Magma_Encript(masA)
        masA = inc_ctr(masA)
        result.append(add_xor(i, mas))

    return result

def inter_CryptMa(text):
    temp = []
    for i in range(len(text)):
        temp.append(format(ord(text[i]), '04x')[:2])
        temp.append(format(ord(text[i]), '04x')[2:])

    count = 8 - (len(temp) % 8)
    for i in range(count):
        temp.append('00')

    open = []
    for i in range(0, len(temp), 8):
        open.append([f"0x{temp[i+j]}" for j in range(8)])

    return open

def inter_DecryptMa(text):
    result = ''
    for block in text:
        for i in range(0, len(block), 2):
            result += chr(int(block[i] + block[i+1][2::], 16))
    return result
# print("Шифр МАГМА Гаммирование")
# print('Шифрование: один дурак может больше спрашивать,чем десять умных ответить.')
# result = []
# strAdd = inter_CryptMa("один дурак может больше спрашивать,чем десять умных ответить.".replace(',', 'зпт').replace('.', 'тчк').replace(' ', ''))
# strAdd=[['0x92','0xde','0xf0','0x6b','0x3c','0x13','0x0a','0x59']]
# result = CTR_Crypt(['0x12', '0x34', '0x56', '0x78', '0x00', '0x00', '0x00', '0x00'], strAdd)
# print(result)
# print('Расшифрование')
# strAdd = []
# strAdd = (CTR_Crypt(['0x12', '0x34', '0x56', '0x78', '0x00', '0x00', '0x00', '0x00'], result))
