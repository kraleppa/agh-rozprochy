import socket;

serverIP = "127.0.0.1"
serverPort = 9008
msg = "Ping Python Udp!"

print('PYTHON UDP CLIENT')
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg_bytes = (300).to_bytes(4, byteorder='big')
client.sendto(msg_bytes, (serverIP, serverPort))

data, addr = client.recvfrom(1024)
data = int.from_bytes(data, byteorder='big')
print("received message: %s" % data)




