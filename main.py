import numpy as np
from kuz import kuznechik
from kuz import kuznechik_de
import random
from difi import Difi
from GOSTS import GOST94DE,GOST94,GOST12DE,GOST12
import math
import random

def square(text, code):  # code=1 шифр code=2 дешифр
    abc = {"а": "11", "б": "12", "в": "13", "г": "14", "д": "15", "е": "16",
           "ж": "21", "з": "22", "и": "23", "й": "24", "к": "25", "л": "26",
           "м": "31", "н": "32", "о": "33", "п": "34", "р": "35", "с": "36",
           "т": "41", "у": "42", "ф": "43", "х": "44", "ц": "45", "ч": "46",
           "ш": "51", "щ": "52", "ъ": "53", "ы": "54", "ь": "55", "э": "56",
           "ю": "61", "я": "62"}
    new_txt = ""
    if (code == 1):
        for x in text:
            if x in abc:
                new_txt += abc.get(x) + ' '  # сначала находим, потом берем ее значение
            else:
                new_txt += (x + x) + ' '
        return new_txt
    else:
        list_fraze = []
        step = 2
        for i in range(0, len(text), 2):
            list_fraze.append(text[i:step])  # отбираем по 2 цифры
            step += 2
        key_abc_list = list(abc.keys())  # уходим от map к list
        val_abc_list = list(abc.values())
        for x in list_fraze:
            if x in val_abc_list:
                i = val_abc_list.index(x)
                new_txt += key_abc_list[i]
            else:
                new_txt += x[0:1]
        return new_txt
def caesar(text, key, code):  # code=1 шифр code=2 дешифр
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    list = ''
    if (code == 2):
        key = key * -1
    for i in text:
        list += (abc[(abc.find(i) + key) % len(abc)])
    return list
def atbash(text):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    return text.translate(str.maketrans(
        abc + abc.upper(), abc[::-1] + abc.upper()[::-1]))  # Создание двух стороннего словаря
def Del(text):
    text = text.replace('зпт', ',')
    text = text.replace('тчк', '.')
    text = text.replace('вск', '!')
    text = text.replace('впр', '?')
    return print(text)
def Trit(text):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    res = ''
    for i in range(len(text)):
        temp = (abc.find(text[i]) + i)
        if temp > 32:
            temp = temp % 32
        res = res + abc[temp]
    return res
def Tritde(text):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    res = ''
    for i in range(len(text)):
        temp = (abc.find(text[i]) - i)
        if temp < -32:
            while temp < 0:
                temp = temp + 32
        res = res + abc[temp]
    return res
def Bel(text, key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    res = ''
    for i in range(len(text)):
        keys = abc.find(key[i % len(key)])
        res = res + abc[((abc.find(text[i]) + keys) % 32)]
    return res
def Belde(text, key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    res = ''
    for i in range(len(text)):
        keys = abc.find(key[i % len(key)])
        res = res + abc[((abc.find(text[i]) - keys) % 32)]
    return res
def Viz(text, key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    res = ''
    text = key + text
    for i in range(1, len(text)):
        keys = abc.find(text[i - 1])
        res = res + abc[((abc.find(text[i]) + keys) % 32)]
    return res
def Vizde(text, key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    res = ''
    keys = abc.find(key)
    for i in range(0, len(text)):
        res = res + abc[((abc.find(text[i]) - keys) % 32)]
        keys = abc.find(res[i])
    return res
def Matr(text, key):
    key = key.replace('  ', '; ')
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    key = np.matrix(key)
    try:
        res = np.linalg.inv(key)  # Проверка на обратимость
    except:
        return 'Данный ключ не обратим'
    spisok = []
    result = ''
    if len(text) % 3 == 1:
        text = text + 'ъъ'
    elif len(text) % 3 == 2:
        text = text + 'ъ'
    for i in range(0, len(text), 3):
        spisok.append([abc.find(x) + 1 for x in list(text[i:i + 3])])
    for i in spisok:
        result += str(np.dot(key, i))
        result += ' '
    result = result.replace(']', '')
    return result.replace('[', '')
def MatrDe(text, key):
    key = key.replace('  ', '; ')
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    key = np.matrix(key)
    try:
        key = np.linalg.inv(key)  # Проверка на обратимость
    except:
        return 'Данный ключ не обратим'
    spisok=[]
    stroka = [int(elem) for elem in text.split()]
    for i in range(0, len(stroka), 3):
        spisok.append(list(stroka[i:i + 3]))
    result =[]
    for i in spisok:
        elem = np.dot(key, i).tolist()
        result.append([round(float(x)) for x in elem[0]])
    res=''
    for i in result:
        for j in i:
            res += abc[j - 1]
    return res
def Pleyf(text, word):
    stroka=text
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    if 'й' in word or 'ъ' in word:
        print('Неверный ключ')
        return
    for elem in abc:
        if elem != 'й' and elem != 'ъ':
            if not elem in word:
                word += elem

    key = ''
    for i in range(0, 30, 6):
        key = key + word[i:i + 6] + ' '
    key = key.split()
    result = ''
    spisok = []
    temp = ''
    count = 0

    for elem in stroka:
        if len(temp) == 1:
            if temp != elem:
                temp += elem
                spisok.append(temp)
                temp = ''
            else:
                temp += 'ф'
                count += 1
                spisok.append(temp)
                temp = elem
        else:
            temp += elem

    if (len(stroka) + count) % 2 == 1:
        spisok.append(stroka[-1] + 'ф')

    for elem in spisok:
        i0, j0, i1, j1 = -1, -1, -1, -1

        for n in range(len(key)):
            if i0 == -1:
                j0 = key[n].find(elem[0])
                if j0 != -1:
                    i0 = n
            if i1 == -1:
                j1 = key[n].find(elem[1])
                if j1 != -1:
                    i1 = n
            if i0 != -1 and i1 != -1:
                break

        if j0 == j1:
            result = result + key[(i0 + 1) % 5][j0]
            result = result + key[(i1 + 1) % 5][j1] + ' '
        elif i0 == i1:
            result = result + key[i0][(j0 + 1) % 6]
            result = result + key[i1][(j1 + 1) % 6] + ' '
        else:
            result = result + key[i0][j1]
            result = result + key[i1][j0] + ' '

    return result
def playferDe(stroka, word):
    print(stroka)
    result = ''
    key = ''
    if 'й' in word or 'ъ' in word:
        print('Неверный ключ')
        return
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    for elem in abc:
        if elem != 'й' and elem != 'ъ':
            if not elem in word:
                word += elem
    for i in range(0, 30, 6):
        key = key + word[i:i + 6] + ' '
    key = key.split()
    spisok = stroka.split()
    print(key)
    print(spisok)
    for elem in spisok:
        i0, j0, i1, j1 = -1, -1, -1, -1

        for n in range(len(key)):
            if i0 == -1:
                j0 = key[n].find(elem[0])
                if j0 != -1:
                    i0 = n
            if i1 == -1:
                j1 = key[n].find(elem[1])
                if j1 != -1:
                    i1 = n
            if i0 != -1 and i1 != -1:
                break

        if j0 == j1:
            result = result + key[(i0 - 1) % 5][j0]
            result = result + key[(i1 - 1) % 5][j1]
        elif i0 == i1:
            result = result + key[i0][(j0 - 1) % 6]
            result = result + key[i1][(j1 - 1) % 6]
        else:
            result = result + key[i0][j1]
            result = result + key[i1][j0]

    return result
def Vertperst(text, key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    var=[]
    vaultkey=[]
    for i in key:
        vaultkey.append(int(abc.find(i)))
        var.append('')
    for i in range(len(text)):
        var[i % len(key)]+=text[i]
    print(var)
    print(vaultkey)
    out=''
    for j in range(0,35):
        for i in range(len(vaultkey)):
            if j==vaultkey[i]:
                out+=(var[key.find(abc[j])])
    return out
def DeVertperst(text,key): #нажоеаапмямоттодкелсшттдтнтичиробшрвзесухеьдумтьпиьчеьывтк   дома
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    remains=len(text)%len(key)
    var=[]
    vaultkey = []
    for i in key:
        vaultkey.append(int(abc.find(i)))
        var.append('')
    print(var)
    print(vaultkey)
    size=len(text)//len(key)
    for j in range(0, 35):
        count=0
        for i in vaultkey:
            if j == i:
                if key.find(key[count])<remains:
                    var[key.find(key[count])]=text[0:size+1]
                    text=text[size+1::]
                    print(text)
                else:
                    var[key.find(key[count])] = text[0:size]
                    text = text[size::]
                    print(text)
            count += 1
    out=''
    print(var)
    for i in range(len(var[0])):
        for j in range(len(key)):
            try:
                out+=var[j][i]
            except:
                return out
    return out
def cardano(stroka):
    result = ''
    text=stroka
    to=len(stroka) // 60
    if to==0: to=1
    for k in range(0, to):
        stroka=text[k*60:(k+1)*60]
        table = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
               [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
               [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]
        res = []
        spisok = []


        for elem in stroka:
            spisok.append(elem)

        for i in range(len(table)):
            res.append([])

        for i in range(len(table)):
            for j in range(len(table[0])):
                res[i].append('')
                if table[i][j] and spisok:
                    res[i][j] = spisok.pop(0)
        table.reverse()

        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] and spisok:
                    res[i][j] = spisok.pop(0)
        for i in range(len(table)):
            table[i].reverse()

        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] and spisok:
                    res[i][j] = spisok.pop(0)
        table.reverse()

        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] and spisok:
                    res[i][j] = spisok.pop(0)

        for i in range(len(res)):
            for j in range(len(res[0])):
                if res[i][j]=='':
                    res[i][j]='ф'
                result += res[i][j]
    result=result.replace('фф','')
    resultf=' '
    for i in range(0,len(result)):
        if i%5==0:
            resultf+=' '
        resultf+=result[i]
    print(resultf)
    print(res)
    return result
def cardanoDe(stroka):
    result = ''
    text = stroka
    to = len(stroka) // 60
    if to == 0: to = 1
    for k in range(0, to):
        stroka = text[k * 60:(k + 1) * 60]
        table = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]
        res = []
        spisok = []

        for elem in stroka:
            spisok.append(elem)

        for i in range(len(table)):
            res.append([])
            for j in range(len(table[0])):
                res[i].append('')
                res[i][j]=stroka[0]
                stroka=stroka[1:len(stroka)]

        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] == 1:
                    result += res[i][j]
        table.reverse()

        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j]==1:
                    result += res[i][j]
        for i in range(len(table)):
            table[i].reverse()

        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j]==1:
                    result+=res[i][j]
        table.reverse()

        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j]==1:
                    result+=res[i][j]
    result = result.replace('фф', '')
    return result
def network(text,key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    var=''
    a=13
    c=7
    t=key
    for i in text:
        res=(abc.find(i)+t)%32
        t=(a*t+c)%32
        var+=abc[res]
    return var
def networkDe(text,key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя" # 10
    var = ''
    a = 13
    c = 7
    t = key # 5
    for i in text:
        res = (abc.find(i) + (32-t)) % 32
        t = (a * t + c) % 32  # 6 (27) 8 (5)
        var += abc[res]
    return var
def Gammir(text,key):
    compare=[['1100', '0100', '0110', '0010', '1010', '0101', '1011', '1001', '1110', '1000', '1101', '0111', '0000', '0011', '1111', '0001'], ['0110', '1000', '0010', '0011', '1001', '1010', '0101', '1100', '0001', '1110', '0100', '0111', '1011', '1101', '0000', '1111'], ['1011', '0011', '0101', '1000', '0010', '1111', '1010', '1101', '1110', '0001', '0111', '0100', '1100', '1001', '0110', '0000'], ['1100', '1000', '0010', '0001', '1101', '0100', '1111', '0110', '0111', '0000', '1010', '0101', '0011', '1110', '1001', '1011'], ['0111', '1111', '0101', '1010', '1000', '0001', '0110', '1101', '0000', '1001', '0011', '1110', '1011', '0100', '0010', '1100'], ['0101', '1101', '1111', '0110', '1001', '0010', '1100', '1010', '1011', '0111', '1000', '0001', '0100', '0011', '1110', '0000'], ['1000', '1110', '0010', '0101', '0110', '1001', '0001', '1100', '1111', '0100', '1011', '0000', '1101', '1010', '0011', '0111'], ['0001', '0111', '1110', '1101', '0000', '0101', '1000', '0011', '0100', '1111', '1010', '0110', '1001', '1100', '1011', '0010']]
    var=[]
    var_key=[] # из 16 букв
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюяъАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ-:!?"
    for elem in text:
        var.append(format(abc.find(elem), '08b'))
    for elem in key:
        var_key.append(format(abc.find(elem), '08b'))
    if len(var)%8:  #
        for i in range(0,8-len(var)%8):
            var.append('00000000')
    if len(var_key) % 32:  #
        for i in range(0, 32 - len(var_key) % 32):
            var_key.append('00000000')
    result=''
    for i in range(0,len(var),8): # пробегаемся по всем 64 битам
        first=var[i]+var[i+1]+var[i+2]+var[i+3]
        second=var[i+4]+var[i+5]+var[i+6]+var[i+7]
        count_key=0
        for l in range(0,32):
            key=var_key[count_key]+var_key[count_key+1]+var_key[count_key+2]+var_key[count_key+3]
            second_for_first = second
            if count_key==28:
                count_key=0
            else:
                count_key+=4
            res=''
            for j in range(0,32):
                temp=int(second[j]) ^ int(key[j]) # Ксор с ключом
                res+=str(temp)
            count_com=0
            secondres=''
            for j in range(0, 32,4): # Таблица . пробегается каждые 4 бита , 8 раз
                for k in range(0,len(compare[count_com])):
                    if int(compare[count_com][k])==int(res[j:j + 4]):
                        if count_com==7:
                            secondres += compare[0][k]
                        else:
                            secondres+=compare[count_com+1][k]
                if count_com==7:
                    count_com=0
                else:
                    count_com+=1
            second=secondres[11::]+secondres[0:11] #сдвиг
            res=''
            for j in range(0,32):
                temp=int(second[j]) ^ int(first[j]) # Ксор с первым
                res+=str(temp)
            second=res
            first=second_for_first
        result+=first+second
    return result
def GammirDe(text,key): # 1111011011110101001010110111111110001110011001101011110011001000            нач- 00001111000100000000100000000010 00000101000100100000110000000000
    compare = [
        ['1100', '0100', '0110', '0010', '1010', '0101', '1011', '1001', '1110', '1000', '1101', '0111', '0000', '0011',
         '1111', '0001'],
        ['0110', '1000', '0010', '0011', '1001', '1010', '0101', '1100', '0001', '1110', '0100', '0111', '1011', '1101',
         '0000', '1111'],
        ['1011', '0011', '0101', '1000', '0010', '1111', '1010', '1101', '1110', '0001', '0111', '0100', '1100', '1001',
         '0110', '0000'],
        ['1100', '1000', '0010', '0001', '1101', '0100', '1111', '0110', '0111', '0000', '1010', '0101', '0011', '1110',
         '1001', '1011'],
        ['0111', '1111', '0101', '1010', '1000', '0001', '0110', '1101', '0000', '1001', '0011', '1110', '1011', '0100',
         '0010', '1100'],
        ['0101', '1101', '1111', '0110', '1001', '0010', '1100', '1010', '1011', '0111', '1000', '0001', '0100', '0011',
         '1110', '0000'],
        ['1000', '1110', '0010', '0101', '0110', '1001', '0001', '1100', '1111', '0100', '1011', '0000', '1101', '1010',
         '0011', '0111'],
        ['0001', '0111', '1110', '1101', '0000', '0101', '1000', '0011', '0100', '1111', '1010', '0110', '1001', '1100',
         '1011', '0010']]
    var_key = []  # из 16 букв
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюяъАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ-:!?"
    for elem in key:
        var_key.append(format(abc.find(elem), '08b'))

    if len(var_key) % 32:  #
        for i in range(0, 32 - len(var_key) % 32):
            var_key.append('00000000')
    tempvar=[]
    for m in range(0,len(var_key),4):
        temp=var_key[m]+var_key[m+1]+var_key[m+2]+var_key[m+3]
        tempvar.append(temp)
    var_key=tempvar
    result = ''
    for i in range(0, len(text), 64):  # пробегаемся по всем 64 битам
        first = text[i:i+32]
        second = text[i+32:i+64]
        count_key = 7
        for l in range(0, 32):
            key = var_key[int(count_key)]
            tempsecond = second
            tempfirst = first
            second = first
            if count_key == 0:
                count_key = 7
            else:
                count_key -= 1
            res = ''
            for j in range(0, 32):
                temp = int(second[j]) ^ int(key[j])  # Ксор с ключом
                res += str(temp)
            count_com = 0
            secondres = ''
            for j in range(0, 32, 4):  # Таблица . пробегается каждые 4 бита , 8 раз
                for k in range(0, len(compare[count_com])):
                    if int(compare[count_com][k]) == int(res[j:j + 4]):
                        if count_com == 7:
                            secondres += compare[0][k]
                        else:
                            secondres += compare[count_com + 1][k]
                if count_com == 7:
                    count_com = 0
                else:
                    count_com += 1
            second = secondres[11::] + secondres[0:11]  # сдвиг
            res = ''
            for j in range(0, 32):
                temp = int(second[j]) ^ int(tempsecond[j])  # Ксор с первым
                res += str(temp)
            first = res
            second = tempfirst
        result += first + second
    tempres=''
    for set in range(0,len(result),8):
        temp=int(result[set:set+8], 2)
        tempres+=abc[temp]

    return tempres.replace('аа','')
def A51(text,key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    var_key=[]
    for elem in key:
        var_key.extend(format(abc.find(elem), '06b'))
    var=[]
    for elem in text:
        var.extend(format(abc.find(elem), '06b'))
    print(var)
    print(var_key)
    first = []
    second = []
    third = []
    count=0
    eltrue=False
    for i in var_key: # по массивам
        eltrue=False
        if count==0:
            if len(first)<19:
                first.append(i)
            else:
                count+=1
                eltrue=True
        if count==1:
            if len(second)<22:
                second.append(i)
            else:
                count += 1
                eltrue = True
        if count==2:
            if len(third)<23:
                third.append(i)
            else:
                count = 0
                eltrue = True
        if eltrue==False:
            if count==2:
                count=0
            else:
                count+=1
    res=''
    for letter in var:
        x=int(first[8])
        y=int(second[10])
        z=int(third[10])
        F=x&y|x&z|y&z
        finxor=[]
        if F==x:
            temp=first.pop(0)
            finxor.append(temp)
            temp=((int(temp)^int(first[1]))^int(first[2]))^int(first[5])
            first.append(temp)
        else:
            finxor.append(first[0])
        if F==y:
            temp=second.pop(0)
            finxor.append(temp)
            temp=int(temp)^int(second[1])
            second.append(temp)
        else:
            finxor.append(second[0])
        if F==z:
            temp=third.pop(0)
            finxor.append(temp)
            temp=int(temp)^int(third[1])^int(third[2])^int(third[15])
            third.append(temp)
        else:
            finxor.append(third[0])
        res+=str(int(letter)^int(finxor[0])^int(finxor[1])^int(finxor[2]))
    return res
def DeA51(text,key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    var_key = []
    for elem in key:
        var_key.extend(format(abc.find(elem), '06b'))
    first = []
    second = []
    third = []
    count = 0
    eltrue = False
    for i in var_key:  # по массивам
        eltrue = False
        if count == 0:
            if len(first) < 19:
                first.append(i)
            else:
                count += 1
                eltrue = True
        if count == 1:
            if len(second) < 22:
                second.append(i)
            else:
                count += 1
                eltrue = True
        if count == 2:
            if len(third) < 23:
                third.append(i)
            else:
                count = 0
                eltrue = True
        if eltrue == False:
            if count == 2:
                count = 0
            else:
                count += 1
    res = ''
    for letter in text:
        x = int(first[8])
        y = int(second[10])
        z = int(third[10])
        F = x & y | x & z | y & z
        finxor = []
        if F == x:
            temp = first.pop(0)
            finxor.append(temp)
            temp = ((int(temp) ^ int(first[1])) ^ int(first[2])) ^ int(first[5])
            first.append(temp)
        else:
            finxor.append(first[0])
        if F == y:
            temp = second.pop(0)
            finxor.append(temp)
            temp = int(temp) ^ int(second[1])
            second.append(temp)
        else:
            finxor.append(second[0])
        if F == z:
            temp = third.pop(0)
            finxor.append(temp)
            temp = int(temp) ^ int(third[1]) ^ int(third[2]) ^ int(third[15])
            third.append(temp)
        else:
            finxor.append(third[0])
        res += str(int(letter) ^ int(finxor[0]) ^ int(finxor[1]) ^ int(finxor[2]))
    result = ''
    for set in range(0, len(res), 6):
        temp = int(res[set:set + 6], 2)
        result += abc[temp]
    return result
def A52(text,key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    var_key = []
    for elem in key:
        var_key.extend(format(abc.find(elem), '06b'))
    var = []
    for elem in text:
        var.extend(format(abc.find(elem), '06b'))
    first = []
    second = []
    third = []
    R4=[]
    eltrue = False
    count=0
    for i in var_key:  # по массивам
        eltrue = False
        if count == 0:
            if len(first) < 19:
                first.append(i)
            else:
                count += 1
                eltrue = True
        if count == 1:
            if len(second) < 22:
                second.append(i)
            else:
                count += 1
                eltrue = True
        if count == 2:
            if len(third) < 23:
                third.append(i)
            else:
                count += 1
                eltrue = True
        if count == 3:
            if len(R4) < 17:
                R4.append(i)
            else:
                count = 0
                eltrue = True
        if eltrue == False:
            if count == 3:
                count = 0
            else:
                count += 1
    res = ''

    for letter in var:
        x = int(R4[3])
        y = int(R4[7])
        z = int(R4[10])
        F = x & y | x & z | y & z
        finxor = []
        finxor.append( first[0])
        finxor.append(second[0])
        finxor.append(third[0])
        res += str(int(letter) ^ int(finxor[0]) ^ int(finxor[1]) ^ int(finxor[2]) ^ (int(first[3])^ int(first[4])^ int(first[6]))^ (int(second[5])^ int(first[8])^ int(first[12]))^(int(third[4])^ int(third[6])^ int(third[9])))
        if F == x:
            temp = first.pop(0)
            temp = ((int(temp) ^ int(first[1])) ^ int(first[2])) ^ int(first[5])
            first.append(temp)
        if F == y:
            temp = second.pop(0)
            temp = int(temp) ^ int(second[1])
            second.append(temp)
        if F == z:
            temp = third.pop(0)
            temp = int(temp) ^ int(third[1]) ^ int(third[2]) ^ int(third[15])
            third.append(temp)
        tmp = R4.pop()
        tmp = int(R4[11])^int(tmp)
        R4.insert(0,tmp)
    return res
def DeA52(text,key):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    var_key = []
    for elem in key:
        var_key.extend(format(abc.find(elem), '06b'))
    first = []
    second = []
    third = []
    R4=[]
    eltrue = False
    count=0
    for i in var_key:  # по массивам
        eltrue = False
        if count == 0:
            if len(first) < 19:
                first.append(i)
            else:
                count += 1
                eltrue = True
        if count == 1:
            if len(second) < 22:
                second.append(i)
            else:
                count += 1
                eltrue = True
        if count == 2:
            if len(third) < 23:
                third.append(i)
            else:
                count += 1
                eltrue = True
        if count == 3:
            if len(R4) < 17:
                R4.append(i)
            else:
                count = 0
                eltrue = True
        if eltrue == False:
            if count == 3:
                count = 0
            else:
                count += 1
    res = ''
    for letter in text:
        x = int(R4[3])
        y = int(R4[7])
        z = int(R4[10])
        F = x & y | x & z | y & z
        finxor = []
        finxor.append( first[0])
        finxor.append(second[0])
        finxor.append(third[0])
        res += str(int(letter) ^ int(finxor[0]) ^ int(finxor[1]) ^ int(finxor[2]) ^ (int(first[3])^ int(first[4])^ int(first[6]))^ (int(second[5])^ int(first[8])^ int(first[12]))^(int(third[4])^ int(third[6])^ int(third[9])))
        if F == x:
            temp = first.pop(0)
            temp = ((int(temp) ^ int(first[1])) ^ int(first[2])) ^ int(first[5])
            first.append(temp)
        if F == y:
            temp = second.pop(0)
            temp = int(temp) ^ int(second[1])
            second.append(temp)
        if F == z:
            temp = third.pop(0)
            temp = int(temp) ^ int(third[1]) ^ int(third[2]) ^ int(third[15])
            third.append(temp)
        tmp = R4.pop()
        tmp = int(R4[11])^int(tmp)
        R4.insert(0,tmp)
    result = ''
    for set in range(0, len(res), 6):
        temp = int(res[set:set + 6], 2)
        result += abc[temp]
    return result
def kuz(text):
    res=0
    return res
def kuzde(text):
    return 0
def RSA(text):
    p=int(input('P= '))
    q=int(input('Q= '))
    if p%2==0 or q%2==0 or q%3==0 or p%3==0 or q%5==0 or p%5==0 or q%7==0 or p%7==0 and p!=7:
        return 'Ошибка данных при вводе'
    N=p*q
    fun=(p-1)*(q-1)
    e=1
    for i in range(1,14):
        if (fun%i)!=0:
            e=i
    q=[]
    p=[1]
    temp=e
    temp_f=fun
    while fun>1:
        q.append(int(fun/temp))
        temp_=temp
        temp=fun%temp
        fun=temp_
        if len(p)==1:
            p.append(p[-1]*q[-1])
        else:
            p.append((p[-2]+p[-1]) * q[-1])
    p.pop()
    fun=temp_f
    if len(p)%2==0:
        d=-p[-1]
        while d<0:
            d=d+fun
    else:
        d=p[-1]%fun
    res=""
    abc = " абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    for i in range(0,len(text)):
        res+=str((((abc.find(text[i]))**e)%N))+' '# abc
    print('E=',e)
    print("N=",N)
    print('D=',d)
    return res
def RSADE(text):
    d = int(input('D= ')) #43
    n = int(input('N= ')) #77
    var=[]
    var=text.split()
    res=''
    abc = " абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    for i in range(len(var)):
        res+=abc[(int(var[i])**d)%n]
    return res
def Elgamal(text):
    abc = " абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    p = int(input('P= '))
    g = int(input('G= '))
    x = int(input('X= '))
    if x<1 or x>p or p<g:
        return 'Ошибка данных при вводе'
    y=(g**x)%p
    k=[0,0,0]
    k[0] = int(input('k1= '))
    k[1] = int(input('k2= '))
    k[2] = int(input('k3= '))
    var=''
    if math.gcd(k[0], (p - 1)) != 1 and math.gcd(k[1], (p - 1)) != 1 and math.gcd(k[2], (p - 1)) != 1:
        return ' k не просто,взаимное'
    temp=0
    for i in range(0,len(text)):
        a=(g**k[temp])%p
        b=(y**k[temp])*((abc.find(text[i])))%p
        var+=str(a)+' '+str(b)+' ; '
        temp+=1
        if temp==3:
            temp=0
    return var
def ElgamalDe(text):
    x = int(input('x= '))
    fun_temp = int(input('P= '))
    var=text.split(';')
    for i in range(len(var)):
        var[i]=var[i].split()
    res=''
    abc = " абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    for i in range(len(var)):
        fun=fun_temp
        temp=(int(var[i][0])**x)%fun_temp
        q = []
        p = [1]
        while fun > 1:
            q.append(int(fun / temp))
            temp_ = temp
            temp = fun % temp
            fun = temp_
            if len(p) == 1:
                p.append(p[-1] * q[-1])
            else:
                p.append((p[-2] + p[-1]) * q[-1])
        p.pop()
        if len(p) % 2 == 0:
            d = (-p[-1])*int(var[i][1])
            while d < 0:
                d = d + fun_temp
        else:
            d = (p[-1]*int(var[i][1])) % fun_temp
        res += abc[d]
    return res
def ECCplus(x2, y2,x,y, Pmod):
    q = []
    temp = (x2-x) % Pmod
    b = (y2-y) % Pmod
    p = [1]
    fun = Pmod
    temp_f = fun
    while fun > 1:
        q.append(int(fun / temp))
        temp_ = temp
        temp = fun % temp
        fun = temp_
        if len(p) == 1:
            p.append(p[-1] * q[-1])
        else:
            p.append((p[-2] + p[-1]) * q[-1])
    p.pop()
    fun = temp_f
    if len(p) % 2 == 0:
        Y = -p[-1] * b % fun
        while Y < 0:
            Y = Y + fun
    else:
        Y = p[-1] * b % fun
    x3 = (Y ** 2 -x-x2) % Pmod
    y3 = (Y * (x - x3) - y) % Pmod
    return x3, y3
def ECCmult(x, y, Pmod, a):
    q = []
    temp = (2 * y) % Pmod
    b = 3 * (x ** 2) + a
    p = [1]
    fun = Pmod
    temp_f = fun
    while fun > 1:
        q.append(int(fun / temp))
        temp_ = temp
        temp = fun % temp
        fun = temp_
        if len(p) == 1:
            p.append(p[-1] * q[-1])
        else:
            p.append(p[-2] + (p[-1] * q[-1]))
    p.pop()
    fun = temp_f
    if len(p) % 2 == 0:
        Y = -p[-1]*b%fun
        while Y < 0:
            Y = Y + fun
    else:
        Y = p[-1]*b % fun
    x1=(Y**2-(2*x))%Pmod
    y1=(Y*(x-x1)-y)%Pmod
    return x1,y1
def ECC(text):
    a = int(input('a= '))
    G = (input('Элп.кривая = '))
    k = int(input('K= '))
    p = int(input('P= '))
    Cb = int(input('Сек.ключ= '))
    abc = " абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    var=[]
    for i in text:
        var.append(int(abc.find(i)))
    res=[]
    if var[0]==-1:
        var=[]
        var.append(text)
    for m in var:
        x = int(G[0:G.find(',')])
        y = int(G[G.find(',') + 1:len(G)])
        x1, y1 = ECCmult(x, y, p, a) #Db=Cb(G)
        if Cb>2:
            for i in range(2,Cb):
                if Cb / 2 == i:
                    x1, y1 = ECCmult(x1, y1, p, a)
                    break
                else:
                    xtemp=x1
                    ytemp=y1
                    x1, y1 = ECCplus(x1, y1,x,y,p)
                    x=xtemp
                    y=ytemp
        x1, y1 = ECCmult(x, y, p, a)  # [k]Db
        if k > 2:
            for i in range(2, k):
                if k/2==i:
                    x1, y1 = ECCmult(x1, y1, p, a)
                    break
                else:
                    xtemp = x1
                    ytemp = y1
                    x1, y1 = ECCplus(x1, y1, x, y, p)
                    x = xtemp
                    y = ytemp
        e = (int(m) * x1) % p
        x=int(G[0:G.find(',')]) # [k]G
        y=int(G[G.find(',')+1:len(G)])
        x1,y1=ECCmult(x,y,p,a)
        if k>2:
            for i in range(2,k):
                if k / 2 == i:
                    x1, y1 = ECCmult(x1, y1, p, a)
                    break
                else:
                    xtemp=x1
                    ytemp=y1
                    x1, y1 = ECCplus(x1, y1,x,y,p)
                    x=xtemp
                    y=ytemp
        res.append(e)
    return x1,y1,  res
def ECCDE(text):
    a = int(input('a= '))
    R = (input('Точка.Элп.кривая (R) = '))
    p = int(input('P= '))
    Cb = int(input('Сек.ключ= '))
    var=text.split(',')
    x = int(R[0:R.find(',')])
    y = int(R[R.find(',') + 1:len(R)])
    x1, y1 = ECCmult(x, y, p, a)
    if Cb > 2:
        for i in range(2, Cb):
            if Cb / 2 == i:
                x1, y1 = ECCmult(x1, y1, p, a)
                break
            else:
                xtemp = x1
                ytemp = y1
                x1, y1 = ECCplus(x1, y1, x, y, p)
                x = xtemp
                y = ytemp
    res=''
    abc = " абвгдежзийклмнопрстуфхцчшщъыьэюяъ-:!?"
    for e in var:
        q = [] # сравнение
        temp = x1
        b = int(e)
        pt = [1]
        fun = p
        temp_f = fun
        while fun > 1:
            q.append(int(fun / temp))
            temp_ = temp
            temp = fun % temp
            fun = temp_
            if len(pt) == 1:
                pt.append(pt[-1] * q[-1])
            else:
                pt.append((pt[-2] + pt[-1]) * q[-1])
        pt.pop()
        fun = temp_f
        if len(pt) % 2 == 0:
            m = -pt[-1] * b % fun
            while m< 0:
                m = m + fun
        else:
            m = pt[-1] * b % fun
        #res+=abc[m]
        res=m
    return res
def RSAP(text):
    # p = 17, q = 31, e = 7
    p = int(input('P= '))
    q = int(input('Q= '))
    e = int(input('e= '))
    if p % 2 == 0 or q % 2 == 0 or q % 3 == 0 or p % 3 == 0 or q % 5 == 0 or p % 5 == 0 or q % 7 == 0 or p % 7 == 0 and p != 7:
        return 'Ошибка данных при вводе'
    N = p * q
    if math.gcd(e, (p - 1) * (q - 1)) != 1:
        return ' Е не просто,взаимное'
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя-:!?"
    h=0
    for elem in text:
        h = pow(h + (abc.find(elem) + 1), 2) % p
    print(h)
    d = pow(e, ((p - 1) * (q - 1) - 1)) % ((p - 1) * (q - 1))
    res=pow(h, d) % N
    print(text)
    print('E=', e)
    print("N=", N)
    print('(секретный)D=', d)
    return res
def RSAPDE(text):
    num=int(text)
    N = int(input('N= '))  # 77
    E = int(input('E= '))  # 77
    m=(num**E) %N
    print(m)
    if num!=m:
        return 'подпись не верна!'
    return 'подпись верна!'
def ElgamalP(text):
    # 11,7,3
    p = int(input('p= '))
    x = int(input('x= '))  #
    g = int(input('g= '))  #
    if 1 < x & x < p-1 and 1 < g & g < p-1:
        l=1
    else:
        return 'ошибка'
    y = pow(g, x) % p
    print('y=',y)
    h = 0
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    for elem in text:
        m = pow(h + (abc.find(elem) + 1), 2) % p
    ki = [3]
    result = []
    a = pow(g, ki[0]) % p
    b = (m - pow(x, a) * pow(ki[0], m)) % (p - 1) # кузнечек, магма в гамировании
    result = [a, b]
    return result
def ElgamalPDE(text):
    # 11, *, 3, 9     27, -168
    p = int(input('p= '))
    var = input('получили= ')
    g = int(input('g= '))
    y = int(input('y= '))
    mas=var.split(',')
    h = 0
    print(mas)
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    for elem in text:
        m = pow(h + (abc.find(elem) + 1), 2) % p
    print(y,int(mas[0]),int(mas[1]),p)
    a1 = (pow(y, int(mas[0])) * pow(int(mas[0]), int(mas[1]))) % p
    a2 = (pow(g, m)) % p
    print(round(a1), a2)
    if (round(a1) == a2):
        res='Успех'
    else:
        res='Провал'
    return res

text = "один дурак может больше спрашивать,чем десять умных ответить."
cript = input('Ввод текста:').lower()
cript = cript.replace('.', 'тчк')
cript = cript.replace('?', 'впр')
cript = cript.replace('!', 'вск')
print('1.Атбаш (1.1-шифр, 1.2-расшиф)', '\n2.Цезарь (2.1-шифр, 2.2-расшиф)',
      '\n3.Квадрат Полибия (3.1-шифр, 3.2-расшиф)',
      '\n4.Шифр Тритемия (4.1-шифр, 4.2-расшиф)', '\n5.Шифр Белазо (5.1-шифр, 5.2-расшиф)',
      '\n6.Шифр Виженера (6.1-шифр, 6.2-расшиф)', '\n7.Митричный шифр (7.1-шифр, 7.2-расшиф)',
      '\n8.Шифр Плейфера (8.1-шифр, 8.2-расшиф)', '\n9.Вертикальная перестановка (9.1-шифр, 9.2-расшиф)', '\n10.Решетка Кардано(10.1-шифр, 10.2-расшиф)'
      , '\n11.Блокнот Шеннона(11.1-шифр, 11.2-расшиф)', '\n12.Гаммирование(12.1-шифр, 12.2-расшиф)', '\n13.A5/1(13.1-шифр, 13.2-расшиф)',
      '\n14.A5/2(14.1-шифр, 14.2-расшиф)','\n15.КУЗНЕЧИК(15.1-шифр, 15.2-расшиф)','\n16.RSA(16.1-шифр, 16.2-расшиф)','\n17.Elgamal(17.1-шифр, 17.2-расшиф)'
      ,'\n18.ECC(18.1-шифр, 18.2-расшиф)','\n19.RSAP(19.1-шифр, 19.2-расшиф)','\n20.ElgamalP(20.1-шифр, 20.2-расшиф)'
      ,'\n21.ГОСТ94','\n22.ГОСТ12','\n23.Difi')
choose = input('Выбор шифра:')
if choose!='18.2':
    if choose != '19.2':
        cript = cript.replace(',', 'зпт')
print('Текст для шифра: '+cript)
if (choose != '7.2'):
    if choose != '8.2':
        if choose != '16.2':
            if choose != '17.2':
                if choose != '18.2':
                        cript = cript.replace(' ', '')
if (choose == '2.1' or choose == '2.2' or choose == '11.1'or choose == '11.2'):
    key = int(input('ключ:'))
if (choose == '5.1' or choose == '5.2' or choose == '6.1' or choose == '6.2' or choose == '7.2' or choose == '7.1'or
        choose == '8.2' or choose == '8.1'or choose == '9.2' or choose == '9.1' or choose == '13.1' or choose == '13.2' or
        choose == '14.1'or choose == '14.2'or choose == '15.1'or choose == '15.2' or choose == '12.1'or choose == '12.2'):
    key = input('ключ:')
if (choose == '1.1'):
    print(atbash(cript))
elif (choose == '1.2'):
    Del(atbash(cript))
elif (choose == '2.1'):
    print(caesar(cript, key, 1))
elif (choose == '2.2'):
    Del(caesar(cript, key, 2))
elif (choose == '3.1'):
    print(square(cript, 1))
elif (choose == '3.2'):
    Del(square(cript, 2))
elif (choose == '4.1'):
    print(Trit(cript))
elif (choose == '4.2'):
    Del(Tritde(cript))
elif (choose == '5.1'):
    print(Bel(cript, key))
elif (choose == '5.2'):
    Del(Belde(cript, key))
elif (choose == '6.1'):
    print(Viz(cript, key))
elif (choose == '6.2'):
    Del(Vizde(cript, key))
elif (choose == '7.1'):
    print(Matr(cript, key))
elif (choose == '7.2'):
    print(MatrDe(cript, key))
elif (choose == '8.1'):
    print(Pleyf(cript, key))
elif (choose == '8.2'):
    Del(playferDe(cript, key))
elif (choose == '9.1'):
    print(Vertperst(cript, key))
elif (choose == '9.2'):
    Del(DeVertperst(cript, key))
elif (choose == '10.1'):
    print(cardano(cript))
elif (choose == '10.2'):
    Del(cardanoDe(cript))
elif (choose == '11.1'):
    print(network(cript,key))
elif (choose == '11.2'):
    Del(networkDe(cript,key))
elif (choose == '12.1'):
    print(Gammir(cript,key))
elif (choose == '12.2'):
    Del(GammirDe(cript,key))
elif (choose == '14.1'):
    print(A52(cript,key))
elif (choose == '14.2'):
    Del(DeA52(cript,key))
elif (choose == '13.1'):
    print(A51(cript,key))
elif (choose == '13.2'):
    Del(DeA51(cript,key))
elif (choose == '15.1'):
    print(kuznechik(cript,key))
elif (choose == '15.2'):
    Del(kuznechik_de(cript,key))
elif (choose == '16.1'):
    print(RSA(cript))
elif (choose == '16.2'):
    Del(RSADE(cript))
elif (choose == '17.1'):
    print(Elgamal(cript))
elif (choose == '17.2'):
    Del(ElgamalDe(cript))
elif (choose == '18.1'):
    print(ECC(cript))
elif (choose == '18.2'):
    print(ECCDE(cript))
elif (choose == '19.1'):
    print(RSAP(cript))
elif (choose == '19.2'):
    print(RSAPDE(cript))
elif (choose == '20.1'):
    print(ElgamalP(cript))
elif (choose == '20.2'):
    print(ElgamalPDE(cript))
elif (choose == '21'):
    print(GOST94DE(cript,31,5,2,GOST94(cript,31,5,2,6)))
elif (choose == '22'):
    print(GOST12DE(cript,11,1,(0,1),GOST12(cript,1,6,11,(0,1),4,4)))
elif (choose == '23'):
    print(Difi(cript,input('второе значение= ')))