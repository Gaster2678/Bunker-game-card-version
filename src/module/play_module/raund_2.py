import time
import asyncio
import sqlite3

from Character_Card_table import Character_Card_table
from updata import updata, random_updata
from retirement_module import dead
from raund_3 import raund_3

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')

class raund_2():
    async def start(list_of_player):
        sek = (5,4,3,2,1)

        print("2-ой раунд начинается через минуту")

        time.sleep(30)
        
        print("2-ой раунд начинается через 30 секунд")

        await raund_2.secret_player_1(player=list_of_player[0])

        time.sleep(25)

        print("Начало через:")

        for x in sek:
            print(x)
            time.sleep(1)

        print("2 раунд начался")
        await raund_2.player_hod(list=list_of_player)

    async def player_hod(list):
        for x in list:
            print(f"Ход игрока {x[1]} через 10 секунд")
            time.sleep(10)
            y = await random_updata.logik_2(user_id= x[0], ethalon= 2)
            if y == 200:
                pass
            elif y == 404:
                await raund_2.vibor(check=0, user_id= x[0])
            else:
                await raund_2.vibor(check=0, user_id= x[0])
            print(f"Ход игрока <@{x[1]}>")
            time.sleep(30)
            print(f"Ход игрока {x[1]} окончен")

        await Character_Card_table.table_player(list_of_players=list)
        print("2-ой раунд окончен ")
        print("Голосование начнется через минуту")
        check = await dead.main(list_of_players=list)
        if check == 200:
            new_list = await raund_2.new_list(list=list)            
            await raund_3.start(list_of_player=new_list)
            
    async def secret_player_1(player):
        user_is = player[0]
        discord_id = player[1]
        print("Ваш ход через 40 секунд\nНадеюсь вы выбрали карту")

    async def vibor(check,user_id):
        
        mass_edit = ("Biology","Health","Hobby","Luggage","Evidense","Special_conditions")
        if check == 1:
            await updata.updata_sql(user_id= user_id, updata= mass_edit[0])
        elif check == 2:
            await updata.updata_sql(user_id= user_id, updata= mass_edit[1])
        elif check == 3:
            await updata.updata_sql(user_id= user_id, updata= mass_edit[2])
        elif check == 4:
            await updata.updata_sql(user_id= user_id, updata= mass_edit[3])
        elif check == 5:
            await updata.updata_sql(user_id= user_id, updata= mass_edit[4])
        elif check == 6:
            await updata.updata_sql(user_id= user_id, updata= mass_edit[5])
        else:
            await random_updata.logik(user_id=user_id)

    async def tap(user_id_discord, number_tap):
        pass

    async def new_list(list):
        cur = connect_bd.cursor()
        cur.execute(f"""SELECT play_id
                    FROM Players
                    where user_id  = {list[0][0]}
                        """)
        
        id_room= cur.fetchall()
        connect_bd.commit()
        
        cur.execute(f"""SELECT user_id,id_player
                    FROM Players
                    where play_id = {id_room}
                        """)
        
        list_of_players = cur.fetchall()
        connect_bd.commit()
        
        
        cur.close()
        return list_of_players