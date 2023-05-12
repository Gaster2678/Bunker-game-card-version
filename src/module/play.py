import asyncio
from formation_of_player_data import data_generation

list_play = ((10,9),(24,99),(25,999))

class raund_1():
    pass

class raund_2():
    pass

class raund_3():
    pass

class raund_4():
    pass

class raund_5():
    pass

class Character_Card_table():
    
    async def heading():
        print("Nikname|Profession|Biology|Health|Hobby|Luggage|Evidense|Special_conditions")
        print("---------------------------------------------------------------------------")

    async def table_player(list_of_players):
        await Character_Card_table.heading()
        for player in list_of_players:
            user_id = player[0]
            ping_nick = player[1]
            
            await data_generation.start(user_id=user_id,nick= ping_nick)


asyncio.run(Character_Card_table.table_player(list_of_players=list_play))
