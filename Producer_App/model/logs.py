class Logs:
    def __init__(self, name, message):
        self.name = name
        self.message = message
    
    def send_log(self):
        return {
            'name': self.name,
            'message': self.message
        }