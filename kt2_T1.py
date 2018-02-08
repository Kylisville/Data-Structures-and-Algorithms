
def sekoita(v, avain):
    tulos = [0] * 5
    try:
        for k in range(0, v[-1]):
            paikka=avain[k]
            tulos[paikka]=v[k]
    except IndexError:
        pass
    return tulos

viesti = [79, 73, 75, 69, 65]
avain = [1, 3, 0, 4, 2]
print sekoita(viesti,avain)
