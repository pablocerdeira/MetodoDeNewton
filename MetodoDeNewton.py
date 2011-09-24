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
Implemente o metodo de Newton para encontrar a raiz de dado numero em uma funcao
-----------    
'''

# variáveis globais
Ns = sample(xrange(1000),100)                                                   # Lista com 100 Ns aleatorios ate 1000
indice = Decimal(2)
precs = [2,6,10,100]
totIteracoes = []

def main():
    for N in Ns: 
        raizes,iteracoes,x0s = [],[],[]
        for prec in precs: 
            x0,iteracs,raiz = newton(indice,N,prec)
            raizes.append(raiz)
            iteracoes.append(iteracs)
            x0s.append(x0)
            totIteracoes.append(iteracoes)
        out(N,indice,raizes,precs,x0s,iteracoes) 
    final()
        
def newton(indice,a,precisao):
    if a == 1: exit
    x0 = randint(1,a-1)
    xOriginal = x0
    resultados = [0,1]
    getcontext().prec = precisao+2

    while resultados[-2] != resultados[-1]:
        resultados.append(Decimal(1/indice*((indice-1)*x0+(a/x0**(indice-1)))))
        x0 = resultados[-1]
    
    # Retorna o rand, as iteracoes e a raiz.
    return xOriginal, len(resultados), x0

def out(N,indice,raizes,precs,x0s,iteracoes):
    print ' '
    print ' '
    print '******************************************************************'
    print 'N:         %d' % N
    print 'Indice:    %d' % indice
    i = 0
    for raiz in raizes:                
        print '------------------------------------------------------------------'
        print 'Raiz:      %s' % raiz
        print 'Precisao:  %d  -  Inicial:  %d  -  Iteracoes:  %d' % (precs[i],x0s[i],iteracoes[i])
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
    pylab.xlabel('Grupo de Iteracoes')
    pylab.ylabel('Quantidade de Iteracoes')
    pylab.xticks(ticks,precs)
    pylab.show()
    
if __name__ == "__main__":
    main()