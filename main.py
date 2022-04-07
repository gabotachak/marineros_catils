def repartir(catils):
    # Retorna la división, el residuo y lo que queda
    return [int(catils / 3), catils % 3, catils - int(catils / 3) - 1]


def situacion(catils):
    registro = []
    # Repartición de los 3 marineros y el almojarife, siempre debe sobrar 1
    sobras_esperadas = [1] * 4
    for sobra_esperada in sobras_esperadas:
        reparto, sobrante, restante = repartir(catils)
        if sobrante == sobra_esperada:
            registro.append([catils, 3, reparto, sobrante, restante])
        else:
            # En caso de que no sobre lo esperado, se retorna un array vacío simbolizando que el registro no es válido,
            # ya que no es como en la situación inicial y no van a ser anexados al resultado.
            return []
        catils = restante

    # No le queda nada al almojarife
    registro[-1][-1] = 0
    return registro


if __name__ == '__main__':
    resultados = {}
    n = 100001
    while len(resultados) < 10:
        intento = situacion(n)
        if intento:
            resultados[n] = intento
        n += 1

    for n, resultado in resultados.items():
        r = []
        print(f"Monedas totales: {n}")
        padding = "{:<20} {:<17} {:<10} {:<10} {:<20}"
        print(padding.format("Monedas en la caja:", "Divididas entre:", "Da:", "Residuo:", "Monedas restantes:"))

        for monedas, divisor, da, residuo, restantes in resultado:
            r.append(da)
            print(padding.format(monedas, divisor, da, residuo, restantes))
        print()

        print(f"Marinero # 1 {r[0]}+{r[3]} = {r[0] + r[3]}")
        print(f"Marinero # 2 {r[1]}+{r[3]} = {r[1] + r[3]}")
        print(f"Marinero # 3 {r[2]}+{r[3]} = {r[2] + r[3]}")
        print(f"Almojarife = 1")
        print(f"Tiradas al mar = 3")
        print(f"Total = {n}")
        print()
