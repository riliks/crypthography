import math
import random
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
def GOST94(text,p,q,a,x):
    if p>1 and a>1 and a<(p-1) and (a**q)%p==1 and x<q and (p-1)%q==0:
        return 'Ошибка переменных при вводе'
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя-:!?"
    h = 0
    for elem in text:
        h = pow(h + (abc.find(elem) + 1), 2) % p
    check=True
    while check:
        k=random.randint(1,q)
        r=((a**k)%p)%q
        if r!=0:
            check=False
    s=(x*r+k*h)%q
    y=(a**x)%p
    return r%(2**256),s%(2**256),y
def GOST94DE(text,p,q,a,rands):
    r,s,y=rands[0],rands[1],rands[2]
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя-:!?"
    h = 0
    for elem in text:
        h = pow(h + (abc.find(elem) + 1), 2) % p
    v=(h**(q-2))%q
    z1=(s*v)%q
    z2=((q-r)*v)%q
    u=(((a**z1)*(y**z2))%p)%q
    return u==r
def GOST12(text,a,b,p,G,xa,k):
    q=7
    x,y=G[0],G[1]
    x1, y1 = ECCmult(x, y, p, a)  # Db=Cb(G)
    if xa > 2:
        for i in range(2, xa):
            if xa / 2 == i:
                x1, y1 = ECCmult(x1, y1, p, a)
                break
            else:
                xtemp = x1
                ytemp = y1
                x1, y1 = ECCplus(x1, y1, x, y, p)
                x = xtemp
                y = ytemp
    Ya=x1,y1
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя-:!?"
    h = 0
    for elem in text:
        h = pow(h + (abc.find(elem) + 1), 2) % p
    k = random.randint(1, q)
    k=5
    x, y = G[0], G[1]
    x1, y1 = ECCmult(x, y, p, a)  # Db=Cb(G)
    if k > 2:
        for i in range(2, k):
            if k / 2 == i:
                x1, y1 = ECCmult(x1, y1, p, a)
                break
            else:
                xtemp = x1
                ytemp = y1
                x1, y1 = ECCplus(x1, y1, x, y, p)
                x = xtemp
                y = ytemp
    P=x1,y1
    r=x%q
    s=(k*h+r*xa)%q
    return r,s,Ya
def GOST12DE(text,p,a,G,rands):
    q=7
    r,s,Ya=rands[0],rands[1],rands[2]
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя-:!?"
    h = 0
    for elem in text:
        h = pow(h + (abc.find(elem) + 1), 2) % p
    if 0<r<q and 0<s<q:
        print('проверка успешна')
    else:
        return 'ошибка'
    u1=s*((h**(q-2))%q)%q
    u2=-r*((h**(q-2))%q)%q
    x, y = G[0], G[1]
    x1, y1 = ECCmult(x, y, p, a)  # Db=Cb(G)
    if u1 > 2:
        for i in range(2, u1):
            if u1 / 2 == i:
                x1, y1 = ECCmult(x1, y1, p, a)
                break
            else:
                xtemp = x1
                ytemp = y1
                x1, y1 = ECCplus(x1, y1, x, y, p)
                x = xtemp
                y = ytemp
    first=x1,y1
    x, y = Ya[0], Ya[1]
    x1, y1 = ECCmult(x, y, p, a)  # Db=Cb(G)
    if u2 > 2:
        for i in range(2, u2):
            if u2 / 2 == i:
                x1, y1 = ECCmult(x1, y1, p, a)
                break
            else:
                xtemp = x1
                ytemp = y1
                x1, y1 = ECCplus(x1, y1, x, y, p)
                x = xtemp
                y = ytemp
    second = x1, y1
    P = ECCplus(first[0], first[0], second[0], second[0], p)
    print(P[0]%q,r)
    return P[0]%q==r
# print(GOST94('жаба',11,5,2,6))
# print('||||')
# print(GOST94DE('жаба',31,5,2,GOST94('жаба',31,5,2,6)))
# print(GOST12('г',1,6,11,(0,1),4,4))
# print('   ')
# text="когдачеловексознательноилиинтуитивновыбираетсебевжизникакуюятоцель,жизненнуюзадачу,онневольнодаетсебеоценку.потомнужпределятьцельсвоегосуществования,ноцельдолжнабыть."
# print(GOST12DE(text,11,1,(0,1),GOST12(text,1,6,11,(0,1),4,4)))



