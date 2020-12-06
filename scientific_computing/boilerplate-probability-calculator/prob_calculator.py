import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []

    for key in kwargs:
      for i in range(kwargs[key]):
        self.contents.append(key)

  def draw(self, num):
    drawn = []
    for i in range(min(num, len(self.contents))):
      drawn.append(random.choice(self.contents))
      self.contents.remove(drawn[i])

    return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  prob = 0

  for _ in range(num_experiments):
    c_hat = copy.deepcopy(hat)
    balls = c_hat.draw(num_balls_drawn)
    ball_dict = {}
    for i in range(len(balls)):
      if balls[i] not in ball_dict:
        ball_dict[balls[i]] = 1
      else:
        ball_dict[balls[i]] += 1

    pass_flag = True

    for key in expected_balls:

      if key not in ball_dict:
        pass_flag = False
        break

      if expected_balls[key] > ball_dict[key]:
        pass_flag = False
        break

    prob += (1 if pass_flag else 0)

  return (prob / num_experiments)
