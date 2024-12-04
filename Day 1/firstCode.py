import os

def main():
    print("Sciutti's solution to the first problem:")
    listaSinistra = []
    listaDestra = []
    leggiFile(listaSinistra, listaDestra)
    listaSinistra = mergeSort(listaSinistra)
    listaDestra = mergeSort(listaDestra)
    risultato = contoDistanzeSommate(listaSinistra, listaDestra)
    print(f"Somma delle Distanze: {risultato}")

def leggiFile(x, y):
    percorso_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(percorso_file, 'r') as file:
        for linea in file:
            numeri = linea.split()
            if len(numeri) == 2:
                x.append(int(numeri[0]))
                y.append(int(numeri[1]))
    return x, y

def mergeSort(x):
    if len(x) <= 1:
        return x
    mid = len(x) // 2
    left = mergeSort(x[:mid])
    right = mergeSort(x[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def contoDistanzeSommate(x, y):
    somma = 0
    for i in range(len(x)):
        somma += abs(x[i] - y[i])
    return somma

main()
