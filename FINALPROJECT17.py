class Survivor():
    #This sets health and inventory values for the player. The player loses health gradually, but it can be increased if the player obtains certain objects.
    def __init__(self):
        #These define values in which the survivor has, like inventory items, health, and water supply, as well as the location of the player.
        self.water = 0
        self.health = 100
        self.location_x, self.location_y = 0
        self.inventory = []

    def move(value, dx, dy):
        self.location_x += dx
        self.location_y += dy

    def move_to_water(self):
        self.move(dx=0, dy=3)

print("The last things you remembered were the plane's engines on fire and the discord that entailed as the plane went down.")

print("You wake up on sand, and find yourself on a deserted and uninhabited island. There are no natives, and seemingly no other survivors from the crash. You shout for help, but nobody replies. You have no forms of communication. It looks like you will be here for a while.")

print("Day 1")

print("As always, the first priority is to find fresh water. After all, the human body can only survive so long without it.")



print("After some exploring, you find a stream three miles north from the shore.")

def collect_water(value, Survivor):
        Survivor.water.append(value.water)