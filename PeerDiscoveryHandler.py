import threading
import time



class PeerDiscoveryHandler():
    def __init__(self,node):
        socketCommunication = node
     
    def start(self):
        statusThread = threading.Thread(target=self.status,args=())
        statusThread.start()
        discoveryThread = threading.Thread(target=self.discovery,args=())
        discoveryThread.start()
        
       
    def status(self):
        while True:
            print("status")
            time.sleep(10)
    
    def discovery(self):
        while True:
            print("discovery")
            time.sleep(10)
    
    def handshak(self,content_node):
        self.socketCommunication.send(content_node,"Handshake ...")
        
            