from pypresence import Presence
import time

class DiscordRPC:
    def __init__(self, client_id):
        self.client_id = client_id
        self.rpc = None
        
    def connect(self):
        try:
            self.rpc = Presence(self.client_id)
            self.rpc.connect()
            return True
        except:
            return False
            
    def update_presence(self, details, state):
        if self.rpc:
            self.rpc.update(
                details=details,
                state=state,
                start=int(time.time()),
                large_image="gamebar_icon"
            )