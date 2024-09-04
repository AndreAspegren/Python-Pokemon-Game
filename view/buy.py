import asyncio
import os


inp = None

async def buy_items(gold, trainer):
    global inp
    inp = '' 
    while inp not in ['1', '2', '']:
        os.system('cls')
        print(f'''
Gull: {gold}

Pokeballer: {trainer.pokeballs}
Potions: {trainer.potions}

Pris for 1 pokeball: 20
Pris for 1 potion: 30
''')
        inp = await input()
