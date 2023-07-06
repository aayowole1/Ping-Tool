class PingResponse:
    def __init__(self, round_trip_time, is_valid_res):
            self.round_trip_time = round_trip_time
            self.is_valid_res = is_valid_res
        
        # Getters
    def get_round_trip_time(self):
        return self.round_trip_time

    def is_valid_response(self):
        return self.is_valid_res