import asyncio
import random
import sqlite3
import raund_2
from utils.formation_of_player_data import *

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')

class updata():

    async def updata_sql(user_id, updata):
        cur = connect_bd.cursor()

        cur.execute(f"""UPDATE Player_Cards_check 
                        SET {updata} = "1"
                        where user_id = {user_id}
                        """)
        
        connect_bd.commit()
        cur.close()

class random_updata():

    async def check_sql(user_id):
        cur = connect_bd.cursor()

        cur.execute(f"""
            SELECT *
            FROM Player_Cards_check
            where user_id = {user_id}
        """)

        data_card = cur.fetchall()
        connect_bd.commit()
        cur.close()
        return data_card
    
    async def logik(user_id):
        z = 0
        ethalon = 2
        mass = await random_updata.check_sql(user_id=user_id)
        clock = 0
        for x in mass:
            for y in x:
                if y == 0:
                    clock = clock + 1
                elif y == 1:
                    z = z + 1
                else:
                    pass
        
        if z == ethalon:
            return 200
        else:            
            return_random = random.randint(1,clock)
            await raund_2.raund_2.vibor(check=return_random, user_id=user_id)

    async def logik_2(user_id,ethalon):
        z = 0
        mass = await random_updata.check_sql(user_id=user_id)
        clock = 0
        for x in mass:
            for y in x:
                if y == 0:
                    clock = clock + 1
                elif y == 1:
                    z = z + 1
                else:
                    pass
        
        if z == ethalon:
            return 200
        else:            
            return 404