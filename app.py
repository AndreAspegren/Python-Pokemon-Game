from view import *
from actors import *
from logic import *
import os
import asyncio

async def play():
    while game_on:
        os.system('cls')
        main_view(gold, pokemon[-1])
        choice = input('>')
        os.system('cls')
        if choice == '1': await wild_encounter(pokemon, trainers[0])
        elif choice == '2': await battle_manager(game_on, trainers)
        elif choice == '3': await buy_items(gold, trainers[0])
        elif choice == '4': await see_roster(trainers[0].roster)
        else: continue

asyncio.run(play())