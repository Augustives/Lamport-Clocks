from operator import imod
from model.message import Message


class LamportClock:
    def __init__(self, id: int, num_clocks: int):
        self.id = id
        self.time_vector = [0]*num_clocks
        self.message_queue = []

    # This could be used for future implementations of a queue
    # def check_message_queue(self):
    #     for message in self.message_queue:
    #         if not self.there_is_time_difference(message):
    #             self.update_time_vector(message.sender_time_vector)
    #             self.message_queue.remove(message)
    #             return self.check_message_queue()

    # def there_is_time_difference(self, message: Message):
    #     for count, time_stamp in enumerate(message.sender_time_vector):
    #         if count != message.sender_id and count != self.id:
    #             if time_stamp != self.time_vector[count]:
    #                 return True
    #     return False

    def local_event(self):
        self.time_vector[self.id] += 1

    def update_time_vector(self, time_vector: list):
        self.time_vector[self.id] += 1
        for count, time_stamp in enumerate(time_vector):
            if count != self.id and self.time_vector[count] < time_stamp:
                self.time_vector[count] = time_stamp

    def send_message(self):
        self.time_vector[self.id] += 1
        return Message(self.id, self.time_vector.copy())
        
    def receive_message(self, message: Message):
        self.update_time_vector(message.sender_time_vector)