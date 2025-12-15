import socket
ipvalue=input("ENTER WEBSITE URL(including www):")
ip=socket.gethostbyname(ipvalue)
print(f"IP ADDRESS:{ip}")