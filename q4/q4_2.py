class Tpol:
    def __init__(self, s):
        self.stepen = []
        self.koef = []
        self.p = s
        self.razd()

    def razd(self):
        m = self.p
        pol = []
        if m[0] != '-':
            m = '+' + m
        while len(m) != 0:
            if m.rfind('+') < m.rfind('-'):
                pol.append(m[m.rfind('-'):])
                m = m[:m.rfind('-')]
            else:
                pol.append(m[m.rfind('+'):])
                m = m[:m.rfind('+')]
        k = self.koef
        s = self.stepen
        for i in range(len(pol)):
            a = pol.pop()
            if a.find('x') == -1:
                s.append(0)
                k.append(float(a))
            elif a.find('^') != -1:
                s.append(int(a[a.find('^') + 1:]))
                k.append(float(a[:a.find("x") - 1]))
            else:
                s.append(1)
                k.append(float(a[:a.find("x") - 1]))

        self.koef = k
        self.stepen = s

    def proiz(self):
        k1 = []
        s1 = []
        for i in range(len(self.koef)):
            k1.append(self.koef[i] * (self.stepen[i]))
            s1.append(self.stepen[i] - 1)
        dif = ''

        for i in range(len(k1)):
            k1[i] = floatToInt(k1[i])

        for i in range(len(k1)):
            if k1[i] == 0:
                pass
            elif s1[i] == 0:
                if k1[i] > 0:
                    dif += '+' + str(k1[i])
                else:
                    dif += str(k1[i])
            elif s1[i] == 1:
                if k1[i] > 0:
                    dif += '+' + str(k1[i]) + '*x'
                else:
                    dif += str(k1[i]) + '*x'
            else:
                if k1[i] > 0:
                    dif += '+' + str(k1[i]) + '*x^' + str(s1[i])
                else:
                    dif += str(k1[i]) + '*x^' + str(s1[i])
        if dif[0] == '+': dif = dif[1:]
        print(dif)


def floatToInt(x):
    if x - int(x) == 0:
        return int(x)
    else:
        return x

print('Вид полинома: 6*x^5-0.25*x^4+1*x-25')
z = input('Введите полином: ')
y = Tpol(z)
y.proiz()
