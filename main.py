import socket

socket.setdefaulttimeout(0.5)

active_ports = {
    socket.SOCK_DGRAM: [],
    socket.SOCK_STREAM: []
}

for port in range(1, 65536):
    for protocol in [socket.SOCK_STREAM, socket.SOCK_DGRAM]:
        conn = socket.socket(socket.AF_INET, protocol) 

        err = conn.connect_ex(("localhost", port))
        if protocol == socket.SOCK_STREAM and err == 0: 
            active_ports[socket.SOCK_STREAM].append(port)
        elif protocol == socket.SOCK_DGRAM:
            try:
                conn.send(b"")
                err = conn.recv(1024)
                active_ports[socket.SOCK_DGRAM].append(port)
            except Exception as e:
                pass
    
        conn.close()

from pprint import pprint

pprint(active_ports)
