import random
from helper import lotm_profile
from helper import item
class Market:
    open: bool = True
    types: list = ["Lavos Squid Blood","Stellar Aqua Crystal","Night Vanilla Liquids","Gold Mint Leaves","Poison Hemlock","Dragon Blood Grass Powder",
                   "Hornacis Great Mountain Goat Horn","Human-Faced Rose Stalk","Purified Water","Tornapple Juice","Black-Rimmed Sunflower Powder","Golden Cloak Grass Powder",
                   "Mist Treant's True Root","Dark-Patterned Black Panther Spinal Fluid","Mist Treant Juice","Droplet Gem Powder","Fantasy Grass Essential Oil",
                   "Mutated Pituitary Gland of Thousand-Faced Hunter","Human Skinned Shadow's Characteristic","Thousand-Faced Hunter's Blood","Black Jimsonweed Juice","Dragontooth Grass Powder","Deep-sea Naga Hair",
                   "Ancient Wraith Dust","Core Crystal of Six-Winged Gargoyle","Golden Spring Water","Drago Bark","Ancient Wraith Remnant Spirituality","Six-Winged Gargoyle Eyes"]
    key = {
        9:["Lavos Squid Blood","Stellar Aqua Crystal","Night Vanilla Liquids","Gold Mint Leaves","Poison Hemlock","Dragon Blood Grass Powder"],
        8:["Hornacis Great Mountain Goat Horn","Human-Faced Rose Stalk","Purified Water","Tornapple Juice","Black-Rimmed Sunflower Powder","Golden Cloak Grass Powder","Poison Hemlock"],
        7:["Mist Treant's True Root","Dark-Patterned Black Panther Spinal Fluid","Mist Treant Juice","Droplet Gem Powder","Fantasy Grass Essential Oil"],
        6:["Mutated Pituitary Gland of Thousand-Faced Hunter","Human Skinned Shadow's Characteristic","Thousand-Faced Hunter's Blood","Black Jimsonweed Juice","Dragontooth Grass Powder","Deep-sea Naga Hair"],
        5:["Ancient Wraith Dust","Core Crystal of Six-Winged Gargoyle","Golden Spring Water","Drago Bark","Ancient Wraith Remnant Spirituality","Six-Winged Gargoyle Eyes"],
        4:["Bizarro Bane's Main Eye","Spirit World Plunderer's True Soul Body","Bizarro Bane's Blood","Spirit World Plunderer's Dust","Golden Grapevines","Fingernail-Sized Self-made Rubber Mask"],
        3:["Hound of Fulgrim's Eyes","Demonic Wolf of Fog's Transformed Heart","Hound of Fulgrim Blood","Demonic Wolf of Fog's White Frost Crystal","Ancient Records"],
        2:["Dark Demonic Wolf Heart","Dark Demonic Wolf Blood","Worm of Star","Worm of Time"],
        1:["Attendant of Mysteries Beyonder Characteristic","Spirit World Specialties"],
        0:["Fool's Uniqueness","Attendant of Mysteries Beyonder Characteristic"]
    }
    reversed_key = {item: number for number, items in key.items() for item in items}
    def __init__(self, ):
        pass
        self.market = []

    def refresh(self):
        self.market.clear()
        self.market = random.sample(self.types, k=5)

        
    
    def interface(self, player: lotm_profile.Lotm_profile):
        
            buysell = input("Welcome to the market. Would you like to buy or sell? B for Buy, S for Sell, Q for Quit.").upper().strip()
            if buysell == "B":
                print(f"Items for sale: {', '.join(self.market)}")
                buy = input("Which item would you like to buy?")
                if buy in self.market:
                    if player.moneyCount()>=5**(10-self.reversed_key[buy]):
                        self.market.remove(buy)
                        player.addItem(item.Item(self.reversed_key[buy],buy))
                        player.loseMoney(5**(10-self.reversed_key[buy]))
                        print("Thank you!")
                        
                    else:
                        print("You do not have enough money to purchase this item.")
                else:
                    print("The market does not have this item.")
                self.interface(player)
            elif buysell == "S":
                target = input("Which item would you like to sell? ").strip()
                found_item = next((i for i in player.getInventory() if i.name == target), None)

                if found_item:
                    value = int(0.7 * 5 ** (10 - self.reversed_key[found_item.name]))
                    player.removeItem(found_item)
                    player.getMoney(value)
                    print(f"You sold {target} for {value} coins.")
                    
                else:
                    print("That item is not in your inventory.")
                self.interface(player)
            
            elif buysell == "Q":
                return
            else:
                print("Select B, S, or Q.")
                self.interface(player)
                

                
                