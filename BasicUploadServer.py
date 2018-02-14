import sys
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def save_data(d):
    with open(sys.argv[1],"ab") as handle :
        handle.write(d.data)
        return True

server = SimpleXMLRPCServer(("localhost",8000));
print (" Running at localhost:8000")
server.register_function(save_data,'save_data');
server.serve_forever()
