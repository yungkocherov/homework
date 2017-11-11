import random


class Fishes:
    pass


class Bears:
    def __init__(self):
        self.nakopitel = 0


river = []
empty_walls = 0


def eco(length, procent_of_bear, procent_of_fish):
    global empty_walls
    global river
    kolvo_bears = int(procent_of_bear * 0.01 * length)
    kolvo_fishes = int(procent_of_fish * 0.01 * length)
    empty_walls = length - kolvo_bears - kolvo_fishes
    for i in range(kolvo_fishes):
        river.append(Bears())
    for i in range(kolvo_bears):
        river.append(Fishes())
    for i in range(empty_walls):
        river.append(None)
    random.shuffle(river)


def walking():
    global empty_walls
    global river
    next_step = True
    for i in range(len(river)):
        if next_step:
            if type(river[i]) == Bears:
                next_step = moving_of_medvedi(i)
            elif type(river[i]) == Fishes:
                next_step = moving_of_ribi(i)
        else:
            next_step = True


def new_index():
    global empty_walls
    global river
    if empty_walls > 0:
        k = random.randint(1, empty_walls)
        m = 0
        for i in range(len(river)):
            if river[i] is None:
                m += 1
                if m == k:
                    return i
    else:
        return -1


def new_animals(object):
    global empty_walls
    global river
    z = new_index()
    if z != -1:
        if object == 'b':
            river[z] = Bears()
        else:
            river[z] = Fishes()
        empty_walls -= 1


def moving_of_medvedi(i):
    global days_without_eating
    global empty_walls
    global river
    if i == 0:
        step = random.randint(0, 1)
    elif i == len(river) - 1:
        step = random.randint(-1, 0)
    else:
        step = random.randint(-1, 1)
    next_step = True
    if step == 1: next_step = False
    if step == 0:
        river[i].nakopitel += 1
        if river[i].nakopitel >= days_without_eating:
            river[i] = None
            empty_walls += 1
    else:
        if type(river[i + step]) == Fishes:
            river[i + step] = Bears()
            river[i] = None
            empty_walls += 1
        elif type(river[i + step]) == Bears:
            new_animals('b')
            river[i].nakopitel += 1
            if river[i].nakopitel >= days_without_eating:
                river[i] = None
                empty_walls += 1
            next_step = True
        else:
            kopilka = river[i].nakopitel
            river[i + step] = Bears()
            river[i] = None
            river[i + step].nakopitel = kopilka + 1
            if river[i + step].nakopitel >= days_without_eating:
                river[i + step] = None
                empty_walls += 1
    return next_step


def moving_of_ribi(i):
    global days_without_eating
    global empty_walls
    global river
    if i == 0:
        step = random.randint(0, 1)
    elif i == len(river) - 1:
        step = random.randint(-1, 0)
    else:
        step = random.randint(-1, 1)
    next_step = True
    if step == 1: next_step = False
    if step != 0:
        if type(river[i + step]) == Fishes:
            new_animals('f')
        elif type(river[i + step]) == Bears:
            river[i] = None
            empty_walls += 1
            river[i + step].nakopitel = 0
            next_step = True
        else:
            river[i] = None
            river[i + step] = Fishes()
    return next_step


length = int(input())
procent_of_bear = int(input())
procent_of_fish = int(input())
days_without_eating = int(input())
kolvo_shagov = int(input())
eco(length, procent_of_bear, procent_of_fish)

for i in range(kolvo_shagov):
    s = ''
    for j in range(length):
        if type(river[j]) == Bears:
            s += 'B'
        elif type(river[j]) == Fishes:
            s += 'F'
        else:
            s += '-'
    print(s)
    walking()
