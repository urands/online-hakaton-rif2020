import rpcgrid as rpcg
from rpcgrid.providers import RabbitMQProvider


@rpcg.register
def address_normalize(data):
    address = address_parse(data)
    return address

if __name__ == '__main__':
    # Create RPC TCP server on port 1234
    rpcserver = rpcg.create(RabbitMQProvider(port = 1234))
    rpcserver.run()
