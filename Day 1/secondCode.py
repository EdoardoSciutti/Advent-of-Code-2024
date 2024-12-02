def main():
    print("Sciutti's solution to the second problem")
    listaSinistra = []
    listaDestra = []
    leggiFile(listaSinistra, listaDestra)
    listaSinistra = mergeSort(listaSinistra)
    listaDestra = mergeSort(listaDestra)
    print("Punteggio di similarità:", calcolaSimilarita(listaSinistra, listaDestra))

def leggiFile(x, y):
    with open("input.txt", "r") as file:
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

def calcolaSimilarita(listaSinistra, listaDestra):
    conteggioDestra = {}
    for num in listaDestra:
        if num in conteggioDestra:
            conteggioDestra[num] += 1
        else:
            conteggioDestra[num] = 1

    punteggio = 0
    for num in listaSinistra:
        if num in conteggioDestra:
            punteggio += num * conteggioDestra[num]

    return punteggio

main()
