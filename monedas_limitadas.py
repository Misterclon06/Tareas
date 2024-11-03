'''
¿Qué sucede si la cantidad de monedas para el cambio es limitada?
Ejem: Se tiene almacenado para el cambio la siguiente cantidad;
1 de 500w, 1 de 100w, 3 de 50w y 2 de 10w.
- ¿Cómo se debe distribuir 710 para el cambio?
'''

def cambio_moneda2(monedas, cant):
    vuelto = []
    n = 0
    try:
        while cant > 0:
            if (monedas[n][0] <= cant) and (monedas[n][1] > 0):
                cant -= monedas[n][0]
                monedas[n][1] -= 1
                vuelto.append(monedas[n][0])
            else:
                n += 1

        return vuelto
    except IndexError:
        print("no fue suficiente para cubrir el vuelto")
        return [0]
            

def cargar_monedas():
    monedas = list(map(lambda x: [int(x)], input("Ingrese las monedas almacenadas (ej: 500, 100, 50): ").split(",")))
    monedas.sort(reverse = True)
    
    for i in monedas:
        i.append(int(input(f"cuantas monedas de {i} tiene:"))) 
    
    return monedas


monedas= cargar_monedas()


cant = int(input("Introduzca monto: "))  # 710
cambios = cambio_moneda2(monedas, cant)  ### Desarrollar función
print(cambios, len(cambios))
