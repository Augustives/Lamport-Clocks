import logging


class Log:
    def __init__(self):
       self.configure_logging()

    def configure_logging(self):
        logging.basicConfig(
            filename='result.log',
            encoding='utf-8',
            level=logging.DEBUG,
            format='%(message)s',
            filemode='w'
        )

    def write_message(self, message: str):
        logging.info(message)    
