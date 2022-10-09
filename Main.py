# from Blockchain2.Blockchain import Blockchain
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node
import sys

if __name__ =="__main__":
    sender = "sender"
    receiver = "receiver"
    amount = 1
    type = "TRANSFER"
    # transaction = Transaction(sender,receiver,amount,type)
    # wallet = Wallet()
    # signature = wallet.sign(transaction.toJson())
    # transaction.sign(signature)
    
    # signatureValid = Wallet.signatureValid(transaction.payload(),signature,wallet.publicKeyString())
    # print(signatureValid)
    # # print(transaction.payload())
    
    wallet = Wallet()
    transaction = wallet.createTransaction(receiver,amount,type)
    signatureValid = Wallet.signatureValid(transaction.payload(),transaction.signature,wallet.publicKeyString())
    pool = TransactionPool()
    # print(transaction.toJson())
    # print(signatureValid)
    if pool.transactionExists(transaction) ==  False:
        pool.addTransaction(transaction)
    
    # block = Block(pool.transactions,"lastHash","forger",1)
    # print(block.toJson())
    
    # block = wallet.createBlock(pool.transactions,"lastHash",1)
    # print(block.toJson())
    
    # wallletValid = Wallet.signatureValid(block.payload(),block.signature,wallet.publicKeyString())
    
    # print(wallletValid) 
    
    #Blockchain
    
    # blockchain = Blockchain()
    # blockchain.addBlock(block)
    # pprint.pprint(blockchain.toJson())
    
    
    #
    
    
    blockchain = Blockchain()
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    block = wallet.createBlock(pool.transactions,lastHash,blockCount)
    
    
    if not blockchain.lastBlockHashValid(block):
        print("LastBlock hash is not valid")
        
    if not blockchain.BlockchainValid(block):
        print("Blockcount is not valid")
        
    
    
    if blockchain.lastBlockHashValid(block) and blockchain.BlockchainValid(block):
        blockchain.addBlock(block)
        
    # pprint.pprint(blockchain.toJson())
    
    # //AccountModel
    
    accountModel = AccountModel()
    accountModel.updateBalance(wallet.publicKeyString(),10)
    accountModel.updateBalance(wallet.publicKeyString(),-2)
    
    # print(accountModel.balances)
    
    # //Adding Transaction into the pool
    
    # blockchain = Blockchain()
    # pool = TransactionPool()
    
    # alic = Wallet()
    # bob = Wallet()
    # exchange = Wallet()
    # forger = Wallet()
    
    # exchangeTransaction = exchange.createTransaction(bob.publicKeyString(),10,"EXCHANGE")
    # if not pool.transactionExists(exchangeTransaction):
    #     pool.addTransaction(exchangeTransaction)
        
    # coveredTransaction = blockchain.getConveredTransaction(pool.transactions)
    
    # lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    # blockCount = blockchain.blocks[-1].blockCount + 1
    # blockOne = forger.createBlock(coveredTransaction,lastHash,blockCount)
    
    # blockchain.addBlock(blockOne)
    # pool.removeFromPool(blockOne.transactions)
    
    # transaction = alic.createTransaction(bob.publicKeyString(),5,"TRANSFER")
    # if not pool.transactionExists(transaction):
    #     pool.addTransaction(transaction)
    
    # coveredTransaction = blockchain.getConveredTransaction(pool.transactions)
    # lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    # blockCount = blockchain.blocks[-1].blockCount + 1
    # blockTwo = forger.createBlock(coveredTransaction,lastHash,blockCount)
    # blockchain.addBlock(blockTwo)
    # pool.removeFromPool(blockTwo.transactions)
        
    # pprint.pprint(blockchain.toJson())
    
    
    #  '''******************************Node Class**********************'''
    
    # node = Node()
    # print(node.blockchain)
    # print(node.transactionPool)
    # print(node.wallet)
    
    # '''**************************Socket Communication*******************************'''

    ip = sys.argv[1]
    port = int(sys.argv[2])
    node = Node(ip,port)
    node.startP2P()
    
    if port == 10002:
        node.p2p.connect_with_node('localhost',10001)
        