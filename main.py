def repartir(catils):
    return [int(catils / 3), catils % 3]


def situacion(catils):
    # Situación inicial
    reparticiones = [[catils, 0]]

    # Repartición de los 3 marineros, en las 3 debe sobrar 1
    for i in range(3):
        reparticion = repartir(catils)
        catils = reparticion[0]
        if reparticion[1] == 1:
            reparticiones.append(reparticion)
        else:
            return []

    # Repartición del tesorero, deben sobrar 2
    reparticion = repartir(catils)
    if reparticion[1] == 2:
        reparticiones.append(reparticion)
    else:
        return []

    return reparticiones


if __name__ == '__main__':
    results = []
    n = 100001
    while len(results) < 10:
        if situacion(n):
            results.append(situacion(n))
        n += 1

    print(results)
