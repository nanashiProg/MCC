import math

R = 8.314   # универсальная газовая постоянная
M = 0.029   # молярная масса воздуха
g = 9.81    # ускорение свободного падения
r = 0.1785   # плотность гелия

def calculation(diameter, weight, chute_diameter, speed, chute_speed):
    V0 = 4/3 * math.pi * (int(diameter)/2)**3

    math_result = (100000*M/(R*20)-r)*V0*g



    return math_result