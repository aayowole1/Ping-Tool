import socket
import time
from DNSResolver import resolve
from PingSender import send_ping_request
from PingRequest import PingRequest
from PingStats import PingStats

def main():
    # User Inputs
    target = input("Enter the IP address or hostname to ping: ")
    port = int(input("Enter the port number to check: "))
    num_of_attempts = int(input("Enter the number of ping attempts: "))

    try:
        address = resolve(target)
        stats = PingStats()

        for num in range(num_of_attempts):
            ping_req = PingRequest(address, port, num + 1, "Ping-Payload")

            # Send the ping request and handle the response
            ping_resp = send_ping_request(ping_req)

            if ping_resp.is_valid_response():
                stats.update_stats(ping_resp.get_round_trip_time())

            # Display the result
            print("Ping request to {}, Port: {}, Sequence Number: {}, RTT: {} ms".format(ping_req.get_dest(), ping_req.get_port(), ping_req.get_seq(), ping_resp.get_round_trip_time()))

            # Sleep for 5 secs between ping requests
            time.sleep(5)
    except ValueError as e:
        print("Invalid target IP address or hostname:", target)
    except Exception as e:
        print("An error occurred: ", e)

if __name__ == '__main__':
    main()