import time
import sqlite3
import asyncio

from Character_Card_table import Character_Card_table
from updata import random_updata
from retirement_module import dead

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')
class raund_3():
    async def start(list_of_player):
        sek = (5,4,3,2,1)

        print("3-ой раунд начинается через минуту")

        time.sleep(30)
        
        print("3-ой раунд начинается через 30 секунд")

        await raund_3.secret_player_1(player=list_of_player[0])

        time.sleep(25)

        print("Начало через:")

        for x in sek:
            print(x)
            time.sleep(1)

        print("2 раунд начался")
        await raund_3.player_hod(list=list_of_player)
        
    async def secret_player_1(player):
        user_is = player[0]
        discord_id = player[1]
        print("Ваш ход через 40 секунд\nНадеюсь вы выбрали карту")
        
    async def player_hod(list):
        for x in list:
            print(f"Ход игрока {x[1]} через 10 секунд")
            time.sleep(10)
            y = await random_updata.logik_2(user_id= x[0], ethalon= 2)
            if y == 200:
                pass
            elif y == 404:
                await raund_3.vibor(check=0, user_id= x[0])
            else:
                await raund_3.vibor(check=0, user_id= x[0])
            print(f"Ход игрока <@{x[1]}>")
            time.sleep(30)
            print(f"Ход игрока {x[1]} окончен")

        await Character_Card_table.table_player(list_of_players=list)
        print("2-ой раунд окончен ")
        print("Голосование начнется через минуту")
        check = await dead.main(list_of_players=list)
        if check == 200:
            pass