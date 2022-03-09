class Message:
    def __init__(self, sender_id: int, sender_time_vector: list):
        self.sender_id = sender_id
        self.sender_time_vector = sender_time_vector

    def __repr__(self):
        return f'MESSAGE - From: Clock {self.sender_id} - CurrentTimeVector: {self.sender_time_vector}'