km = float(input('Digite a quantidade de quilômetros percorridos: '))
dias = float(input('Digite a quantidade de dias alugados: '))
cdias = dias * 60
ckm = km * 0.15

total = cdias + ckm

print('O total a ser pago por {}Km rodados e {:.0f} dias alugados é de R$ {:.2f}.'.format(km, dias, total))

