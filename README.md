# Repositório de Estudos em Python

Uso este repositório como forma de documentar meu progresso na linguagem Python.

Cada "pasta" (pacote) é um tema estudado e praticado. Nelas, existem arquivos `.py` (módulos) com soluções de exercícios.

Até o dia **15/04/2026**, estes módulos não eram perfeitamente estruturados. Eu deixava-os separados por "nível de dificuldade" de exercícios.

A partir de **16/04/2026**, eles começaram a ser separados corretamente, onde cada módulo é uma solução de exercício, um script apenas.

---

## Estrutura e Temas

Abaixo seguem os temas e exercícios relacionados, descritos com mais detalhes.

### *args_kwargs*
*(pasta pré reformulação do repositório)*

- Contém exercícios deste tema separados apenas pelo nível de dificuldade. *(foi o início da jornada)*

---

### decorators

#### Nível Fácil (01 ao 05)
Decorators de 2 níveis (sem argumentos).  
Foco: entender o wrapper e a execução de funções.

#### Nível Intermediário (06 ao 10)
Decorators de 3 níveis (com argumentos).  
Foco: entender a "fábrica" de decorators e o fechamento de escopo (closures).

#### Nível Avançado (11 ao 15)
Casos complexos e arquitetura.  
Foco: decorators em classes, preservação de metadados e lógica de negócio.

---

## Lista de Exercícios

### Exercício 01
O Mensageiro:  
Crie um decorator que apenas imprima "Iniciando função..." antes da função decorada rodar e "Função finalizada!" depois.

### Exercício 02
Conversor de Maiúsculas:  
Crie um decorator que pegue o retorno de uma função (supondo que ela retorne uma string) e o transforme todo em letras maiúsculas.

### Exercício 03
Dobrador de Valor:  
Crie um decorator que multiplique por 2 o resultado numérico de qualquer função decorada.

### Exercício 04
Verificador de Tipo:  
Crie um decorator que verifique se os argumentos passados para a função são todos do tipo int. Se não forem, imprima um aviso.

### Exercício 05
Contador de Chamadas:  
Crie um decorator que conte quantas vezes uma função foi executada durante a execução do programa e imprima esse valor a cada chamada.

### Exercício 06
Multiplicador Genérico:  
Crie um decorator `@multiplicar(n)` que multiplique o resultado da função por um valor n definido no decorator.

### Exercício 07
Prefixo Personalizado:  
Crie um decorator `@prefixo(texto)` que adicione uma string personalizada antes do retorno de uma função que retorna texto.

### Exercício 08
Validador de Intervalo:  
Crie um decorator `@entre(min, max)` que verifique se o resultado de uma função está dentro do intervalo permitido.  
Se não estiver, retorne um erro ou um valor padrão.

### Exercício 09
Atraso na Execução:  
Crie um decorator `@delay(segundos)` que faça o programa "dormir" (`time.sleep`) pelo tempo especificado antes de executar a função.

### Exercício 10
Tentativas de Execução:  
Crie um decorator `@retry(n)` que, se a função decorada der um erro (exceção), tente executá-la novamente até n vezes antes de desistir.

### Exercício 11
O Cache de Resultados (Memoização):  
Crie um decorator `@cache` que armazene o resultado de uma função para determinados argumentos.  
Se a função for chamada com os mesmos argumentos de novo, retorne o valor salvo sem processar a função original.

### Exercício 12
Preservação de Identidade:  
Pesquise sobre `functools.wraps` e aplique-o em um decorator para garantir que, ao dar um `print(minha_funcao.__name__)`, o Python mostre o nome original da função e não o nome "wrapper".

### Exercício 13
Autenticação por Perfil:  
Crie um decorator `@requer_perfil("admin")` que receba um objeto usuario como primeiro argumento da função e só a execute se o `usuario.perfil` for igual ao exigido.

### Exercício 14
Limitador de Taxa (Rate Limiting):  
Crie um decorator `@limite(max_chamadas=5)` que impeça uma função de ser executada mais do que X vezes em um curto período de tempo.

### Exercício 15
Decorator de Classe:  
Crie um decorator que não seja uma função, mas sim uma classe (usando o método `__call__`), que registre o horário exato de cada chamada da função decorada em um arquivo `.txt`.

---

### tratamento de erros (try/except)
Nesta seção, explorei a resiliência de código em Python, implementando mecanismos para capturar e tratar exceções de forma que o fluxo do programa não seja interrompido abruptamente por falhas previstas.

#### Nível Fácil (01 ao 05)
Foco nos fundamentos da sintaxe try/except e no mapeamento das exceções mais comuns do Python (Built-in Exceptions). Os exercícios abordam a captura de erros de tipos (ValueError), divisões impossíveis (ZeroDivisionError), chaves inexistentes em dicionários (KeyError) e índices inválidos em sequências (IndexError), além da manipulação básica de arquivos.

#### Nível Intermediário (06 ao 10)
Exploração do controle de fluxo avançado utilizando as cláusulas else (executada em caso de sucesso) e finally (executada obrigatoriamente). Aborda a propagação manual de exceções com o comando raise, a captura de erros de importação de módulos e a hierarquia de exceções, diferenciando tratamentos específicos de capturas genéricas.

#### Nível Avançado (11 ao 15)
Aplicação de tratamento de erros em cenários simulados de sistemas reais. O foco está na criação e captura de exceções personalizadas (Custom Exceptions), automação de validações complexas com loops de repetição, simulação de falhas de conectividade (APIs), gestão de permissões de sistema e o tratamento de interrupções de hardware/usuário (KeyboardInterrupt).

---

## Lista de exercícios (tratamento de erros)

### Exercício 1
Divisão Segura: 
Crie um programa que peça dois números e realize a divisão. Trate o erro de divisão por zero (ZeroDivisionError) e entrada de dados inválida (ValueError).

### Exercício 2
Conversão de Tipos: 
Peça para o usuário digitar uma lista de números separados por vírgula. Tente converter cada elemento para int. Se houver algo que não seja número, informe qual elemento falhou e pule para o próximo.

### Exercício 3
Acesso a Dicionário: 
Crie um dicionário com 5 produtos e preços. Peça ao usuário o nome de um produto e exiba o preço. Trate o erro caso o produto não exista no dicionário (KeyError).

### Exercício 4
Índice de Lista: 
Dada a lista frutas = ["Maçã", "Banana", "Uva"], peça um número ao usuário e exiba a fruta naquela posição. Trate o erro de índice fora do alcance (IndexError).

### Exercício 5
Leitura de Arquivo Simples: 
Tente abrir um arquivo chamado dados.txt para leitura. Se o arquivo não existir, exiba uma mensagem amigável em vez do erro do sistema (FileNotFoundError).

### Exercício 6
Calculadora de Média com finally: 
Crie uma função que calcula a média de uma lista. Independentemente de a lista estar vazia ou conter erros, use o bloco finally para imprimir "Processamento finalizado".

### Exercício 7
Soma de Inteiros com else: 
Peça dois números. Se a conversão para inteiro e a soma funcionarem perfeitamente, use o bloco else para exibir o resultado. Se falhar, use o except.

### Exercício 8
Validação de Idade: 
Peça a idade do usuário. Se a idade for menor que 0 ou maior que 150, use o comando raise ValueError("Idade impossível") e capture esse erro no bloco except para exibir a mensagem customizada.

### Exercício 9
Busca de Módulo: 
Tente importar uma biblioteca que não existe (ex: import biblioteca_fantasma). Capture o ImportError e sugira ao usuário verificar se o pacote está instalado.

### Exercício 10
Tratamento Genérico vs. Específico: 
Crie um código que possa gerar múltiplos erros (ex: erro de matemática e erro de variável não definida). Escreva blocos except específicos para cada um e um except Exception as e ao final para capturar qualquer outro erro inesperado, exibindo a mensagem do erro original.

### Exercício 11
Simulador de Saque Bancário: 
Crie uma função sacar(valor). Se o valor for maior que o saldo (invente um saldo inicial), dispare uma exceção personalizada chamada SaldoInsuficienteError. Capture-a fora da função.

### Exercício 12
Consumo de API Hipotética: 
Simule uma requisição web. Crie uma lista de dicionários que representam "status codes" (200, 404, 500). Se o status for diferente de 200, dispare e trate exceções simulando falha de conexão ou servidor fora do ar.

### Exercício 13
Escrita em Arquivo Protegido: 
Tente escrever em um arquivo que está configurado como "somente leitura" (ou simule isso tentando escrever em uma pasta do sistema sem permissão). Trate o PermissionError.

### Exercício 14
Iterador Infinito Interrompido: 
Crie um loop while True que pede números e os soma. O loop só deve parar se o usuário pressionar Ctrl+C. Capture o KeyboardInterrupt para exibir a soma total antes de fechar o programa.

### Exercício 15
Validador de Senha Complexo: 
Crie uma função que valida uma senha (mínimo 8 caracteres, uma letra e um número). Dispare exceções diferentes para cada regra violada e use um loop para forçar o usuário a digitar uma senha válida, tratando todos os erros até que a condição de sucesso seja atingida.

