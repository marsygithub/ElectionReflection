import random

def red_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return 'hsl(0, {0}%, {1}%)'.format(random.randint(60, 100), random.randint(30, 75))


def blue_color(word, font_size, position, orientation, random_state=None, **kwargs):
    return 'hsl(225, {0}%, {1}%)'.format(random.randint(80, 100), random.randint(45, 65))
