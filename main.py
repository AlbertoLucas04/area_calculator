from math import pi
from math import ceil # Arrendada para o número inteiro mais próximo para cima
from math import floor # Arredonda para o número inteiro mais próximo para baixo

def area_quadrado_retangulo (b, h):
    a_q = b * h
    return a_q

def area_triangulo (b, h):
    a_t = (b * h) / 2
    return a_t

def area_circulo(r):
    a_c = pi * r**2
    return a_c

print('\n======CALCULADORA DE ÁREA======\n')

options = int(input('\n[1] = Quadrado ou Retângulo \n[2] = Triângulo \n[3] = Círculo \n\nSelecione sua forma geométrica: '))

match options:

    case 1:
        base_q = float(input('Insira o valor da Base: '))
        altura_q = float(input('Insira o valor da Altura: '))
        result_q = area_quadrado_retangulo(base_q, altura_q)
        print(f'\nA(Quadrado) = B x H\nA = {base_q} x {altura_q}\nA = {result_q} u.')
    case 2:
        base_t = float(input('Insira o valor da Base: '))
        altura_t = float(input('Insira o valor da Altura: '))
        result_t = area_triangulo(base_t, altura_t)
        print(f'\nA(Triângulo) = (B x H) / 2 \nA = ({base_t} x {altura_t}) / 2\nA = {result_t} u.')
    case 3:
        raio_c = float(input('Insira o Raio: '))
        result_c = area_circulo(raio_c)
        print(f'\nA(Círculo) = π x Rˆ2 \nA = π x {raio_c}ˆ2 \nA ~= {ceil(result_c)} u.')
        



