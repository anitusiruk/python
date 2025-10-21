import random
from helper import lotm_profile
from helper import market
from helper import item

key = {
    1: "seer",
    2: "seer",
    3: "seer"
}
alive: bool = True
print("You wake up and find yourself in the world of LOTM.\n"
      "Surviving is an ordeal, with monsters, occult organizations, and indescribable horrors lurking around every corner.\n"
      "Fortunately, there exists mystical potions one can take to gain powers to protect themselves.")

validPotion = False
while not validPotion:
    try:
        potion_num = int(input("Select a number from 1 to 3. This will be the potion that you will start out trying to obtain: "))
        if potion_num in key:
            potion = key[potion_num]
            validPotion = True
        else:
            print("Enter an integer between 1 and 3.")
    except ValueError:
        print("Enter a valid integer between 1 and 3.")

print("You have chosen the", potion, "potion.")

user = lotm_profile.Lotm_profile(10, potion, "none", "noble")
user.run()
market1 = market.Market()
day = 0
while alive and user.sequence>0 and day < 50:
    print("The sun rises on a new day.")
    user.run()
    day+=1
    print("Today is Day ",day,".")
    market1.refresh()
    actions: int = 3
    while actions > 0:
        action = input(f"You have {actions} actions left. What do you want to do? \nM for Market, J for Job, E for Explore, P for Profile, I for Info, and A to Advance: ").upper().strip()
        if action == "M":
            cash = user.money
            market1.interface(user)
            if cash != user.money:
                actions-=1
            
        if action == "P":
            print("Inventory: ")
            for item in user.getInventory():
                print(item.name,"(Sequence:",item.sequence,", Price:", int(0.7*5**(10-item.sequence)),")")
            print("Money: ",user.moneyCount())

        if action == "J":
            print("Your current profession is: ",user.status)
            choice = input("Do you wish to reroll?(Y/N)").upper().strip()
            if choice == "Y":
                user.status = user.type[random.randint(1, 15)]
                actions-=1

        if action == "E":
            n = int(user.sequence)

            possible_sequences = [n - 1, n, n + 1]

            valid_sequences = [seq for seq in possible_sequences if seq in market1.key and market1.key[seq]]

            if not valid_sequences:
                print("No available items for nearby sequences.")
            else:
                chosen_seq = random.choice(valid_sequences)
                item_name = random.choice(market1.key[chosen_seq])
                new_item = item.Item(chosen_seq, item_name)
                user.inventory.append(new_item)
                actions -=1

                print(f"You found '{item_name}' (Sequence {chosen_seq})!")


        if action == "A":
            seq = user.sequence-1
            required_items = market1.key.get(seq, [])

            if not required_items:
                print("There are no available ritual ingredients for this sequence.")
            elif len(required_items) < 2:
                print("Not enough key ingredients exist for this sequence to attempt advancement.")
            else:
                mandatory = required_items[:2]
                boosters = required_items[2:]
                inventory_names = [i.name for i in user.inventory]
                if all(item in inventory_names for item in mandatory):
                    booster_count = sum(1 for item in boosters if item in inventory_names)
                    success_chance = 0.8 + 0.05 * booster_count
                    if seq ==1:
                        success_chance-=0.1
                    if seq == 0:
                        success_chance-=0.3
                    success_chance = min(success_chance, 1.0) 
                    print(f"Attempting advancement ritual for Sequence {seq}...")
                    print(f"Success chance: {int(success_chance * 100)}%")
                    for item_name in mandatory + boosters:
                        for inv_item in user.inventory:
                            if inv_item.name == item_name:
                                user.inventory.remove(inv_item)
                                break
                    roll = random.random()
                    if roll < success_chance:
                        user.sequence -= 1
                        print(f"Success. You are now Sequence {user.sequence}.")
                        actions -=1
                    else:
                        alive = False
                        actions = 0
                        print("You have lost control and died.")
                else:
                    print("You do not have all the core ritual materials needed for advancement.")

        if action == "I":
            print("Each day you are paid a set amount of money depending on your social class.\nBuy and sell items at the market, which refreshes each day with new materials.\nExplore for the chance of valuable materials.\nAdvance in sequence by drinking potions to become more powerful. A complete list of potion formulas can be found on the LOTM wiki.")

if day >=50:
    if user.sequence <= 0:
        print("Congratulations! You have become a true god and won the game! Amon is powerless against you.")
    else:
        print("You see a curly-haired young man walk up to you. He is wearing a black pointy hat and a crystal monocle on his right eye. You have died.")

else:
    print("You have become The Fool.")
exit()

        


