ps = float(input('Digite um segmento: '))
ss = float(input('Digite o segundo segmento: '))
ts = float(input('Digite o terceiro segmento: '))
if ps + ss > ts and ps + ts > ss and ss + ts > ps:
    print('Os segmentos PODEM formar um triângulo.')
    if ps == ss == ts:
        print('O triângulo formado será EQUILÁTERO.')
    elif ps == ss != ts or ps == ts != ss or ss == ts != ps:
        print('O triângulo formado será ISÓSCELES.')
    elif ps != ss != ts:
        print('O triângulo formado será ESCALENO.')
else:
    print('Os segmentos NÃO PODEM formar um triângulo.')