valor_investido = float(input('Qual o valor investido em reais ?\n '))

numero_views = (valor_investido * 21.6) * 4 + (valor_investido * 30)
print('O número aproximado de pessoas que visualizarão o anúncio será {:.2f} '.format(numero_views))