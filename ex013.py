salario = float(input('Qual é o salário do funcionário? R$ '))
novo = salario + (salario * 20 / 100)
print('O salário do funcionário que era de R$ {:.2f} com o aumento de 20%, passou a ser R$ {:.2f}!!!'.format(salario, novo))