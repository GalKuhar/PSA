# Naloga 2: Podkupnine
# Gal Kuhar, 27151078
# matematika, 2. letnik

def main_final():
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


main_final()