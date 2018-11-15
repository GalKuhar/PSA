# Naloga 2: Podkupnine
# Gal Kuhar, 27151078
# matematika, 2. letnik

def main1():
    st_primerov = int(input())
    for _ in range(st_primerov):
        # poberemo prazno vrstico
        input()

        n, m, q, t = list(map(int, input().split()))

        # naredimo list dolzine n, i-ti element predstavlja zep i-tega birokrata, na zacetku vsi zepi prazni
        birokrati = [0] * n
        for ponudnik in range(m):
            a, b, c = list(map(int, input().split()))
            for i in range(a - 1, b):
                p = birokrati[i]
                p += c
                if p >= t:
                    p -= t
                birokrati[i] = p

        birokrati.reverse()
        polinom = 0
        for p in birokrati:
            polinom = (polinom * q) % t + p

        print(polinom)

def main2():
    st_primerov = int(input())
    for _ in range(st_primerov):
        # poberemo prazno vrstico
        input()

        polinom = 0

        n, m, q, t = list(map(int, input().split()))

        powmodlist_q = powmodlist(n, q, t)

        for ponudnik in range(m):
            a, b, c = list(map(int, input().split()))

            # to geometrijska vrsta za q. Na zalost ne deluje v mod t, zato na star nacin
            podpolinom = 0
            for i in range(a - 1, b):
                podpolinom += powmodlist_q[i]
                podpolinom %= t

            polinom += (c * podpolinom) % t
            polinom %= t

        print(polinom)

def main3():
    st_primerov = int(input())
    for _ in range(st_primerov):
        # poberemo prazno vrstico
        input()

        polinom = 0

        n, m, q, t = list(map(int, input().split()))

        powmodlist_q = powmodlist(n, q, t)
        powlist_q = powlist(n, q)

        for ponudnik in range(m):
            a, b, c = list(map(int, input().split()))

            podpolinom = 0
            # zrtvujemo to, da moramo zracunati q**n, da lahko tu spustimo sum.
            # bo to dovolj hitro?
            podpolinom = ((powlist_q[b - a + 1] - 1) // (q - 1)) % t
            podpolinom = (podpolinom * powmodlist_q[a - 1]) % t

            polinom += (c * podpolinom) % t
            polinom %= t

        print(polinom)

def main4():
    st_primerov = int(input())
    for _ in range(st_primerov):
        # poberemo prazno vrstico
        input()

        polinom = 0

        n, m, q, t = list(map(int, input().split()))

        powmodlist_q = powmodlist(n, q, t)

        for ponudnik in range(m):
            a, b, c = list(map(int, input().split()))

            podpolinom = 0
            # zrtvujemo to, da moramo zracunati q**n, da lahko tu spustimo sum.
            # bo to dovolj hitro?
            podpolinom = ((q **(b - a + 1) - 1) // (q - 1)) % t
            podpolinom = (podpolinom * powmodlist_q[a - 1]) % t

            polinom += (c * podpolinom) % t
            polinom %= t

        print(polinom)

def main5():
    st_primerov = int(input())
    for _ in range(st_primerov):
        # poberemo prazno vrstico
        input()

        polinom = 0

        n, m, q, t = list(map(int, input().split()))

        for ponudnik in range(m):
            a, b, c = list(map(int, input().split()))

            podpolinom = 0
            # zrtvujemo to, da moramo zracunati q**n, da lahko tu spustimo sum.
            # bo to dovolj hitro?
            podpolinom = ((q **(b - a + 1) - 1) // (q - 1)) % t
            podpolinom = (podpolinom * pow(q, a - 1, t)) % t

            polinom += (c * podpolinom) % t
            polinom %= t

        print(polinom)

def main6():
    # ideja nadaljevanje main2: kaj pa ce ne bi vsakic posebej racunali sum geometrijske vrste?
    st_primerov = int(input())
    for _ in range(st_primerov):
        # poberemo prazno vrstico
        input()

        polinom = 0

        n, m, q, t = list(map(int, input().split()))

        powsumlist_q = powsumlist(n, q, t)

        for ponudnik in range(m):
            a, b, c = list(map(int, input().split()))

            podpolinom = powsumlist_q[b] - powsumlist_q[a - 1]
            podpolinom %= t

            polinom += (c * podpolinom) % t
            polinom %= t

        print(polinom)

def powmodlist(n, q, t):
    # generira seznam 1, q % t, q^2 % t, ... q^n-1 % t
    pow = q % t
    powmodlist_q = [1]
    for i in range(n - 1):
        powmodlist_q.append(pow)
        pow = (pow * q) % t
    return powmodlist_q

def powlist(n, q):
    # ta zna biti ZELO pocasen
    # prekoraci spomin
    pow = q
    powlist_q = [1]
    for i in range(n):
        powlist_q.append(pow)
        pow *= q
    return powlist_q

def powsumlist(n, q, t):
    # za 4, 10, 10000 vrne [0,1,11,111,1111]
    sum = 1
    pow = q % t
    powsumlist_q = [0]
    for i in range(n):
        powsumlist_q.append(sum)
        sum += pow
        sum %= t
        pow = (pow * q) % t

    return powsumlist_q

main6()