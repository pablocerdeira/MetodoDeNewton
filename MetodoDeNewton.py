# -*- coding: utf-8 -*-
from decimal import *
import pylab
import matplotlib.pyplot as plt
from random import sample, randint
from statlib import stats

print '''
Curso:      Análise Matemática para Aplicações
Professor:  Antônio Carlos Saraiva Branco 
Aluno:      Pablo Cerdeira
Exercício:
Implemente o método de Newton para encontrar a raiz de dado número em uma função
-----------    
'''

# variáveis globais
Ns = sample(xrange(100000),1000)                                                # Lista com 100 Ns aleatorios ate 1000
indice = Decimal(2)                                                             # 2 para raiz quadrada, 3 para cúbica ...
precs = [2,6,10,100,1000]                                                       # Precisões a serem buscadas
totIteracoes = []                                                               # Histórico do contador de iterações

def main():
    i = 0
    for N in Ns: 
        raizes,iteracoes = [],[]
        x0 = randint(1,N-1)
        for prec in precs:                                                      # Loop para cada uma das precisões
            iteracs,raiz = newton(indice,N,prec,x0)                             # chama newton() para o cálculo da raiz
            raizes.append(raiz)
            iteracoes.append(iteracs)
            totIteracoes.append(iteracoes)
        i+=1
        out(N,indice,raizes,precs,x0,iteracoes,i,len(Ns)) 
    final()
        
def newton(indice,a,precisao,x0):
    if a == 1: exit
    resultados = [0,1]
    getcontext().prec = precisao+2

    while resultados[-2] != resultados[-1]:
        resultados.append(Decimal(1/indice*((indice-1)*x0+(a/x0**(indice-1)))))
        x0 = resultados[-1]
    
    # Retorna as iterações e a raiz.
    return len(resultados), x0

def out(N,indice,raizes,precs,x0,iteracoes,i,total):
    print ' '
    print ' '
    print '******************************************************************'
    print 'Teste:     '+str(i)+'/'+str(total)+' - '+str(float(i)/total*100)+'%'
    print 'N:         %d' % N
    print 'Indice:    %d' % indice
    print 'Inicial:   %d' % x0
    i = 0
    for raiz in raizes:                
        print '------------------------------------------------------------------'
        print 'Raiz:      %s' % raiz
        print 'Precisao:  %d -  Iteracoes:  %d' % (precs[i],iteracoes[i])
        i+=1
    print '------------------------------------------------------------------'
    
def final():
    i = 0
    iteracoes = zip(*totIteracoes)
    print ' '
    print ' '
    print '******************************************************************'
    print 'Media e desvio padrao das iteracoes:'
    for prec in precs:
        print '------------------------------------------------------------------'
        print 'Precisao:    %d' % prec
        print 'Media:       %d' % stats.mean(iteracoes[i])
        print 'Maximo:      %d' % max(iteracoes[i])
        print 'Minimo:      %d' % min(iteracoes[i])
        print 'Desvio:      %d' % stats.stdev(iteracoes[i])
        i+=1
    print '------------------------------------------------------------------'

    ticks = range(1,i+1)
    pylab.boxplot(iteracoes)
    pylab.title('Distribuicao das Iteracoes')
    pylab.xlabel('Precisao da raiz em casas decimais')
    pylab.ylabel('Quantidade de Iteracoes')
    pylab.xticks(ticks,precs)
    pylab.show()
    
if __name__ == "__main__":
    main()