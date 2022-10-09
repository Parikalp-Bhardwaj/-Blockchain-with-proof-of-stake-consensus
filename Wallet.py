from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from numpy import sign
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Block import Block


class Wallet:
    def __init__(self):
        self.keyPair = RSA.generate(2048)


    def sign(self,data):
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKCS1_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()

    
    #Signature is Valid or not
    @staticmethod
    def signatureValid(data,signature,publicKeyString):
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.import_key(publicKeyString)     
        signatureSchemeObject = PKCS1_v1_5.new(publicKey)
        signatureValid = signatureSchemeObject.verify(dataHash,signature)
        return signatureValid
    
    
    def publicKeyString(self):
        publicKeyString = self.keyPair.publickey().exportKey("PEM").decode("utf-8")
        return publicKeyString
    
    def createTransaction(self,receiver,amount,type):
        transaction = Transaction(self.publicKeyString(),receiver,amount,type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction
    
    def createBlock(self,transaction,lastHash,blockCount):
        block = Block(transaction,lastHash,self.publicKeyString(),blockCount)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block