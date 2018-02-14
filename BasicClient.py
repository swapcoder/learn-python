import sys
import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
with open(sys.argv[1],"rb") as handle :
    binary_data=xmlrpc.client.Binary(handle.read())
    proxy.save_data(binary_data)
