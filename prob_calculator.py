import random
import copy
class Hat:
    def __init__(self,**kwargs) -> None:
        self.dict=(kwargs)
        self.contents = [key for key,value in self.dict.items() for _ in range(value)]
        self.deep=copy.deepcopy(self.contents)
    def draw(self,number):
        random_list=[]
        if number > len(self.contents):
            return self.contents
        else:
            for i in range(number):
                random_ball=random.choice(self.contents)
                random_list.append(random_ball)
                self.contents.remove(random_ball)
        return random_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    no_of_match = 0
    original_hat = copy.deepcopy(hat)  

    for _ in range(num_experiments):
        hat.contents = copy.deepcopy(original_hat.contents)  
        drawn_balls = hat.draw(num_balls_drawn)
        drawn_balls_dict = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        match = True
        for color, number in expected_balls.items():
            if drawn_balls_dict.get(color, 0) < number:
                match = False
                break  
        if match:
            no_of_match += 1

    return no_of_match / num_experiments






hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat,
                  expected_balls={"blue":2,"green":1},
                  num_balls_drawn=4,
                  num_experiments=1000)

print(probability)