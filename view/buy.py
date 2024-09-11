import asyncio
import os



async def buy_items(gold, trainer):
    inp = '' 
    while inp != '3':
        os.system('cls')
        print(f'''
Gull: {gold}

Pokeballer: {trainer.pokeballs}
Potions: {trainer.potions}

Pris for 1 pokeball: 20
Pris for 1 potion: 30

Trykk 1 for pokeball
Trykk 2 for potion
Trykk 3 for å forlate shoppen
''')
        inp = input('>')
        if inp == '1' : await buy_item(gold, trainer, 'pokeball', 20)
        elif inp == '2': await buy_item(gold, trainer, 'potion', 30)


async def buy_item(gold, trainer, item_type, cost):
    os.system('cls')
    if gold >= cost:
        print(f'Du kjøpte en {item_type}!')
        gold -= cost
        if item_type == 'pokeball':
            trainer.pokeballs += 1
        elif item_type == 'potion':
            trainer.potions += 1
    else:
        print(f'Du har ikke nok gull til å kjøpe en {item_type}!')
    asyncio.sleep(2)
