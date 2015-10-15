import socket
import SocketServer

def get_temp():
	tempfile = open("/sys/bus/w1/devices/28-0315715dbaff/w1_slave")
	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split("\n")[1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature / 1000
	return str(round(temperature,2))

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
	print "connection received"
        self.request.sendall(get_temp())

class V6Server(SocketServer.TCPServer):
  address_family = socket.AF_INET6

if __name__ == "__main__":
    HOST, PORT = "2001:a60:f073:0:76da:38ff:fe00:5e92", 31337

    server = V6Server((HOST, PORT), MyTCPHandler)
    server.serve_forever()
