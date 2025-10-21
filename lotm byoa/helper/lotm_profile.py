from .item import *
class Lotm_profile: 
    key = {
        "homeless":0,
        "peasant":50,
        "commoner":150,
        "business owner":600,
        "merchant":1000,
        "noble":2000
    }
    job = {
        1:"homeless",
        2:"homeless",
        3:"peasant",
        4:"peasant",
        5:"peasant",
        6:"peasant",
        7:"commoner",
        8:"commoner",
        9:"commoner",
        10:"commoner",
        11:"business owner",
        12:"business owner",
        13:"merchant",
        14:"merchant",
        15:"noble"
    }
    def __init__(self, sequence: int, pathway: str, special: str, status: str):
        self.sequence = sequence
        self.pathway = pathway
        self.special = special
        self.status = status
        self.money = 0
        self.danger = 1
        self.inventory = []
    
    def run(self):
        self.money+=self.key[self.status]

    def getMoney(self, money: int):
        self.money+=money

    def moneyCount(self):
        return self.money
    
    def loseMoney(self, money:int):
        self.money-=money
    
    def getSequence(self):
        return self.sequence
    
    def getPathway(self):
        return self.pathway
    
    def getInventory(self):
        return self.inventory
    
    def addItem(self, item:Item):
        self.inventory.append(item)
    
    def removeItem(self, item:Item):
        self.inventory.remove(item)
    

