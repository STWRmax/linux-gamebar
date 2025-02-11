from pypresence import Presence
import notify2

def connect_discord():
    client_id = "123456789012345678"
    RPC = Presence(client_id)
    RPC.connect()
    RPC.update(state="Jugando en Linux", details="Usando Game Bar")
    
    notify2.init("Game Bar")
    notification = notify2.Notification("Discord Conectado", "Ahora estás conectado a Discord.")
    notification.show()