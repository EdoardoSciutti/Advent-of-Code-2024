def main():
    print("Sciutti's solution to the first problem")
    listaSinistra = []
    listaDestra = []
    leggiFile(listaSinistra, listaDestra)
    listaSinistra = mergeSort(listaSinistra)
    listaDestra = mergeSort(listaDestra)
    return contoDistanzeSommate(listaSinistra, listaDestra)

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

def contoDistanzeSommate(x, y):
    somma = 0
    for i in range(len(x)):
        somma += abs(x[i] - y[i])
    return somma

main()
