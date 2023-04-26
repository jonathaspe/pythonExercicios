from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo desejado: '))
seno = sin(radians(angulo))
print('O ângulo {} tem o SENO igual a {:.2f}'.format(angulo, seno))

cose = cos(radians(angulo))
print('O ângulo {} tem o COSSENO igual a {:.2f}'.format(angulo, cose))

tan = tan(radians(angulo))
print('O ângulo {} tem a TANGENTE igual a {:.2f}'.format(angulo, tan))