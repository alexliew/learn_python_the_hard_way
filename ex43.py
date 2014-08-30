import random

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.map = scene_map

    def play(self):
        while True:
            self.map.opening_scene()

class Death(Scene):

    def enter(self):
        print("You are dead.")
        exit(0)

class CentralCorridor(Scene):

    def enter(self):
        print("You are in an endless corridor. It gleams and sparkles like it was just washed this morning. In fact, it WAS just washed this morning.")

        joke = input("A Gothon is guarding the way. Tell it a joke to defeat it: ")

        if joke.strip() == "":
            print("That wasn't much of a joke. The Gothon scowls and shoots you dead.")
            return 'death'
        else:
            return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):

    def enter(self):
        print("Racks upon racks of heavy weaponry are laid out before you.")
        print("A keypad seals the entrace to the neutron bomb. You have 10 guesses to find out what the correct key value [1 to 100] is.")

        ans = random.randint(1, 100)

        for i in range(10):
            guess = input()
            if not guess.isdigit():
                print("Wow, you just wasted one chance. Try a number next time alright?")
                continue
            guess = int(guess)
            if guess == ans:
                print("The door unlocks itself with a satisfying *CLICK*")
                return 'the_bridge'
            elif guess > ans:
                print("Try lower.")
            else:
                print("Try higher.")

        print("You've wasted your chances and the guards have arrived. Time to die.")
        return 'death'

class TheBridge(Scene):

    def enter(self):
        print("Main screen turn on. A man is saying something about \"zigs\".")

        input("Plant the bomb? [RETURN]")

        return 'escape_pod'

class EscapePod(Scene):

    def enter(self):
        print("You fasten the safety harness and pray that you survive your landing.")

        pod = input("There are two escape pods; one on the left and one on the right. Which do you take? ")

        if 'left' in pod:
            return 'death'
        else:
            print("You escaped successfully!")
            exit(0)


class Map(object):

    def __init__(self, start_scene):
        self.scenes = {'central_corridor': CentralCorridor(), 'laser_weapon_armory': LaserWeaponArmory(), 'the_bridge': TheBridge(), 'escape_pod': EscapePod(), 'death': Death()}
        self.scene = self.scenes[start_scene]
        self.started = False

    def next_scene(self, scene_name):
        self.scene = self.scenes[scene_name]

    def opening_scene(self):
        self.next_scene(self.scene.enter())


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
