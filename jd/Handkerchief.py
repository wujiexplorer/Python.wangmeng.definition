def fnA(p, personNum, cnt):
    times = cnt // personNum + 1
    temp = [];

    for t in range(times):
        temp = temp + p

    p2 = p[:]
    p2.remove(temp[cnt-1])
    return p2


def fnB(p, cnt):
    pa = p[:cnt-1]
    pb = p[cnt:]
    p = pb + pa
    return p


cnt = 9   #M
personNum = 30   #N

persons = ["p"+ str(x) for x in range(1, personNum+1)]
print(persons)

personNum = len(persons)
if cnt < personNum:
    while True:
        persons = fnB(persons, cnt)
        print(len(persons))
        print(persons)
        if len(persons) <= cnt:
            break


personNum = len(persons)
while True:
    persons = fnA(persons, personNum, cnt)
    print(len(persons))
    print(persons)
    if len(persons) == 1:
        break
    else:
        personNum = personNum - 1;