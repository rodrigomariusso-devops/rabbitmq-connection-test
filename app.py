import pika
import sys

def validate_rabbitmq_connection(host='', port=5672, user='', password='', virtual_host='/'):
    """Valida a conexão com o servidor RabbitMQ."""
    
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters(host=host, port=port, virtual_host=virtual_host, credentials=credentials)

    try:
        connection = pika.BlockingConnection(parameters)
        if connection.is_open:
            print("Conexão estabelecida com sucesso!")
            connection.close()
            return True
        else:
            print("Falha ao estabelecer conexão.")
            return False
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Erro ao conectar ao RabbitMQ: {e}")
        return False

if __name__ == "__main__":
    host = ''  #endereço do RabbitMQ
    port = 5672         # porta padrão do RabbitMQ
    user = ''      # usuário padrão
    password = ''  # senha padrão
    virtual_host = '/'  # virtual host padrão
    
    if len(sys.argv) > 1:
        host = sys.argv[1]
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    if len(sys.argv) > 3:
        user = sys.argv[3]
    if len(sys.argv) > 4:
        password = sys.argv[4]
    if len(sys.argv) > 5:
        virtual_host = sys.argv[5]

    validate_rabbitmq_connection(host, port, user, password, virtual_host)
