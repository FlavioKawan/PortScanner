import socket


ip = input("Digite o endereço IP")
ports = range(63535)

for port in ports:
    cliente = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    cliente.settimeout(0.05)

    code = cliente.connect_ex ((ip , port))



    if code == 0 :
        print(str(port))
   
