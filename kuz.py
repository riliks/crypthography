text="когдачеловексознательноилиинтуитивновыбираетсебевжизникакуюятоцель,жизненнуюзадачу,онневольнодаетсебеоценку.потому,рад"
key = '8899aabbccddeeff0011223344556677 fedcba98765432100123456789abcdef'.split()
def on_bytes(stroka):
    temp = []
    for i in range(3, len(stroka), 2):
        temp.append(f'0x{stroka[i - 1]}{stroka[i]}')

    return temp


def mult_galua(a, b):
    pole = [8, 7, 6, 1, 0]
    a = format(a, '08b')
    b = format(b, '08b')

    pole_a = []
    pole_b = []
    for i in range(len(a)):
        if a[i] == '1':
            pole_a.append(7 - i)
        if b[i] == '1':
            pole_b.append(7 - i)

    mult_pole = []
    for i in range(len(pole_a)):
        for j in range(len(pole_b)):
            if not (pole_a[i] + pole_b[j]) in mult_pole:
                mult_pole.append(pole_a[i] + pole_b[j])
            else:
                mult_pole.pop(mult_pole.index(pole_a[i] + pole_b[j]))

    max_num = 0
    for elem in mult_pole:
        if elem > max_num:
            max_num = elem

    while max_num > 7:
        mult = max_num - 8  # x^14
        for i in range(len(pole)):
            if (pole[i] + mult) in mult_pole:
                mult_pole.pop(mult_pole.index(pole[i] + mult))
            else:
                mult_pole.append(pole[i] + mult)

        max_num = 0
        for elem in mult_pole:
            if elem > max_num:
                max_num = elem

        # print(mult_pole)

    res = 0
    for elem in mult_pole:
        res += 2 ** elem

    # print(res)
    return res


def L(stroka):
    arr = [1, 148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148]

    temp = stroka
    temp.reverse()

    for i in range(16):
        num = 0
        for j in range(len(temp)):
            num ^= mult_galua(int(temp[j], 16), arr[j])
        num = '0x' + format(num, '02x')

        for j in range(1, len(temp)):
            temp[j-1] = temp[j]
        temp[-1] = num
        # print(temp)

    temp.reverse()
    # print(temp)
    return temp


def S(stroka):
    res = []
    table = [252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147, 46, 153,
             186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142,
             79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72,
             171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183,
             93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117, 25, 61,
             255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169, 62, 168, 67, 201, 215, 121,
             214, 246, 124, 34, 185, 3, 224, 15, 236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167,
             151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140,
             163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137,
             225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9,
             91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166, 116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57,
             75, 99, 182]

    for elem in stroka:
        res.append('0x' + format(table[int(elem, 16)], '02x'))

    return res


def S_de(stroka):
    res = []
    table = [252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233, 119, 240, 219, 147, 46, 153,
             186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142,
             79, 5, 132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72,
             171, 242, 42, 104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183,
             93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117, 25, 61,
             255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245, 36, 169, 62, 168, 67, 201, 215, 121,
             214, 246, 124, 34, 185, 3, 224, 15, 236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167,
             151, 96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140,
             163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137,
             225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97, 32, 113, 103, 164, 45, 43, 9,
             91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166, 116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57,
             75, 99, 182]

    for elem in stroka:
        res.append('0x' + format(table.index(int(elem, 16)), '02x'))

    return res


def form_key(stroka):
    key = []
    first = on_bytes(hex(int(f'0x{stroka[0]}', 16)))
    second = on_bytes(hex(int(f'0x{stroka[1]}', 16)))

    key.append([first, second])

    array_const = []
    for i in range(1, 33):
        constant = hex(i)
        if len(constant) < 4:
            constant = f'0x{"0" * 30}0{constant[-1]}'
        else:
            constant = '0x' + ("0" * 30) + constant[2:]

        # создание констант
        array_const.append(L(on_bytes(constant)))

    count = 0
    for i in range(4):
        key.append(list(key[-1]))
        for k in range(8):
            # XOR ключа и константы
            temp = []
            for j in range(16):
                temp.append('0x' + format(int(key[-1][0][j], 16) ^ int(array_const[count][j], 16), '02x'))
            # print('XOR =', temp)

            # преобразование S
            temp = S(temp)
            # print('S() =', temp)

            # преобразование L
            temp = L(temp)
            # print('L() =', temp)

            # XOR ключей
            for j in range(16):
                temp[j] = '0x' + format(int(temp[j], 16) ^ int(key[-1][1][j], 16), '02x')

            key[-1][1] = key[-1][0]
            key[-1][0] = temp
            # print(key[-1])

            count += 1

    res = []
    for i in range(len(key)):
        res.append(key[i][0])
        res.append(key[i][1])

    return res


def kuznechik(stroka, key):
    stroka = on_bytes('0x' + stroka)

    key = form_key(key)

    # Первые 9 раундов
    for i in range(9):
        # побитовый XOR ключа и входного блока
        temp = []
        for j in range(16):
            temp.append('0x' + format(int(stroka[j], 16) ^ int(key[i][j], 16), '02x'))
        # print('X =', temp)

        # Нелинейное преобразование, простая замена
        temp = S(temp)
        # print('S =', temp)

        # Линейное преобразование
        temp = L(temp)
        # print('L =', temp)

        stroka = temp

    res = []
    for j in range(16):
        res.append('0x' + format(int(stroka[j], 16) ^ int(key[9][j], 16), '02x'))

    return res


def kuznechik_de(stroka, key):
    key = form_key(key)

    for i in range(9):
        temp = []
        for j in range(16):
            temp.append('0x' + format(int(stroka[j], 16) ^ int(key[9 - i][j], 16), '02x'))

        temp.reverse()
        temp = L(temp)
        temp.reverse()

        temp = S_de(temp)

        stroka = temp

    res = []
    for j in range(16):
        res.append('0x' + format(int(stroka[j], 16) ^ int(key[0][j], 16), '02x'))

    return res
# print(kuznechik('1122334455667700ffeeddccbbaa9988',key))
# temp = []
# for i in range(len(text)):
#     temp.append(format(ord(text[i]), '04x')[:2])
#     temp.append(format(ord(text[i]), '04x')[2:])
#
# count = 16 - (len(temp) % 16)
# for i in range(count):
#     temp.append('00')
#
# open = []
# for i in range(15, len(temp), 16):
#     block = ''
#     for j in range(i - 15, i + 1):
#         block += temp[j]
#     open.append(block)
#
# shifr = [kuznechik(x, key) for x in open]
# # print('SHIFR =', shifr)
#
# deshifr = [kuznechik_de(x, key) for x in shifr]
# # print('DESHIFR =', deshifr)
#
# # answer1 = []
# answer2 = ''
# for i in range(len(deshifr)):
#     for j in range(len(deshifr[i])):
#         deshifr[i][j] = deshifr[i][j][2:]
#         # shifr[i][j] = shifr[i][j][2:]
#     for j in range(1, len(deshifr[i]), 2):
#         answer2 += chr(int('0x' + deshifr[i][j - 1] + deshifr[i][j], 16))
#         # answer1.append(chr(int('0x' + shifr[i][j - 1] + shifr[i][j], 16)))
# print(text)
# print(shifr)
# print((answer2))