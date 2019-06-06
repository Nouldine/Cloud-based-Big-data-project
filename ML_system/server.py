import socket
import sys

def convertToGrams(ret_text):
        print(ret_text)
        return ({}, {})

def classifyOffWorld(text):
        print("beginning")
#       if True:
#               return ({}, {})

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('10.142.0.3', 1300)
        print("connecting...")
        sock.connect(server_address)
        print("connected")
        sock.sendAll(text + " END")

        ret_text_list = []
        while True:
                data = sock.recv(1024)
                ret_text_list.append( data )
                if " END" in data:
                        break
                if data is None:
                        break
        socket.close()
        return convertToGrams("".join(ret_text_list))



