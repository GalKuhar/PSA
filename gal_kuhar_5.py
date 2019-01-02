# Naloga 5: Glasovanje
# Gal Kuhar, 27151078
# matematika, 2. letnik


def main():
    # N = št strank
    # M = št sestankov
    N, M = list(map(int, input().split()))

    # P = moč stranke
    P = list(map(int, input().split()))

    # V = glas stranke, 0 = false, 1 = true
    V = list(map(int, input().split()))

    # T = s katero stranko ima slkenjeno pogodbo o trajnem sodelovanju, na začetku vsaka sama s sabo
    T = [i for i in range(N)]

    def vodja(i):
        """vrne vodjo koalicije, ki ji pripada i-ta stranka"""
        if T[i] == i:  # stranka sama vodja
            return i

        else:
            x = T[i]
            if x == T[x]:  # če takoj povezava na vodjo  ni treba nič popravljati
                return x

            else:  # še popravimo vmesne člene
                seznam = [i]
                while x != T[x]:
                    seznam.append(x)
                    x = T[x]
                # tu pridemo do x = vodja koalicije

                for i in seznam:
                    # popravimo vse vmesne člene
                    T[i] = x

                return x

    for _ in range(M):
        S = list(map(int, input().split()))
        if len(S) == 3:
            x = V[vodja(S[0] - 1)] + V[vodja(S[1] - 1)] + V[vodja(S[2] - 1)]
            if x < 2:
                V[vodja(S[0] - 1)] = 0
                V[vodja(S[1] - 1)] = 0
                V[vodja(S[2] - 1)] = 0
            else:
                V[vodja(S[0] - 1)] = 1
                V[vodja(S[1] - 1)] = 1
                V[vodja(S[2] - 1)] = 1
        else:
            T[vodja(S[1] - 1)] = vodja(S[0] - 1)

    za = 0
    proti = 0
    for i in range(N):
        if V[vodja(i)] == 0:
            proti += P[i]
        else:
            za += P[i]

    print(str(za) + " " + str(proti))


main()
