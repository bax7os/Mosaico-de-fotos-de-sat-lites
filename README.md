# Mosaico de Fotos de Satélites

### 1 Introdução

O Instituto Campograndense de Pesquisas Espaciais (ICPE) lançou o satélite TERES (“Tereré”)
para fazer um levantamento de informações geográficas do Estado de Mato Grosso do Sul. O
objetivo é fotografar e mapear as áreas de preservação ambiental localizadas em nosso estado.
A novidade é que você foi um dos selecionados para fazer parte de uma equipe de cientistas da
computação que vai trabalhar no desenvolvimento de um software que fará a identificação e o
mapeamento de cada uma das áreas fotografadas pelo satélite.
O problema é que as fotos obtidas com as câmeras digitais presas ao satélite TERES possuem
um ângulo de cobertura bastante reduzido. Nos casos em que é necessário fotografar uma área
maior, são necessárias diversas fotos para mapeá-la. Para estas situações, o seu programa deve
estar preparado para fazer a junção de várias imagens para compor uma foto única de uma área
mais abrangente. Esse processo de junção de imagens consecutivas dá-se o nome de montagem
do mosaico (mosaiking).

### 2 Tarefa
A sua tarefa é desenvolver uma aplicação que permita a manipulação das imagens obtidas
pelo satélite TERES. Assuma que todas as áreas fotografadas correspondem a retângulos que
são identificados pelas coordenadas (xse, yse) e (xid, yid), correspondendo, respectivamente, às
coordenadas das extremidades superior esquerda (se) e inferior direita (id) de cada fotografia
tirada pelo satélite TERES. As laterais de cada área são sempre paralelas aos eixos x e y.
Caso haja sobreposição de fotos, as áreas devem ser identificadas pelas coordenadas do menor
retângulo que as contenha. Considere que a sobreposição ocorre sempre que existe, pelo menos,
um ponto em comum entre as áreas fotografadas. A sua aplicação deve permitir, a qualquer
instante, a visualização das áreas identificadas. Observe que podem existir algumas áreas que
não se sobreponham. Nestes casos, deve existir um retângulo mínimo envolvendo as
duas áreas identificadas.
A saída do seu programa deve listar a quantidade e as coordenadas dos retângulos mínimos
que delimitam cada uma das áreas fotografadas pelo satélite TERES e “mosaicadas”pela sua
aplicação

## 🚀 Começando

Para que o código sera executado corretamente siga os passos abaixo.

### 🔧 Instalação

1 - Faça o download da biblioteca matplotlib.

2 -  Instale a biblioteca no Prompt de Comando com o comando "pip install matplotlib"

3 - Em seguida, ponha suas coordenadas em um arquivo .txt com o nome teste (teste.txt) 
na mesma pasta do arquivo python.

4 - Em seguida, volte ao Prompt de Comando e acesse a página que estão os arquivos com o 
comando "cd "O diretorio da pasta"".

5 - Execute o programa com o comando "python "Nome do programa".py"
