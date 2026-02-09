import sys
import math

# Save humans, destroy zombies!

MOVE_ZOMBIE = 400
MOVE_HERO = 1000
RANGE_HERO = 2000
MAP_SIZE = (16000, 9000)

def compute_line_between_two_coordinates(xA: int, yA: int, xB: int, yB: int) -> tuple:
    """
    Compute a and b representing the straight line crossing the two input coordinates (equation : y = a*x + b)

    Example :

    Input:
    pA = (1, 0)
    pB = (3, 2)

    Output:
    (1.0, -1.0) # y = x - 1
    """
    if xA == xB:
        return xA
    else:
        a = (yB - yA)/(xB - xA)
        b = yA - a*xA
        return a,b

def compute_perpendicular_line_crossing_one_coordinate(a: float, x: int, y: int):
    """
    Compute a and b representing the perpendicular line crossing a given axis (equation : y = a*x + b)
    
    Example :

    Input:
    a = 2.5
    pC = (7, 0)

    Output:
    (-0.4, 2.8000000000000003) # y = -0.4x+2.8000000000000003
    """
    newA = 0
    if a == 0:
        return x
    newA = -1/a
    newB = y - (newA * x)
    return newA, newB

def compute_crossing_point_between_two_lines(a1: float, b1: float, a2: float, b2: float) -> tuple:
    """
    Compute the coordinates of the point crossing two straight lines
    """
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return x, y

def get_point_from_line_crossing_C_and_perpendicular_with_line_between_A_and_B(point_A_x, point_A_y, point_B_x, point_B_y, point_C_x, point_C_y):
    """
    Get coordinates of the crossing point between the line from A to B, and its perpendicular line crossing C
    
    Example :

    Input:
    pA = (1, 1)
    pB = (6, 6)
    pC = (6, 1)

    Output:
    pD = (3.5, 3.5)
    """
    pointA = point_A_x, point_A_y
    pointB = point_B_x, point_B_y
    pointC = point_C_x, point_C_y

    print(f"Point A: {pointA} ; Point B: {pointB} ; Point C: {pointC}", file=sys.stderr, flush=True)

    line_A_B = compute_line_between_two_coordinates(*pointA, *pointB)
    if type(line_A_B) != tuple:
        print(f"Line A <-> B : x = {line_A_B}", file=sys.stderr, flush=True)
        raise Exception("A and B are aligned.")
    else:
        print(f"Line A <-> B : y = {line_A_B[0]}x+{line_A_B[1]}", file=sys.stderr, flush=True)
        line_crossing_C_perpendicular_to_line_A_B = compute_perpendicular_line_crossing_one_coordinate(line_A_B[0], *pointC)

    if type(line_crossing_C_perpendicular_to_line_A_B) != tuple:
        print(f"Line C <-> D : x = {line_crossing_C_perpendicular_to_line_A_B}", file=sys.stderr, flush=True)
        return pointA # Force Hero to move to human if both human and zombie are aligned with the hero
    else:
        print(f"Line C <-> D : y = {line_crossing_C_perpendicular_to_line_A_B[0]}x+{line_crossing_C_perpendicular_to_line_A_B[1]}", file=sys.stderr, flush=True)
        return compute_crossing_point_between_two_lines(*line_A_B, *line_crossing_C_perpendicular_to_line_A_B)

class Human:
    def __init__(self, id: int, x: int, y: int):
        self.id = id
        self.x = x
        self.y = y
        self.dist_to_hero = None
        self.turns_count_to_hero = None
        self.closest_zombie = None
        self.dist_to_zombie = None
        self.turns_count_to_zombie = None

    def __repr__(self):
        return f"Human({self.id}: ({self.x}, {self.y}), zombie_turns:{self.turns_count_to_zombie} vs hero_turns: {self.turns_count_to_hero})"

    def set_dist_to_hero(self, x, y):
        self.dist_to_hero = math.dist((self.x, self.y), (x, y))
        self.turns_count_to_hero = math.ceil(self.dist_to_hero / MOVE_HERO) - math.ceil(RANGE_HERO / MOVE_HERO) # Minus 2 turns to take into account the fact that the hero has a 2000 range 
        self.closest_zombie = None
    
    def set_closest_zombie(self, zombie) -> bool:
        dist_to_zombie = math.dist((self.x, self.y), (zombie.x, zombie.y))
        if not self.dist_to_zombie or (dist_to_zombie < self.dist_to_zombie):
            self.dist_to_zombie = dist_to_zombie
            self.closest_zombie = zombie.id
            self.turns_count_to_zombie = math.ceil(dist_to_zombie / MOVE_ZOMBIE)
            return True
        else:
            return False
       

class Zombie:
    def __init__(self, id: int, x: int, y: int, destX: int, destY: int):
        self.id = id
        self.x = x
        self.y = y
        self.destX = destX
        self.destY = destY
        

# game loop
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())

    humans = dict()
    zombies = dict()
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans[human_id] = Human(human_id, human_x, human_y)
        humans[human_id].set_dist_to_hero(x, y)
        
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_x_next, zombie_y_next = [int(j) for j in input().split()]
        zombie = Zombie(zombie_id, zombie_x, zombie_y, zombie_x_next, zombie_y_next)
        for human in humans.values():
            human.set_closest_zombie(zombie)
        zombies[zombie_id] = zombie
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    nb_human = len(humans.values())
    human_center = int(sum(h.x for h in humans.values())/nb_human), int(sum(h.y for h in humans.values())/nb_human)

    human_to_save = None
    sorted_humans = sorted(humans.values(), key=lambda x: x.turns_count_to_zombie)
    print(sorted_humans, file=sys.stderr, flush=True)
    for human in sorted_humans:
        if (human.turns_count_to_zombie >= human.turns_count_to_hero):
            human_to_save = human
            print(f"Human to save: {human_to_save}", file=sys.stderr, flush=True)
            break

    zombie_to_kill = zombies[human_to_save.closest_zombie if human_to_save else zombies.values().get(0)]
    targetX, targetY = 0, 0
    try:
        targetX, targetY = get_point_from_line_crossing_C_and_perpendicular_with_line_between_A_and_B(human_to_save.x, human_to_save.y, zombie_to_kill.x, zombie_to_kill.y, x, y)
        if ((targetX < human_to_save.x and targetY < human_to_save.x) and (targetX < zombie_to_kill.x and targetY < zombie_to_kill.y)) or ((targetX > human_to_save.x and targetY > human_to_save.x) and (targetX > zombie_to_kill.x and targetY > zombie_to_kill.y)):
            raise Exception("The target should be between human and zombie")
    except:
        dist_to_human = human_to_save.dist_to_hero
        dist_to_zombie = math.dist((x, y), (zombie.x, zombie.y))
        targetX, targetY = (human_to_save.x, human_to_save.y) if dist_to_human <= dist_to_zombie else (zombie.x, zombie.y)
    finally:
        # Your destination coordinates
        targetX, targetY = math.floor(targetX), math.floor(targetY)
        print(f"{targetX} {targetY}")
