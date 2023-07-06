class PingRequest:

    def __init__(self, dest, port, seq, payload):
        self.dest = dest
        self.port = port
        self.seq = seq
        self.payload = payload

# Getters
    def get_dest(self):
        return self.dest
    
    def get_port(self):
        return self.port

    def get_seq(self):
        return self.seq

    def get_payload(self):
        return self.payload