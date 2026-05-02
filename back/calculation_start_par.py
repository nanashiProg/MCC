import math

R = 8.314   # универсальная газовая постоянная
M = 0.029   # молярная масса воздуха
g = 9.81    # ускорение свободного падения
r = 0.1785   # плотность гелия

<<<<<<< HEAD:back/calculations.py
def calculation(diameter, weight, chute_diameter, speed, chute_speed):
=======
def startV(diameter):
>>>>>>> c21c8015929b4ae4792385cb95173278f506a655:back/calculation_start_par.py
    V0 = 4/3 * math.pi * (int(diameter)/2)**3
    return V0

def startF_lift(V0):
    F_lift = (100000*M/(R*20)-r)*V0*g
    return F_lift

def startF_net_lift(F_lift, weight, weight_ball):
    F_net_lift = F_lift - (int(weight) - int(weight_ball)) * g
    return F_net_lift
