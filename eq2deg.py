import cmath, math

def eq2deg(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Le discriminant est positif : ∆ = {delta}\nLes solutions de l'équation sont donc "
              f"réelles : \nx1 = {x1} et x2 = {x2}")
    elif delta == 0:
        x0 = -b / (2 * a)
        print(f"Le discriminant est nul : ∆ = {delta}.\nLa solution de l'équation est donc réelle : \nx0 = {x0}")
    else:
        z1 = (-b + cmath.sqrt(delta)) / (2 * a)
        z2 = (-b - cmath.sqrt(delta)) / (2 * a)
        print(f"Le discirmant est négatif : ∆ = {delta}\nLes solutions de l'équation sont donc "
              f"complexes : \nz1 = {z1} et z2 = {z2}")

eq2deg(-1, 1, 1)
