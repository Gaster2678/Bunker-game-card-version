import asyncio
import sqlite3

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')
   
class data_generation():

    async def sd():
        pass

class database_managment_table_player_out_checks():
    
    async def request(data_player):
        cur = connect_bd.cursor()
        user_id = data_player[0]


        cur.execute(f"""
            SELECT *
            FROM Player_Cards_check
            where user_id = {user_id}
        """)

        data_checks = cur.fetchall()

        connect_bd.commit()

        return data_checks
    
    async def request_2(data_player):
        cur = connect_bd.cursor()
        user_id = data_player[0]


        cur.execute(f"""
            SELECT *
            FROM Player_Cards
            where user_id = {user_id}
        """)

        data_checks = cur.fetchall()

        connect_bd.commit()

        return data_checks
    
    async def checks_if(data_player):
        
        data = await database_managment_table_player_out_checks.request(data_player=data_player)
        data_name = await database_managment_table_player_out_checks.request_2(data_player=data_player)
        data_return = ["1","2","3","4","5","6","7"]

        await database_managment_table_player_out_checks.chek_proff(data=data, data_return= data_return, data_retyrn_2=data_name)
        

    async def chek_proff(data, data_return, data_retyrn_2):
        if data[0] == 0:
            database_managment_table_player_out_checks.chek_bio()
        else:
            data_return[0].replase("1", f"{data_retyrn_2[0]}")
            database_managment_table_player_out_checks.chek_bio()

    async def chek_bio(data, data_return, data_retyrn_2):
        pass

    async def chek_heal(data, data_return):
        pass

    async def chek_lug(data, data_return):
        pass

    async def chek_evid(data, data_return):
        pass

    async def chek_special(data, data_return):
        pass
