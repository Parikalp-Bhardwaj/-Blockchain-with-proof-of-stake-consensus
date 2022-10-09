from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

class Blockchain:
    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountBalance = AccountModel()
        
    
    def addBlock(self,block):
        self.blocks.append(block)
        self.executeTransactions(block.transactions)
        
    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        
        data["block"] = jsonBlocks
        return data
    
    def BlockchainValid(self,block):
        if self.blocks[-1].blockCount == block.blockCount -1:
            return True
        else:
            return False
        
    def lastBlockHashValid(self,block):
        lastBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        if lastBlockchainBlockHash == block.lastHash:
            return True
        else:
            return False 
        
    def getConveredTransaction(self,transactions):
        converedTransaction = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                converedTransaction.append(transaction)
            else:
                print("Transaction is not covered by sender")
        
        return converedTransaction
        
    def transactionCovered(self,transaction):
        if transaction.type == "EXCHANGE":
            return True
        senderBalance = self.accountBalance.getBalance(transaction.senderPublicKey)
        if senderBalance >= transaction.amount:
            return True
        else:
            return False
        
    def executeTransactions(self,transactions):
        for transaction in transactions:
            self.executeTransaction(transaction)
            
        
    def executeTransaction(self,transaction):
        sender = transaction.senderPublicKey
        receiver = transaction.receiverPublicKey 
        amount = transaction.amount
        self.accountBalance.updateBalance(sender,-amount)
        self.accountBalance.updateBalance(receiver,amount)
        
        