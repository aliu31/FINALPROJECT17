class Player(object):
    # This sets the class, where all functions are defines under this class.
    def __init__(self,name):
        #This defines all the scenes and sets the inital scene at scene 0.
        self.name = name
        self.all_scenes = [scene0, scene1, scene2, scene3, scene4, scene5, scene6, scene7, scene8, scene9, scene10, scene11, scene12, scene13, scene14, scene15, scene16, scene17, scene18, scene19, scene20, scene21, scene22, scene23, scene24, scene25, scene26, scene27]
        self.current_scene = 0

    def run_scene(self):
        #This runs the loop and starts the program.
        scene = self.all_scenes[self.current_scene]

        print(scene.desc)
        # This will print out the initial scene.

        for k, v in scene.choices.items():
            #This creates a dictionary to match choices with the scenes they lead to.
            print(f" -{k}:{v}")

        choice = input('a, b or c?')
        # This would take the human input and guide the user to the next step.
        if choice == 'a':
            self.current_scene = scene.next_a
        if choice == 'b':
            self.current_scene = scene.next_b
        elif choice =='c':
            self.current_scene = scene.next_c

class Scene(object):
    #This would lay out the options for the user to pick, and show what happens when the user picks a, b, or c.
    def __init__(self, desc, choice_a, choice_b, choice_c, next_a, next_b, next_c):
        self.desc = desc
        self.choices = {'a': choice_a, 'b': choice_b, 'c': choice_c}
        self.next_a = next_a
        self.next_b = next_b
        self.next_c = next_c

scene0 = Scene("You suddenly wake up on a desert island. You have no idea where you are.", "Climb up high so you can see", "Go for a swim", "Explore the island", 1, 2, 3)

scene1 = Scene("You climb a palm tree and spot a stream of fresh water close by.", "Climb down and go to stream", "Jump down", "Climb down and keep exploring", 3, 7, 0)

scene2 = Scene("You walk into the ocean water.", "Continue away from shore", "Look for fish to catch", "Return to shore", 4, 11, 0)

scene3 = Scene("You walk northward to a stream of fresh water and drink. Water never tasted so good.", "Continue exploring", "Return to shore", "Look for fish in the water", 5, 0, 11)

scene4 = Scene("Turns out there's nothing here", "Continue swimming", "Return to the island", "Change direction and swim parallel to the shore", 6, 0, 6)

scene5 = Scene("You find fresh berries on a bush, however, you don't know if they are poisonous or not", "Try them", "Pocket them and return to shore", "Ignore them and continue exploring", 7, 8, 9)

scene6 = Scene("There's nothing around. You are stranded in the middle of nowhere. You drown after exhaustion.", "return to start", "return to start" , "return to start", 0, 0, 0)

scene7 = Scene("You made a grave mistake doing so. There's no medical care on this island. You died.", "return to start", "return to start", "return to start", 0, 0, 0)

scene8 = Scene("You go back to shore with the berries", "Eat them", "Leave them there", "Continue exploring", 7, 9, 3)

scene9 = Scene("You return back to shore. The day is almost over, and the sun has just set.", "collect sticks for fire", "collect rocks to make an SOS signal", "do neither and go to sleep", 10, 13, 12)

scene10 = Scene("You collect a small bundle of sticks and make a sufficient fire", "make an SOS signal with rocks", "continue exploring", "get some rest", 13, 12, 12)

scene11 = Scene("There are no fish here.", "return to previous scene (ocean)", "return to previous scene (stream)", "return to previous scene", 2, 3, 3)

scene12 = Scene("You get tired and go to sleep. You wake up the next day.", "Continue exploring", "Continue to sleep", "sing a song to pass the time", 14, 15, 16)

scene13 = Scene("You make a big SOS signal with rocks, and return to your camp.", "Return to your settlement", "Return to your settlement", "Return to your settlement", 9, 9, 9)

scene14 = Scene("You see a small animal, about the size of a rabbit.", "Kill it and use it for food", "Spare it", "Chase it away", 18, 12, 12)

scene15 = Scene("You try to continue sleeping, but the sun is too bright for you, and you ultimately give up.", "Go back to previous scene", "Go back to previous scene","Go back to previous scene", 12, 12, 12)

scene16 = Scene("Your loud singing has attracted a few animals. You see a small animal, about the size of a rabbit.", "Kill it and use it for food", "Spare it", "Chase it away", 18, 12, 12)

scene17 = Scene("The animal you killed was a baby, and its mother, ten times larger than the baby, has found you and fatally attacked you.", "return to start", "return to start", "return to start", 0, 0, 0)

scene18 = Scene("You chase the animal, and ultimately outrun it, and suffocate the thing easily.", "Bring it back to camp", "Feel regretful and leave it behind", "Look for more animals", 19, 12, 17)

scene19 = Scene("You bring your animal back to camp and use your fire to cook it and eat it. It tastes great. You've enjoyed your dinner and the sun is about to set.", "sleep", "sing a song to pass the time", "continue exploring", 20, 22, 22)

scene20 = Scene("You wake up the next day and see a small speck in the distance. Could this be rescue, or just a mirage?", "scream at the top of your lungs", "jump around and wave your arms", "ignore it and continue on with your day", 21, 21, 23)

scene21 = Scene("Your ecstatic movements may have worked, because the speck is slowly getting bigger. This must mean rescue by now.", "Continue screaming to make sure it's a rescue boat", "relax and wait", "ignore and move on", 24, 24, 23)

scene22 = Scene("You stay up a little longer, but you eventually get tired.", "Sleep", "Sleep", "Sleep", 20, 20, 20)

scene23 = Scene("You decide to ignore it, thinking it was a mirage.", "continue exploring", "sing to yourself", "relax and wait for rescue", 25, 25, 25)

scene24 = Scene("Yes, it's a boat! It saw you and it is moving quicker towards your island. Within 20 minutes, you are rescued.", "Ask the seaman on the ship for information", "Thank him", "Be rude to him", 26, 26, 26)

scene25 = Scene("You see a small plane above you, up in the distance. You run towards your SOS signal, and fortunately, the pilot sees you and flies down to your rescue.", "Ask the pilot for information", "Thank her", "Be rude to her", 26, 26, 26)

scene26 = Scene("You have survived the island and made it home safely.", "play again", "quit", "play again", 0, 27, 0)

scene27 = Scene("hahaha you're a quitter hahaha", "tide pod", "spaghet", "do u kno da wae", 0, 0, 0)

player = Player("Alex")

while player.current_scene not in [27]:
    # This will let the program run smoothly, instead of showing a blank when opened. It will also close the program if the player chooses to quit.
    player.run_scene()