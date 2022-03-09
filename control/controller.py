import asyncio
from random import randint

from model.lamport_clock import LamportClock
from model.log import Log


class LamportClocksController:
    def __init__(self, num_clocks: int, cycles: int):
        self.log = Log()
        self.clocks = self.create_clocks(num_clocks)
        self.cycles = cycles

    def create_clocks(self, num_clocks: int):
        return [(LamportClock(i, num_clocks)) for i in range(num_clocks)]

    def choose_sender_receiver(self):
        sender = randint(0, len(self.clocks)-1)
        while True:
            receiver = randint(0, len(self.clocks)-1)
            if receiver != sender:
                return sender, receiver

    def send_ramdom_message(self):
        sender, receiver = self.choose_sender_receiver()
        sender_message = self.clocks[sender].send_message()
        self.clocks[receiver].receive_message(sender_message)
        self.log.write_message(f'!!!! Clock {sender} sent a message to Clock {receiver} !!!!')

    def send_message_from_to(self, sender: int, receiver: int, time: int = 0):
        sender, receiver = sender, receiver
        sender_message = self.clocks[sender].send_message()
        self.clocks[receiver].receive_message(sender_message)
        self.log.write_message(f'!!!! Clock {sender} sent a message to Clock {receiver} !!!!')
        self.log.write_message(f'!!!! {sender_message} !!!!')

    def log_current_clocks_vectors(self):
        self.log.write_message('CURRENT VECTORS STATES:')
        for count, clock in enumerate(self.clocks):
            self.log.write_message(f'Clock {count} Vector = {clock.time_vector}')

    def test_routine(self):
        self.send_message_from_to(0, 1)
        self.log_current_clocks_vectors()
        self.send_message_from_to(1, 0)
        self.log_current_clocks_vectors()
        self.send_message_from_to(0, 2)
        self.log_current_clocks_vectors()
        self.send_message_from_to(0, 3)
        self.log_current_clocks_vectors()

    def random_routine(self):
        self.log.write_message(f'Starting random routine with {len(self.clocks)} Clocks and {self.cycles} Cycles\n')
        counter = 0
        while counter < self.cycles:
            counter += 1
            self.log.write_message(f'------------ CYCLE {counter} STARTING ------------')
            self.send_ramdom_message()
            self.log_current_clocks_vectors()
            self.log.write_message('------------------------------------------\n')
