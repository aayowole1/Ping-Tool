class PingStats:
    def __init__(self):
            # Total packets sent & total packer received 
            self.total_sent = 0
            self.total_received = 0
            self.min_rtt = float('inf')
            self.max_rtt = 0
            self.total_rtt = 0

# Update Stats function
    def update_stats(self, round_trip_time):
        self.total_sent += 1
        self.total_received += 1
        self.total_rtt += round_trip_time

        if round_trip_time < self.min_rtt:
            self.min_rtt = round_trip_time
        
        if round_trip_time > self.max_rtt:
            self.max_rtt = round_trip_time

# Getters
    def get_total_packets_sent(self):
        return self.total_packets_sent

    def get_total_packets_rec(self):
        return self.total_packets_rec

    def get_min_rtt(self):
        return self.min_rtt

    def get_max_rtt(self):
        return self.max_rtt

    def get_average_rtt(self):
        if self.total_packets_rec == 0:
            return 0
        return self.total_rtt / self.total_packets_rec

    def get_packet_loss_percentage(self):
        if self.total_packets_sent == 0:
            return 0
        return (self.total_packets_sent - self.total_packets_rec) / self.total_packets_sent * 100