class SocketConnector():
    def __init__(self,id,port):
        self.id = id
        self.port = port
    
        
    def equal(self,connector):
        if connector.id == self.id and connector.port == self.port:
            return True
        else:
            return False
        
        
        
        