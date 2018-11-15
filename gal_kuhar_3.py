# Naloga 3: Go
# Gal Kuhar, 27151078
# matematika, 2. letnik


N = 19
st_potez = 1000

def igraj(x0, y0, barva, plosca):
    '''igra potezo, vrne true in novo plosco ce poteza uspesna, false z zacetno plosco sicer'''
    # ne moremo igrati na polno polje
    if plosca[y0 - 1][x0 - 1] != ".":
        return False, plosca

    # kamen damo na polje, da lahko preverjamo
    plosca[y0 - 1][x0 - 1] = barva
    nasprotna = nasprotna_barva(barva)

    # najprej preverimo ce smo s tem kamnom ubili kaksnega soseda.
    for x, y in sosedi(x0, y0):
        # pogledamo ce je sosed nasprotne barve
        if plosca[y - 1][x - 1] == nasprotna:
            live, pomozna_plosca = is_alive(x, y, nasprotna, plosca)
            # ce smo ga ubili
            if not live:
                # spucamo jih s plosce
                plosca = kill(plosca, pomozna_plosca)

    # preverimo ce je kamen sam ziv
    if is_alive(x0, y0, barva, plosca)[0]:
        # ce kamen ziv to ok poteza
        return True, plosca

    # ce kamn ni ziv je potem mrtev in ga umaknemo s polja
    plosca[y0 - 1][x0 - 1] = "."
    return False, plosca


def is_alive(x0,y0, barva, plosca, pomozna_plosca=None):
    '''preveri ali je kamen ziv'''
    # najprej osnoven test:
    for (x, y) in sosedi(x0,y0):
        # ce med sosedi najde praznega, je ziv
        if plosca[y - 1][x - 1] == ".":
            return True, pomozna_plosca

    # ce ni zacnemo dfs:
    # najprej naredimo pomozno plosco, ce je se nimamo
    if pomozna_plosca == None:
        pomozna_plosca = [[0 for _ in range(N)] for _ in range(N)]

    # oznacimo, da smo trenutnega ga ze preiskali
    pomozna_plosca[y0 - 1][x0 - 1] = 1
    for (x, y) in sosedi(x0, y0):
        # ce je iste barve in ga se nismo preiskali:
        if plosca[y - 1][x - 1] == barva and pomozna_plosca[y - 1][x - 1] == 0:
            # tukaj, da dobimo ven pomozno plosco, ker hocem na koncu vse povezane imeti na seznamu
            live, pomozna_plosca = is_alive(x, y, barva, plosca, pomozna_plosca)
            if live:
                return True, pomozna_plosca

    # ce noben njegov sosed ni ziv, je mrtev
    return False, pomozna_plosca


def kill(plosca, pomozna_plosca):
    '''ubije oznacene kamne'''
    for x in range(N):
        for y in range(N):
            if pomozna_plosca[y - 1][x - 1] == 1:
                plosca[y - 1][x - 1] = "."
    return plosca


def sosedi(x,y):
    '''vrne sosednja polja v obliki (x,y)'''
    sosedje = []
    if x > 1:
        sosedje.append((x - 1, y))
    if x < N:
        sosedje.append((x + 1, y))
    if y > 1:
        sosedje.append((x, y - 1))
    if y < N:
        sosedje.append((x, y + 1))
    return(sosedje)


def nasprotna_barva(barva):
    if barva == "B":
        return "W"
    else:
        return "B"


def print2(plosca):
    for i in range(N):
        str = ""
        for j in range(N):
            str += plosca[i][j]
        print(str)


def main():
    plosca = [["." for _ in range(N)] for _ in range(N)]
    barva = "B"

    for _ in range(st_potez):
        try:
            x, y = list(map(int, input().split()))
            veljavna, plosca = igraj(x, y, barva, plosca)

            if veljavna:
                barva = nasprotna_barva(barva)

        except ValueError:
            break
        except EOFError:
            break

    print2(plosca)


main()