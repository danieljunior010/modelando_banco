# Sistema Bancário POO

Este projeto implementa um sistema bancário utilizando o paradigma de **Programação Orientada a Objetos (POO)** em Python. Ele oferece funcionalidades básicas de gestão de contas correntes, incluindo saques, depósitos, e o registro do histórico de transações para cada cliente.

## Funcionalidades

1. **Cadastro de Clientes**:
   - Permite cadastrar um cliente com **CPF**, **nome**, **data de nascimento** e **endereço**.
   - Cada cliente pode ter uma ou mais contas correntes.

2. **Criação de Contas Correntes**:
   - Permite criar uma conta corrente para um cliente. A conta é identificada por um número sequencial e a agência é fixa.
   - Cada conta tem um **saldo**, **limite de saques**, e mantém um histórico de todas as transações realizadas.

3. **Operações Bancárias**:
   - **Depósitos**: Permite adicionar um valor ao saldo de uma conta.
   - **Saques**: Permite retirar um valor do saldo de uma conta, respeitando o limite e o número máximo de saques diários.
   
4. **Histórico de Transações**:
   - Cada conta mantém um histórico das operações realizadas, como saques e depósitos.

## Classes Principais

### 1. `Cliente`
- Representa um cliente do banco.
- Atributos:
  - `endereco`: Endereço do cliente.
  - `contas`: Lista de contas do cliente.
- Métodos:
  - `realizar_transacao(conta, transacao)`: Realiza uma transação (depósito ou saque).
  - `adicionar_conta(conta)`: Adiciona uma nova conta ao cliente.

### 2. `PessoaFisica`
- Subclasse de `Cliente`.
- Atributos:
  - `cpf`: CPF do cliente (apenas números).
  - `nome`: Nome completo do cliente.
  - `data_nascimento`: Data de nascimento do cliente.

### 3. `Conta`
- Representa uma conta bancária.
- Atributos:
  - `saldo`: O saldo atual da conta.
  - `numero`: O número da conta (sequencial).
  - `agencia`: Número fixo da agência (ex: "0001").
  - `cliente`: Referência ao objeto `Cliente` associado.
  - `historico`: Histórico de transações da conta.
- Métodos:
  - `sacar(valor)`: Realiza um saque, se o saldo e limites permitirem.
  - `depositar(valor)`: Realiza um depósito na conta.
  - `saldo()`: Retorna o saldo atual da conta.

### 4. `ContaCorrente`
- Subclasse de `Conta`.
- Atributos:
  - `limite`: Limite de saque da conta.
  - `limite_saques`: Número máximo de saques permitidos por dia.

### 5. `Historico`
- Mantém o histórico de transações de uma conta.
- Métodos:
  - `adicionar_transacao(transacao)`: Adiciona uma transação ao histórico.

### 6. `Transacao` (interface)
- Interface abstrata para as operações de transação.
- Método abstrato:
  - `registrar(conta)`: Registra a transação em uma conta específica.

### 7. `Saque`
- Subclasse de `Transacao`, que representa uma operação de saque.
- Método:
  - `registrar(conta)`: Realiza o saque e atualiza o saldo da conta.

### 8. `Deposito`
- Subclasse de `Transacao`, que representa uma operação de depósito.
- Método:
  - `registrar(conta)`: Realiza o depósito e atualiza o saldo da conta.

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario-poo.git
   cd sistema-bancario-poo


2. Execute o script principal:
   ```bash
   python3 main.py
