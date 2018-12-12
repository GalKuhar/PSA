# Naloga 4: Lov na zaklad
# Gal Kuhar, 27151078
# matematika, 2. letnik

import sys


def main():
    N, M = list(map(int, input().split()))

    # v najhujšem primeru se sprehodimo po vseh vozliščih + nekaj dodatnih ???
    # 1 ni dovolj, 10 je - iz testov
    sys.setrecursionlimit(N + 10)

    graf = [[] for _ in range(N)]

    for _ in range(M):
        A, B, C = list(map(int, input().split()))
        graf[A - 1].append((B - 1, C))

    komponente, k, vKomponenti = tarjan(graf, N)

    # koliko zakladov v posamezni komponenti
    zakladi_v_komponenti = [0 for _ in range(k)]

    for i in range(k):
        zakladi_v_sosednjih = [0]
        for v in komponente[i]:
            for w, st_zakladov in graf[v]:
                if vKomponenti[w] == i:
                    zakladi_v_komponenti[i] += st_zakladov
                else:
                    zakladi_v_sosednjih.append(st_zakladov + zakladi_v_komponenti[vKomponenti[w]])

        zakladi_v_komponenti[i] += max(zakladi_v_sosednjih)

    for v in range(N):
        print(zakladi_v_komponenti[vKomponenti[v]])


def tarjan(graf, N):
    '''vrne seznam močno povezanih komponent in seznam v kateri komponenti je vozlišče'''
    # večinoma prekopiran z wikipedije

    # označimo v kateri komponenti so vozlišča, -1 še nepregledana
    index = [-1 for _ in range(N)]

    # temu mi pravili najbolj zgodnje vozlišče
    lowlink = [-1 for _ in range(N)]

    # sklad oz. stack
    S = []

    # označujemo še ali je na skladu
    onStack = [False for _ in range(N)]

    # seznam komponent
    komponente = []
    # k vozlišču napišemo v kateri komponenti je
    vKomponenti = [-1 for _ in range(N)]

    k = 0
    i = 0

    def strongconnect(v, i, k):

        index[v] = i
        lowlink[v] = i
        i += 1
        S.append(v)
        onStack[v] = True

        for w, _ in graf[v]:
            if index[w] == -1:
                i, k = strongconnect(w, i, k)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onStack[w]:
                lowlink[v] = min(lowlink[v], index[w])

        if lowlink[v] == index[v]:
            komponente.append([])

            while True:
                w = S.pop()
                onStack[w] = False

                #dodamo w v komponento k
                komponente[k].append(w)
                vKomponenti[w] = k
                if w == v:
                    break

            k += 1
        return i, k

    for v in range(N):
        if index[v] == -1:
            i, k = strongconnect(v, i, k)

    return komponente, k, vKomponenti


main()