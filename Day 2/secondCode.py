import os

def main():
    print("Sciutti's solution to the second problem")
    res = letturaRighe()
    print(f"Numero di righe valide: {res}")

def letturaRighe():
    conteggio = 0
    percorso_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(percorso_file, 'r') as file:
        for linea in file:
            numeri = list(map(int, linea.split()))
            if analisiRiga(numeri):
                conteggio += 1
    return conteggio

def analisiRiga(x):
    if is_safe(x):
        return True
    for i in range(len(x)):
        if is_safe(x[:i] + x[i+1:]):
            return True
    return False

def is_safe(x):
    if all(x[i] < x[i + 1] for i in range(len(x) - 1)) or all(x[i] > x[i + 1] for i in range(len(x) - 1)):
        if all(1 <= abs(x[i] - x[i + 1]) <= 3 for i in range(len(x) - 1)):
            return True
    return False

main()
