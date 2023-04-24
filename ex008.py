#km hm dam m dm cm mm

medida = float(input('Digite uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('A medida de {} metros é igual a {} decímetros'.format(medida, dm))
print('A medida de {} metros é igual a {} centímetros'.format(medida, cm))
print('A medida de {} metros é igual a {} milímetros'.format(medida, mm))
print('A medida de {} metros é igual a {} decâmetros'.format(medida, dam))
print('A medida de {} metros é igual a {} hectômetros'.format(medida, hm))
print('A medida de {} metros é igual a {} quilômetros'.format(medida, km))