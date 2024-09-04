import os
import random
from .movemethods import *
from actors.trainers import *

p1faster = None
name = None
max_hp = None
hp = None
base_attack = None
attack = None
speed = None
movelist = None
inp = None

async def battle_manager(game_on):
    if len(trainers[0].roster) < 1: return input('Du må ha minst en pokemon for å sloss mot rivalen din!')
    while game_on:
        await player_action()
        check_speed()
        set_speed()
        for i in range(2):
            announce_move(i)
            make_move(i)
            handle_death(i)
            handle_switch(i)
            check_end(i)
    game_over()


async def player_action():
    global inp
    inp = ''
    while inp != '1' or inp != '2' or inp != '3' or inp !='4':
        os.system('cls')
        mon = trainers[0].roster[0]
        options = ''
        for i, move in enumerate(mon.movelist):
            options += f'{i + 1}: {move}\n'
        options += f'{len(mon.movelist) + 1}: Potions ({trainers[0].potions})\n'
        inp = input(options)

def check_speed():
    global p1faster
    if trainers[0].roster[0].speed > trainers[1].roster[0].speed: p1faster = True
    elif trainers[0].roster[0].speed < trainers[1].roster[0].speed: p1faster = False
    else: p1faster = random.random() > 0.5

def set_speed():
    global p1faster
    global name
    global max_hp
    global hp
    global base_attack
    global attack
    global speed
    global movelist
    name = [trainers[0].roster[0].name, trainers[1].roster[0].name] if p1faster else [trainers[1].roster[0].name, trainers[0].roster[0].name]
    max_hp = [trainers[0].roster[0].max_hp, trainers[1].roster[0].max_hp] if p1faster else [trainers[1].roster[0].max_hp, trainers[0].roster[0].max_hp]
    hp = [trainers[0].roster[0].hp, trainers[1].roster[0].hp] if p1faster else [trainers[1].roster[0].hp, trainers[0].roster[0].hp]
    base_attack = [trainers[0].roster[0].base_attack, trainers[1].roster[0].base_attack] if p1faster else [trainers[1].roster[0].base_attack, trainers[0].roster[0].base_attack]
    attack = [trainers[0].roster[0].attack, trainers[1].roster[0].attack] if p1faster else [trainers[1].roster[0].attack, trainers[0].roster[0].attack]
    speed = [trainers[0].roster[0].speed, trainers[1].roster[0].speed] if p1faster else [trainers[1].roster[0].speed, trainers[0].roster[0].speed]
    movelist = [trainers[0].roster[0].movelist, trainers[1].roster[0].movelist] if p1faster else [trainers[1].roster[0].movelist, trainers[0].roster[0].movelist]

def game_over():
    return
    