from p2pnetwork.node import Node
from PeerDiscoveryHandler import PeerDiscoveryHandler
from SocketConnector import SocketConnector

class SocketCommunication(Node):
    def __init__(self,ip,port):
        super(SocketCommunication,self).__init__(ip,port,None)
        self.peers = []
        self.peerDiscoveryHandler = PeerDiscoveryHandler(self)
        self.socketConnector = SocketConnector(ip,port)
        
    def connectToFirstNode(self):
        if self.socketConnector.port != 10001:
            self.connect_with_node('localhost',10001)
        
    def startCommunication(self):
        self.start()
        self.peerDiscoveryHandler.start()
        self.connectToFirstNode()
        
    def inbound_node_connected(self,connection_id):
        print("inbounde_node_connection ")
        self.send_to_node(connection_id,"Hi i am node who connected to")
        
        
    def outbound_node_connected(self, connection_id):
        print("outbound_node_connected ")
        self.send_to_node(connection_id,"Hi i am node who initial the connection ")
        
    def node_message(self,connected_node,message):
        print(message)
        
    def send(self,message):
        self.send_to_node(message)
        
    def broadcast(self,message):
        self.send_to_node(message)