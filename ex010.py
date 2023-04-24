real = float(input('Digite o valor em reais: R$ '))
dolar = real / 5.05
euro = real / 5.55
print('Comprando R$ {:.2f}, você receberá U$ {:.2f}'.format(real, dolar))
print('Comprando R$ {:.2f}, você receberá € {:.2f}'.format(real, euro))