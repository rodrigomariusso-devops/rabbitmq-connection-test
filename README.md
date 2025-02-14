# RabbitMQ Connection Tester

## Descrição
Este projeto é um script Python para testar a conexão com um servidor RabbitMQ, validando se as credenciais e os parâmetros de conexão estão corretos.

## Como usar

### 1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/RabbitMQ-Connection-Tester.git
cd RabbitMQ-Connection-Tester
```

### 2. Instale as dependências
```bash
pip install pika
```

### 3. Execute o script
```bash
python app.py
```

Por padrão, o script tentará se conectar ao servidor `sua.url.com` na porta `5672` usando as credenciais padrão.

### 4. Personalizar parâmetros de conexão
Você pode fornecer argumentos personalizados para testar diferentes configurações:
```bash
python app.py <host> <port> <user> <password> <virtual_host>
```

Exemplo:
```bash
python app.py rabbitmq.meuservidor.com 5672 meu_usuario minha_senha /
```

## Estrutura do Projeto
```
RabbitMQ-Connection-Tester/
│── app.py               # Script Python que testa a conexão com o RabbitMQ
```

## Requisitos
- Python 3
- Biblioteca `pika` instalada (`pip install pika`)

## Possíveis Melhorias Futuras
- Adicionar suporte para saída em JSON
- Implementar logs estruturados
- Criar uma interface gráfica simples para facilitar os testes

