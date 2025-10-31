# 🔐 TVC1 - Assinatura Digital e Criptografia de Mensagens

Projeto desenvolvido como trabalho avaliativo (TVC1) sobre criptografia, assinatura digital e verificação de integridade de mensagens.

## Integrantes

- **Igor Almeida Guedes - 202176007**
- **Rhuan Nascimento Ferreira - 202176033**

## Descrição do Projeto

Este projeto implementa um sistema completo de **criptografia híbrida** e **assinatura digital** utilizando algoritmos de criptografia assimétrica (RSA) e simétrica (AES).


## Arquitetura do Sistema

O projeto está organizado em módulos que executam etapas específicas do processo criptográfico:

### 1. `gerar_chaves.py` - Geração de Par de Chaves RSA
- Gera um par de chaves RSA 
- As chaves são exportadas no formato PEM
- Arquivos gerados:
  - `private_key.pem` - Chave privada (mantida em segredo)
  - `public_key.pem` - Chave pública (pode ser distribuída)

### 2. `origem.py` - Assinatura e Criptografia

1. Lê a mensagem do arquivo `mensagem.txt`
2. Calcula o hash SHA-256 da mensagem
3. Assina o hash com a chave privada RSA 
4. Gera uma chave AES aleatória
5. Criptografa a mensagem + assinatura 
6. Salva os arquivos:
   - `mensagem_cifrada.bin` - Mensagem e assinatura criptografadas
   - `chave_aes.bin` - Chave AES 

### 3. `destino.py` - Decriptografia e Verificação

1. Lê a chave e a mensagem cifrada
2. Decifra o conteúdo
3. Separa a mensagem original da assinatura digital
4. Calcula o hash da mensagem recebida
5. Verifica a assinatura usando a chave pública
6. Exibe o resultado da verificação

### 4. `main.py` - Orquestrador
- Executa automaticamente as três etapas em sequência
- Exibe mensagens de progresso no terminal
- Simplifica a execução do processo completo


## Como Executar

#### 1. Configure o ambiente (primeira vez)

Permissão para rodar scripts bash
```bash
chmod +x ./setup.sh
```

```bash
chmod +x ./run.sh
```

Configurar projeto
```bash
./setup.sh
```

O script `setup.sh` realiza:
- Verifica se Python 3 está instalado
- Cria um ambiente virtual (`venv`)
- Atualiza pip, setuptools e wheel
- Instala as dependências do `requirements.txt`

#### 2. Execute o projeto
```bash
./run.sh
```

O script `run.sh` realiza:
- tiva o ambiente virtual
- Executa `python src/main.py`
- Desativa o ambiente virtual automaticamente


## Dependências

- **Python 3**
- **cryptography** - Biblioteca para operações criptográficas

## Execução Manual (sem scripts)

Se preferir executar o projeto manualmente sem usar os scripts `setup.sh` e `run.sh`, siga estes passos:

### Configuração Inicial

```bash
# 1. Criar ambiente virtual
python3 -m venv venv

# 2. Ativar o ambiente virtual
source venv/bin/activate

# 3. Atualizar pip
pip install --upgrade pip

# 4. Instalar dependências
pip install cryptography
# ou
pip install -r requirements.txt
```

### Executar o Projeto

```bash
# Certifique-se de que o ambiente virtual está ativado
source venv/bin/activate

# Execute o projeto principal
python src/main.py
```

### Desativar o Ambiente Virtual

```bash
deactivate
```

---

**Desenvolvido com 🔐 por Igor Almeida Guedes e Rhuan Nascimento Ferreira**
