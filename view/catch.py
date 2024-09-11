import random
import asyncio
import os

inp = ''

async def wild_encounter(pokemon, trainer):
    global inp
    rand = random.randint(0, len(pokemon) - 1)
    wild_pokemon = pokemon[rand]

    print(f'''En vill {wild_pokemon.name} dukket opp!''')
    await asyncio.sleep(2)
    
    while inp != '2' or inp != '1':
        os.system('cls')
        inp = input(f'''{wild_pokemon.sprite}

Du har {trainer.pokeballs} pokeballer!

1: fang pokemon
2: Stikk av
''')
        if inp == '1': catch_pokemon(wild_pokemon, trainer)
        elif inp == '2': await flee()


async def catch_pokemon(wild_pokemon, trainer):
    caught = random.random() > 0.5
    os.system('cls')

    if caught: 
        print(f'Du fanget {wild_pokemon.name}! Gratulerer!')
        await asyncio.sleep(2)
        trainer.pokemon.append(wild_pokemon)
    else: 
        print(f'Oida! {wild_pokemon.name} stakk av :(')
        await asyncio.sleep(2)


async def flee():
    os.system('cls')
    print('Du flyktet')
    await asyncio.sleep(2)


