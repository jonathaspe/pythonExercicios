import math

co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)

hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))