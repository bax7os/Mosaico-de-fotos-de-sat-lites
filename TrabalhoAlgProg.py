# Aluna: Ana Clara Bastos Moraes    


# Importando a biblioteca responsável por fazer gráficos com os pontos
import matplotlib.pyplot as plt

# Listas e variáveis a serem usadas
x1 = []
x2 = []
y1 = []
y2 = []
cont = 0
a = 1

# Lendo o arquivo e designando valores para os vetores x1,x2,y1 e y2.


# Abrindo o arquivo
arquivo = open("teste.txt", "r")
# Nesta etapa iremos ler linha por linha do arquivo e seta-los na variável v1.
# O .split() irá remover os espaços entre os ítens do arquivo.
for j in arquivo:
    v1 = j.split()

    # Abaixo designamos os valores de x1,x2,y1 e y2 a partir de sua posição no vetor v1.
    # Assim, se v1 for [3,4,5,6], x1 = 3, x2 = 5, y1 = 4 e y2 = 6.
    for i in range(len(v1)):
        if i == 0:
            x1.append(v1[i])
        if i == 2:
            x2.append(v1[i])
        if i == 1:
            y1.append(v1[i])
        if i == 3:
            y2.append(v1[i])

# Para melhor manipulação dos dados, criei as x_1, x_2, y_1 e y_2 para receber as primeiras posições
# de cada vetor.
x_1, x_2, y_1, y_2 = x1[0], x2[0], y1[0], y2[0]

# Seta o tamanho do vetor x1 na variável cont.
cont = len(x1)

# Analisando os dados:


# Neste "for" comparei os valores iniciais do retangulo com novas posições, sempre dois em dois.
# Toda vez que há ou não há sobreposição um novo par de pontos é feito, então, se altera os valores de
# x_1, x_2, y_1 e y_2 para comparar com as outras posições de x1,x2,y1 e y2.
for l in range(cont):

    # O try é usado nesse código para ter a certeza de que o código não vai parar de executar.
    try:

        # Transformando os vetores em inteiros
        x1 = list(map(int, x1))
        x2 = list(map(int, x2))
        y1 = list(map(int, y1))
        y2 = list(map(int, y2))
        x_1 = int(x_1)
        x_2 = int(x_2)
        y_1 = int(y_1)
        y_2 = int(y_2)

        # Novas variáveis criadas para receber o valor de x1,x2,y1 e y2 na posição l da lista.
        X1, X2, Y1, Y2 = x1[l], x2[l], y1[l], y2[l]

        # Áreas que não se sobrepõem

        # Aqui é feito a verificação se as formas se sobrepõem, se não se sobreporem o código
        # entra nessa sequência de 4 if's, que possuem as mesmas condições do primeiro if só que
        # separadas, porque cada caso muda de uma forma diferente a posição do novo retângulo.

        if x_1 > X2 or x_2 < X1 or y_2 > Y1 or y_1 < Y2:
            if x_1 > X2:
                x_1 = X1
            if x_2 < X1:
                x_2 = X2
            if y_2 > Y1:
                y_2 = Y2
            if y_1 < Y2:
                y_1 = Y1


        # Áreas que se sobrepõem

        # Se a condição do if não for atendida o código entra aqui.
        # É uma sequência de 4 if's que possuem condições que são responsáveis para saber quais vão ser
        # os novos pontos do retângulo.
        else:
            if x_1 > X1:
                x_1 = X1
            if x_2 < X2:
                x_2 = X2
            if y_2 > Y2:
                y_2 = Y2
            if y_1 < Y1:
                y_1 = Y1
    # Exceção para certificar de que o códico não vai parar por erro de estar em uma posição de l que não é encontrada
    # nos vetores.
    except IndexError:
        # Se a exceção acontecer, o código só continua.
        continue

# Mostrando os valores
print("A quantidade de retângulos finais é %i" % a)
print("Seus pontos de são (%i,%i) e (%i,%i)" % (x_1, y_1, x_2, y_2))

# Abaixo, temos as linhas responsáveis pela parte gráfica do código
# Esse resigna o nome do gráfico
plt.title("Pontos do retângulo final")

# Adiciona as grades no gráfico
plt.grid(True)

# Fazem os pontos finais no gráfico
plt.scatter(x_1, y_1)
plt.scatter(x_2, y_2)

# Mostra o gráfico
plt.show()
