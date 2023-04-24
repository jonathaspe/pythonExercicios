preco = float(input('Digite o valor atual do produto: R$ '))
novo = preco - (preco * 20 / 100)
print('O produto que custava R$ {:.2f} na promoção com 20% de desconto passou a custar R$ {:.2f}!!!'.format(preco, novo))