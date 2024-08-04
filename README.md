# Grafo Bipartido de Emparelhamento Estável

## Sobre

Este projeto implementa um sistema de gerenciamento de campeonatos de futebol, gerando um campeonato com 38 rodadas, incluindo jogos de ida e volta. Desenvolvido em Python, o projeto é parte do trabalho da disciplina Teoria e Aplicação de Grafos da Universidade de Brasília (UnB), utilizando as bibliotecas NetworkX para manipulação de grafos e Matplotlib para visualização.

O sistema permite a definição de times e a geração de uma tabela de partidas com a restrição de que times da mesma cidade não podem ser mandantes simultaneamente. Os dados podem ser importados de arquivos CSV formatados especificamente.

## Instalação

### Pré-requisitos

Antes de começar, certifique-se de ter o Python e as bibliotecas necessárias instaladas no seu sistema.

#### 1. Instalação do Python

Se o Python não estiver instalado, siga as instruções adequadas para o seu sistema operacional:

- ##### Linux (Debian/Ubuntu):
  ```bash
  sudo apt install python3
  ```

- ##### Arch Linux:
  ```bash
  sudo pacman -S python
  ```

- ##### Fedora:
  ```bash
  sudo dnf install python3
  ```

- ##### Windows:
  Baixe o instalador do Python em python.org e siga as instruções.
  Verifique a instalação do Python no prompt de comando:
  ```bash
  python --version
  ```

- ##### macOs:
  ```bash
  brew install python
  ```
  
#### 2. Instalação das Bibliotecas Python

O projeto requer as seguintes bibliotecas Python:

- **NetworkX:** Biblioteca para criação, manipulação e estudo de estruturas, dinâmicas e funções de redes complexas.
- **Matplotlib:** Biblioteca para criação de gráficos estáticos, animações e interações.

Você pode instalá-las facilmente usando o PIP, o gerenciador de pacotes padrão do Python:

```bash
pip install networkx matplotlib
```

### Configuração do Ambiente

#### 1. Navegar até o Diretório do Projeto

Entre no diretório do projeto:

```bash
cd graph-soccer-scheduler
```

#### 2. Executar o Programa

Execute o programa principal do grafo bipartido:

```bash
python main.py
```

## Estrutura do Projeto

### Database

Este diretório armazena todos os dados utilizados pelo projeto. Ele é subdividido da seguinte maneira:

- **csv/:** Contém o arquivo CSV `teams.csv`.
- **images/:** Armazena a imagem gerada do grafo colorido de restrições.
- **images/rounds:** Contém as imagens dos grafos bipartidos que representam cada rodada do campeonato.

### Models

O diretório models contém definições de classes que representam as principais entidades do sistema. Cada arquivo desempenha um papel crucial na modelagem e manipulação dos dados do projeto:

- `team.py`: Implementa a classe Team, responsável pela manipulação do grafo bipartido que representa as relações entre estudantes e projetos.
- `round.py`: Define a classe Round, representando uma rodada específica dentro do contexto do campeonato.
- `championship.py`: Contém a definição da classe Student, que modela os dados e comportamentos dos estudantes participantes do projeto.

### Utilities

Este diretório contém utilitários e funções auxiliares que são essenciais para diversas operações dentro do projeto:

- `csv_handler.py`: Fornece a função para a manipulação do arquivo **CSV**, facilitando a integração e processamento de dados.
- `path_handler.py`: Contém funções para a manipulação e obtenção de caminhos de diretórios de arquivos, ajudando a gerenciar a estrutura de armazenamento de dados de forma eficiente.

### Arquivos Principais

Além dos diretórios específicos, o projeto inclui os seguintes arquivos principais:

- `README.md`: Este arquivo contém informações detalhadas sobre o projeto.
- `.gitignore`: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git durante o versionamento do código-fonte.
- `main.py`: O script principal do projeto, usado para iniciar e executar o programa principal.


## Pacote Models:

### Classe Team:

A classe `Team` representa um time com seus atributos básicos: sigla, nome e cidade. Ela fornece métodos para acessar e modificar esses atributos, além de um método para exibir as informações do time.

#### Construtor

###### `__init__(self, acronym, name, city)`
Inicializa uma nova instância da classe `Team`.

- **Parâmetros:**
  - `acronym` (str): A sigla do time.
  - `name` (str): O nome do time.
  - `city` (str): A cidade do time.

#### Propriedades

##### `acronym`
Obtém ou define a sigla do time.

- **Getter:** `acronym(self)`
  - Retorna: A sigla do time.
  
- **Setter:** `acronym(self, acronym)`
  - Parâmetros: 
    - `acronym` (str): A nova sigla do time.

##### `name`
Obtém ou define o nome do time.

- **Getter:** `name(self)`
  - Retorna: O nome do time.
  
- **Setter:** `name(self, name)`
  - Parâmetros: 
    - `name` (str): O novo nome do time.

##### `city`
Obtém ou define a cidade do time.

- **Getter:** `city(self)`
  - Retorna: A cidade do time.
  
- **Setter:** `city(self, city)`
  - Parâmetros: 
    - `city` (str): A nova cidade do time.

#### Métodos

##### `information(self)`
Exibe as informações do time.

### Classe Round:

A classe `Round` representa uma rodada em um campeonato, contendo métodos para gerenciar as partidas e gerar uma imagem de gráfico bipartido das equipes.

#### Construtor

##### `__init__(self, id)`
Inicializa uma nova instância da classe `Round`.

- **Parâmetros:**
  - `id` (int): O identificador da rodada.

#### Propriedades

##### `id`
Obtém ou define o identificador da rodada.

- **Getter:** `id(self)`
  - Retorna: O identificador da rodada.
  
- **Setter:** `id(self, id)`
  - Parâmetros: 
    - `id` (int): O novo identificador da rodada.

##### `matches`
Obtém ou define o grafo de partidas.

- **Getter:** `matches(self)`
  - Retorna: O grafo de partidas.
  
- **Setter:** `matches(self, matches)`
  - Parâmetros: 
    - `matches` (nx.Graph): O novo grafo de partidas.

#### Métodos

##### `is_home_team(self, acronym)`
Verifica se uma equipe é mandante.

- **Parâmetros:**
  - `acronym` (str): A sigla da equipe.
  
- **Retorna:** `bool`
  - `True` se a equipe for mandante, caso contrário `False`.

##### `is_away_team(self, acronym)`
Verifica se uma equipe é visitante.

- **Parâmetros:**
  - `acronym` (str): A sigla da equipe.
  
- **Retorna:** `bool`
  - `True` se a equipe for visitante, caso contrário `False`.

##### `is_team_in_round(self, acronym)`
Verifica se uma equipe está participando da rodada.

- **Parâmetros:**
  - `acronym` (str): A sigla da equipe.
  
- **Retorna:** `bool`
  - `True` se a equipe estiver participando da rodada, caso contrário `False`.

##### `is_valid_round(self, number_of_teams)`
Verifica se a rodada é válida.

- **Parâmetros:**
  - `number_of_teams` (int): O número total de equipes.
  
- **Retorna:** `bool`
  - `True` se a rodada for válida, caso contrário `False`.

##### `add_home_team(self, acronym)`
Adiciona uma equipe como mandante.

- **Parâmetros:**
  - `acronym` (str): A sigla da equipe.
  
- **Exceção:** 
  - `ValueError`: Se a equipe já existir como mandante ou visitante.

##### `add_away_team(self, acronym)`
Adiciona uma equipe como visitante.

- **Parâmetros:**
  - `acronym` (str): A sigla da equipe.
  
- **Exceção:** 
  - `ValueError`: Se a equipe já existir como mandante ou visitante.

##### `create_match_pair(self, home_team_acronym, away_team_acronym)`
Cria uma partida entre uma equipe mandante e uma equipe visitante.

- **Parâmetros:**
  - `home_team_acronym` (str): A sigla da equipe mandante.
  - `away_team_acronym` (str): A sigla da equipe visitante.
  
- **Exceção:** 
  - `ValueError`: Se a equipe mandante ou visitante não existir ou não estiver no papel correto.

##### `reset_matches(self)`
Limpa todas as partidas da rodada.

##### `generate_bipartite_graph_image(self, directory)`
Gera e salva uma imagem do gráfico bipartido das partidas.

- **Parâmetros:**
  - `directory` (str): O diretório onde a imagem será salva.
  
- **Saída:** 
  - Uma imagem do gráfico bipartido salva no diretório especificado.


### Classe Championship:

A classe `Championship` representa um campeonato de futebol, gerenciando equipes, restrições de cidade, e gerando a tabela de jogos e visualizações.

#### Construtor

##### `__init__(self, name)`
Inicializa uma nova instância da classe `Championship`.

- **Parâmetros:**
  - `name` (str): O nome do campeonato.

#### Propriedades

##### `restrictions`
Obtém ou define o grafo de restrições.

- **Getter:** `restrictions(self)`
  - Retorna: O grafo de restrições.
  
- **Setter:** `restrictions(self, restrictions)`
  - Parâmetros: 
    - `restrictions` (nx.Graph): O novo grafo de restrições.

##### `teams`
Obtém ou define o dicionário de equipes.

- **Getter:** `teams(self)`
  - Retorna: O dicionário de equipes.
  
- **Setter:** `teams(self, teams)`
  - Parâmetros: 
    - `teams` (dict): O novo dicionário de equipes.

##### `rounds`
Obtém ou define o dicionário de rodadas.

- **Getter:** `rounds(self)`
  - Retorna: O dicionário de rodadas.
  
- **Setter:** `rounds(self, rounds)`
  - Parâmetros: 
    - `rounds` (dict): O novo dicionário de rodadas.

##### `name`
Obtém ou define o nome do campeonato.

- **Getter:** `name(self)`
  - Retorna: O nome do campeonato.
  
- **Setter:** `name(self, name)`
  - Parâmetros: 
    - `name` (str): O novo nome do campeonato.

#### Métodos Públicos

##### `add_team(self, acronym, name, city)`
Adiciona uma equipe ao campeonato.

- **Parâmetros:**
  - `acronym` (str): A sigla da equipe.
  - `name` (str): O nome da equipe.
  - `city` (str): A cidade da equipe.
  
- **Exceção:** 
  - `ValueError`: Se a equipe já existir no campeonato.

##### `create_restrictions(self)`
Cria restrições com base nas equipes da mesma cidade.

##### `generate_round_robin_schedule(self, directory=".")`
Gera a tabela de jogos do campeonato.

- **Parâmetros:**
  - `directory` (str): O diretório onde as imagens dos gráficos bipartidos serão salvas. Padrão é o diretório atual.
  
- **Exceção:** 
  - `ValueError`: Se o número de equipes não for par.

##### `generate_graph_coloring_image(self, directory=".", filename="championship_restrictions_graph.png")`
Gera e salva uma imagem de coloração do grafo de restrições.

- **Parâmetros:**
  - `directory` (str): O diretório onde a imagem será salva. Padrão é o diretório atual.
  - `filename` (str): O nome do arquivo da imagem. Padrão é `"championship_restrictions_graph.png"`.

##### `print_all_rounds(self)`
Imprime todas as rodadas e seus respectivos jogos em ordem crescente.

#### Métodos Privados

##### `__number_of_teams(self)`
Obtém o número total de equipes no campeonato.

- **Retorna:** O número de equipes.

##### `__number_of_rounds(self)`
Obtém o número total de rodadas necessárias.

- **Retorna:** O número de rodadas.

##### `__get_largest_number_of_teams_in_same_city(self)`
Obtém o maior número de equipes na mesma cidade.

- **Retorna:** O maior número de equipes na mesma cidade.

##### `__initialize_rounds(self)`
Inicializa as rodadas do campeonato.

##### `__check_team_restriction(self, home_team_acronym, away_team_acronym)`
Verifica se há uma restrição entre duas equipes.

- **Parâmetros:**
  - `home_team_acronym` (str): A sigla da equipe da casa.
  - `away_team_acronym` (str): A sigla da equipe visitante.
  
- **Retorna:** `True` se há uma restrição, `False` caso contrário.

##### `__can_generate_schedule_with_restrictions(self)`
Para verificar se é possível gerar uma tabela de jogos com as **restrições de cidade**, deve-se validar a seguinte inequação:

**N * M ≤ T**

onde:
- **N** é a quantidade de **cores** no grafo de restrições,
- **M** é a quantidade de rodadas como mandante **mandantes**,
- **T** é o total de **rodadas**.

Para um campeonato de **38 rodadas**, sendo **19** dessas como mandantes, deve-se garantir que, no máximo, existam **2 times** por cidade. Isso assegura que seja possível gerar o campeonato sem que times da mesma cidade atuem como mandantes simultaneamente em uma mesma rodada.

- **Retorna:** `True` se a tabela pode ser gerada com as restrições, `False` caso contrário.


## Pacote Utilities:

### `csv_handler.py`:

#### Descrição

A função `read_csv` lê as linhas de um arquivo CSV, ignorando o cabeçalho e retornando os dados como uma lista de listas. 

#### Parâmetros

- `file_path` (str): O caminho para o arquivo CSV que deve ser lido.

#### Retorno

- `data` (list of lists): Uma lista contendo as linhas do arquivo CSV, onde cada linha é representada como uma lista de strings.

#### Exceções

A função pode lançar as seguintes exceções:

- `FileNotFoundError`: Se o arquivo especificado por `file_path` não for encontrado.
  - Mensagem: "Error: The file '{file_path}' was not found."

- `IOError`: Se houver um erro ao abrir o arquivo.
  - Mensagem: "Error opening the file '{file_path}': {e.strerror}"

- `csv.Error`: Se ocorrer um erro ao ler o arquivo CSV.
  - Mensagem: "Error reading the CSV file '{file_path}': {e}"

- `Exception`: Para qualquer outro erro inesperado que ocorra durante a leitura do arquivo.
  - Mensagem: "Unexpected error while reading the file '{file_path}': {e}"

### `path_handler.py`:

#### Função `ensure_directory_exists`

##### Descrição

Garante que o diretório especificado existe, criando-o se necessário.

##### Parâmetros

- `directory_path` (str): O caminho para o diretório que deve ser verificado e possivelmente criado.

##### Retorno

- `directory_path` (str): O caminho para o diretório garantido ou criado.

##### Exceções

A função pode lançar as seguintes exceções:

- `PermissionError`: Se ocorrer um erro de permissão ao tentar criar o diretório.
  - Mensagem: "Permission error: Unable to create directory '{directory_path}'. Details: {e}"

- `OSError`: Se ocorrer um erro de sistema ao tentar criar o diretório.
  - Mensagem: "OS error: Failed to create directory '{directory_path}'. Details: {e}"

- `Exception`: Para qualquer outro erro inesperado.
  - Mensagem: "Unexpected error: {e}"

#### Função `get_images_directory`

##### Descrição

Obtém o caminho para o diretório de imagens, criando-o se necessário.

##### Retorno

- `images_dir` (str): O caminho para o diretório de imagens.

## `main.py`:

Este script configura um campeonato, gera o cronograma de rodadas e fornece um menu para interagir com o usuário. O código utiliza classes e funções para gerenciar as equipes, criar restrições, gerar imagens e exibir informações do programa.

### Importações

- `read_csv`: Função para ler arquivos CSV.
- `get_csv_directory`, `get_round_images_directory`, `get_images_directory`: Funções para obter diretórios de arquivos.
- `Championship`: Classe para gerenciar o campeonato.

### Funções

#### `setup_championship()`

Configura o campeonato com as equipes, restrições e imagens.

- **Passos:**
  1. Lê os dados das equipes a partir do arquivo `teams.csv`.
  2. Cria uma instância da classe `Championship`.
  3. Adiciona as equipes ao campeonato.
  4. Cria restrições para o campeonato.
  5. Gera uma imagem de coloração gráfica.
  6. Gera o cronograma de rodadas.
  7. Imprime uma mensagem de sucesso e aguarda o usuário pressionar uma tecla.

- **Observação:** Caso deseje mudar os times, basta alterar o nome do arquivo CSV na função `read_csv` para o novo arquivo contendo as informações das equipes.
- **Retorno:** Objeto `Championship`.



#### `print_all_rounds(cp)`

Imprime todas as rodadas do campeonato se o campeonato estiver configurado.

- **Parâmetros:**
  - `cp`: Objeto `Championship`.

#### `print_program_information()`

Imprime informações do programa, incluindo detalhes sobre a universidade, departamento, curso, aluno e número de matrícula.

#### `display_menu()`

Exibe o menu principal com opções para o usuário.

#### `get_user_choice()`

Obtém e valida a escolha do usuário a partir do menu.

- **Retorno:** Opção escolhida pelo usuário (1, 2 ou 3).

#### `main_menu(cp)`

Gerencia as escolhas do usuário a partir do menu principal.

- **Parâmetros:**
  - `cp`: Objeto `Championship`.

### Inicialização

No início do script, o campeonato é configurado e o menu principal é iniciado.

```python
if __name__ == "__main__":
    cp = setup_championship()
    main_menu(cp)
```