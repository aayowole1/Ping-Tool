import socket
import time

from PingResponse import PingResponse

TIMEOUT = 5

def send_ping_request(ping_request):
        if ping_request.get_port() == 0:
             return PingResponse(0, False)
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(TIMEOUT)
                result = sock.connect_ex((ping_request.get_dest(), ping_request.get_port()))

                if result == 0:
                     return PingResponse(0, True)
                else:
                     return PingResponse(0, False) 
            
        except socket.error as e:
            print("An error occured (asdf): ", e)
            return PingResponse(0, False)