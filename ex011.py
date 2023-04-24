alt = float(input('Informe a altura da parede: '))
larg = float(input('Informe a largura da parede: '))
area = alt * larg
tinta = area / 2
print('A sua parede tem a dimensão de {}m X {}m e a área total é de {}m2'.format(alt, larg, area))
print('Para pintar essa parede, você vai precisar de {}l de tinta'.format(tinta))
