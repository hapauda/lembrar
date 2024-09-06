# filtre ano bixesto divisivel por 4 , por 100 não é igual a zero, ano divisivel por 400 igual a zero
def ano_bixesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    return False

ano = 2028
if ano_bixesto == True:
    print(f"{ano} esse ano é bixesto.")
else:
    print(f"{ano} esse ano não é bixesto.")

# faça uma função que volte uma equação de segundo grau
import math

def equação_segundo_grau(a,b,c):
    delta = b*b - 4*a*c
    if delta < 0:
        raise ValueError("delta impossivel de ocorrer.")
    elif delta == 0: 
        x = -b / (2*a)
        return f"A equação real {x}"
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        return f"A equação real tem dois valores {x1}, {x2}"

a,b,c = 1,-3,2
resultado = equação_segundo_grau(a,b,c)
print(resultado)