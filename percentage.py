def number(n, p):
    a = int(input("1 : Augmentation, 2 : Diminution "))

    if a == 1:
        prix = n * (1 + p/100)
        print(f"Vous avez subi une augmentation de {p}%, le prix à présent est de {n - prix}")
    else:
        prix = n * (1 - p/100)
        print(f"Vous avez subi une diminution de {p}%, le prix à présent est de {n - prix}")

number(140, 85)