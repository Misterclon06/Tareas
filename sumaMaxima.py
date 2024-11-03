### Q3. Dados n enteros en una matriz unidimensional sucesiva,
###     escriba un algoritmo que encuentre
###     cuándo se maximiza la suma de los valores sucesivos de la matriz.

# si utilizamos el algoritmo de kadane:

def maximum_subarray(S):
    Max_total = S[0]
    Max_actual = S[0]

    for i in range(1, len(S)):
        Max_actual = max(S[i], Max_actual + S[i]) 
        if Max_actual > Max_total:
            Max_total = Max_actual
    
    return Max_total



S = [-2, 1, -2, 4, -1, 2, 1, -5, 4]
M = maximum_subarray(S)
print(M)
