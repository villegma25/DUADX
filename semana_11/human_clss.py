class Head:
    def __init__(self):
        self.brain = "Functioning"
        self.eyes = 2


class Hand:
    def __init__(self):
        self.fingers = 5


class Feet:
    def __init__(self):
        self.toes = 5


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Leg:
    def __init__(self, feet):
        self.feet = feet


class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg


class Human:
    def __init__(self, torso):
        self.torso = torso


# Build parts
left_hand = Hand()
right_hand = Hand()

left_arm = Arm(left_hand)
right_arm = Arm(right_hand)

left_foot = Feet()
right_foot = Feet()

left_leg = Leg(left_foot)
right_leg = Leg(right_foot)

head = Head()

torso = Torso(head, left_arm, right_arm, left_leg, right_leg)
human = Human(torso)

# Print info
print("The human has", human.torso.head.eyes, "eyes and", human.torso.left_arm.hand.fingers, "fingers on the left hand.")
print("The human has", human.torso.right_leg.feet.toes, "toes on the right foot.")