import random
def Difi(a,n):
    a=int(a)
    n=int(n)
    if 1<a<n:
        print('проверка прошла')
    else:
        return 'ошибка'
    first = random.randint(3, n-1)
    second = random.randint(3, n-1)
    Y1=(a**first)%n
    Y2=(a**second)%n
    if (Y1**second)%n==(Y2**first)%n and (Y1**second)%n!=1:
        return 'Успешно'
    else:
        return 'Тревога! Повторите генерацию ключей повторно'
