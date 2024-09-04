import asyncio

async def see_roster(roster):
    if len(roster) < 1: 
        print('Du har ikke pokemon. Nothing to see here!')
        await asyncio.sleep(2)  
        return
    
    for mon in roster:
        print(f'''
{mon.name:<20}{" " * 5}{mon.sprite}
HP: {mon.max_hp:<5}{" " * 5}Attack: {mon.base_attack:<5}
Speed: {mon.speed:<5}
Moves: {', '.join(mon.movelist)}
''')
    
    await input('Trykk hva som helst for å gå tilbake til hovedmenyen')
