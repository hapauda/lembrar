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
"""""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M  is  3  times N .) 
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""
def main_math(n, m):
    for x in range(1, n, 2):
        print((".|."* x).center(m, '-'))
    print("WELCOME".center(m, '-'))
    for x in range(n-2, 0, -2):
        print((".|."*x).center(m, '-'))
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    main_math(N, M)
'''''''''
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
'''
def number_printer(number):
    oar = len(bin(number)) - 2
    for i in range(1, number + 1): 
        # range deve ser o primeiro numero que começa e seu numero final mais 1 ou se for 15 deve usar 16 para mostrar
        dc =  str(i).rjust(oar)
        oc = oct(i)[2:].rjust(oar)
        hexa = hex(i)[2:].rjust(oar)
        bina =  bin(i)[2:].rjust(oar)
        # str numero normal
        # oct para numerosos octal
        # hex para numeros hexadecimais 
        # bin para numeros binarios 0001
        # rjust deve ser usado para centralizar em um loop de caracteres
        print (dc,oc, hexa, bina)
if __name__ == '__main__':
    n = int(12)
    number_printer(n)

# You are given an integer,N . Your task is to print an alphabet rangoli of size N . (Rangoli is a form of Indian folk art based on creation of patterns.) 

# Different sizes of alphabet rangoli are shown below: in python

