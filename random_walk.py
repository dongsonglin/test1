from random import choice

class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points = num_points

        self.x_value = [0]
        self.y_value = [0]


    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            x_direction = choice([-1,1])
            x_distence = choice(list(range(0,6)))
            y_direction = choice([-1, 1])
            y_distence = choice([0, 5])

            x_step = x_direction*x_distence
            y_step = y_direction*y_distence

            if x_step== 0 and y_step == 0:
                continue

            new_x = self.x_value[-1]+x_step
            new_y = self.y_value[-1]+y_step

            self.x_value.append(new_x)
            self.y_value.append(new_y)