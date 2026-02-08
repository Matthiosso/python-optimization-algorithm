import sys
import math

# Save humans, destroy zombies!

class Human:
    def __init__(self, id, x, y, x0, y0):
        self.id = id
        self.x = x
        self.y = y
        self.x0, self.y0 = x0, y0
        self.dist = math.dist((x, y), (x0, y0))

class Zombie:
    def __init__(self, id, x, y, destX, destY):
        self.id = id
        self.x = x
        self.y = y
        self.destX = destX
        self.destY = destY


# game loop
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    humans = []
    zombies = []
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append(Human(human_id, human_x, human_y, x, y))
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_x_next, zombie_y_next = [int(j) for j in input().split()]
        zombies.append(Zombie(zombie_id, zombie_x, zombie_y, zombie_x_next, zombie_y_next))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    nb_human = len(humans)
    human_center = int(sum(h.x for h in humans)/nb_human), int(sum(h.y for h in humans)/nb_human)
    humans.sort(key=lambda x: x.dist)
    closest_human = humans[0].x, humans[0].y
    #targetX, targetY = humans[0].x, humans[0].y
    targetX, targetY = closest_human


    # Your destination coordinates
    print(f"{targetX} {targetY}")
