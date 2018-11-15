# Naloga 1: Sosedski Odnosi
# Gal Kuhar, 27151078
# matematika, 2. letnik

def stevilo_sosedskih_parov(naslovi, N, D):
    # najprej sortiramo list. To sicer v O(n log(n)) ampak vseeno zelo hitro)
    naslovi.sort()

    st_parov = 0
    max_sosed = 0
    st_sosedov = 0

    for st_cloveka in range(N - 1):
        naslov_cloveka = naslovi[st_cloveka]
        while max_sosed < N - 1 and naslovi[max_sosed+1] - naslov_cloveka <= D:
            max_sosed += 1
            st_sosedov += 1

        st_parov += st_sosedov
        st_sosedov -= 1

    return st_parov

def main():
    N, D = list(map(int, input().split()))
    seznam = list(map(int, input().split()))

    print(stevilo_sosedskih_parov(seznam, N, D))

main()