import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

while True:
    a = int(input("Enter number A: "))
    b = int(input("Enter number B: "))

    print("Add =", proxy.add(a, b))
    print("Sub =", proxy.sub(a, b))
    print("Mul =", proxy.mul(a, b))
    print("Div =", proxy.div(a, b))
    print("Mod =", proxy.mod(a, b))
    
    print()