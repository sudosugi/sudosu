from xmlrpc.server import SimpleXMLRPCServer

# Define all operations in one place
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b
def mod(a, b): return a % b

server = SimpleXMLRPCServer(("localhost", 8000))
print("XMLRPC Calculator Server running on port 8000...")

# Register all functions quickly
for func in (add, sub, mul, div, mod):
    server.register_function(func)

server.serve_forever()