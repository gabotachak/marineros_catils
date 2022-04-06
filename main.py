def repartir(catils):
    return [int(catils / 3), catils % 3]


def situacion(catils):
    # Situación inicial, en donde quedan las monedas iniciales y no sobra ninguna
    reparticiones = [[catils, 0]]

    # Repartición de los 3 marineros y el contador, en las 3 primeras veces debe sobrar 1 y en la del contador 2
    sobras_esperadas = [1, 1, 1, 2]
    for sobra_esperada in sobras_esperadas:
        restante, sobrante = repartir(catils)
        catils = restante
        if sobrante == sobra_esperada:
            reparticiones.append([restante, sobrante])
        else:
            # En caso de que no sobre lo esperado, se retorna un array vacío simbolizando que los catils no son como la
            # situación inicial.
            return []
    return reparticiones


if __name__ == '__main__':
    resultados = []
    n = 100001
    while len(resultados) < 10:
        intento = situacion(n)
        if intento:
            resultados.append(intento)
        n += 1

    for resultado in resultados:
        print(resultado)
