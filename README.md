# Funcoes_Plot_Funcao_Randint
Assessment activity of the 1º period of IT Bachelor on Functions in Python / Atividade avaliativa do 1º periodo do Bacharelado em TI sobre Funções em Python

## Plot Função Randint

### Goal / Objetivo

In the question of analysis of the randint function, we analyzed how random the choices of the randint function are for a given range of values, and the greater the number of choices, the better this distribution of the chosen numbers.
We also saw in the plot mustache issue, the use of the matplotlib library to plot a graph for a set of X and Y values.
In this question, we will plot the percentage of variation of the choices of the randint function in relation to the ideal average number of choices for each element given the total number of choices. For example, if we have 10 elements (0 to 9, for example), and we make 100 choices, the ideal average of choices per element to be fully balanced is 100 / 10 = 10. If a certain element was chosen 14 times, then the percentage of variation of this element is: (14 - 10) / 10 = 0.4 = 40%. If another element was chosen only 7 times, its percentage of variation is: (7 - 10) / 10 = -0.3 = -30%.

Na questão análise da função randint, analisamos o quão aleatória são as escolhas da função randint para um determinado intervalo de valores, e quanto maior era o número de escolhas, melhor era essa distribuição dos números escolhidos.
Vimos também na questão plot mustache, o uso da biblioteca matplotlib para plotar um gráfico para um conjunto de valores X e Y.
Nesta questão, iremos plotar o percentual de variação das escolhas da função randint em relação à quantidade média ideal de escolhas de cada elemento dado o total de escolhas. Por exemplo, se temos 10 elementos (0 a 9, por exemplo), e fazemos 100 escolhas, a média ideal de escolhas por elemento para ficar totalmente balanceado é 100 / 10 = 10. Se um determinado elemento foi escolhido 14 vezes, então o percentual de variação deste elemento é: (14 - 10) / 10 = 0.4 = 40%. Já se um outro elemento foi escolhido apenas 7 vezes, o seu percentual de variação é: (7 - 10) / 10 = -0.3 = -30%.

1. Example / Exemplo
```py

Inteiro inicial do intervalo? 0
Inteiro final do intervalo? 9
Quantidade de escolhas? 100000
Contagem de escolhas:
0 - 9985
1 - 10060
2 - 9987
3 - 10022
4 - 10067
5 - 9942
6 - 9899
7 - 9969
8 - 9958
9 - 10111
```
