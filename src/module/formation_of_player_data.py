import asyncio
import sqlite3

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')
   
class data_generation():

    async def start(user_id, nick):
        await database_managment_table_player_out_checks.checks_if(user_id=user_id, nick=nick)

class database_managment_table_player_out_checks():
    
    async def request(data_player):
        cur = connect_bd.cursor()
        user_id = data_player

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
        user_id = data_player

        cur.execute(f"""
            SELECT *
            FROM Player_Cards
            where user_id = {user_id}
        """)

        data_card = cur.fetchall()
        connect_bd.commit()
        return data_card

    async def checks_if(user_id, nick):
        y = 0
        data = await database_managment_table_player_out_checks.request(data_player=user_id)
        player_card = await database_managment_table_player_out_checks.request_2(data_player=user_id)
        data_return = ["1","2","3","4","5","6","7"]
        await database_managment_table_player_out_checks.chek_proff(data=data, data_return=data_return,data_card=player_card )
        print(f"<@{nick}>. {data_return[0]}|{data_return[1]}|{data_return[2]}|{data_return[3]}|{data_return[4]}|{data_return[5]}|{data_return[6]}|")


    async def chek_proff(data, data_return, data_card):
        if data[0][1] == 0:
            data_return[0] = "???"
            await database_managment_table_player_out_checks.chek_bio(data=data, data_return=data_return,data_card=data_card )
        else:
            data_return[0] = data_card[0][1]
            await database_managment_table_player_out_checks.chek_bio(data=data, data_return=data_return,data_card=data_card )

    async def chek_bio(data, data_return, data_card):
        if data[0][2] == 0:
            data_return[1] = "???"
            await database_managment_table_player_out_checks.chek_heal(data=data, data_return=data_return,data_card=data_card )
        else:
            data_return[1] = data_card[0][2]
            await database_managment_table_player_out_checks.chek_heal(data=data, data_return=data_return,data_card=data_card )

    async def chek_heal(data, data_return, data_card):
        if data[0][3] == 0:
            data_return[2] = "???"
            await database_managment_table_player_out_checks.chek_hobby(data=data, data_return=data_return,data_card=data_card )
        else:
            data_return[2] = data_card[0][3]
            await database_managment_table_player_out_checks.chek_hobby(data=data, data_return=data_return,data_card=data_card )

    async def chek_hobby(data, data_return, data_card):
        if data[0][4] == 0:
            data_return[3] = "???"
            await database_managment_table_player_out_checks.chek_lug(data=data, data_return=data_return,data_card=data_card )
        else:
            data_return[3] = data_card[0][4]
            await database_managment_table_player_out_checks.chek_lug(data=data, data_return=data_return,data_card=data_card )


    async def chek_lug(data, data_return, data_card):
        if data[0][5] == 0:
            data_return[4] = "???"
            await database_managment_table_player_out_checks.chek_evid(data=data, data_return=data_return,data_card=data_card )
        else:
            data_return[4] = data_card[0][5]
            await database_managment_table_player_out_checks.chek_evid(data=data, data_return=data_return,data_card=data_card )

    async def chek_evid(data, data_return, data_card):
        if data[0][6] == 0:
            data_return[5] = "???"
            await database_managment_table_player_out_checks.chek_special(data=data, data_return=data_return,data_card=data_card )
        else:
            data_return[5] = data_card[0][6]
            await database_managment_table_player_out_checks.chek_special(data=data, data_return=data_return,data_card=data_card )

    async def chek_special(data, data_return, data_card):
        if data[0][7] == 0:
            data_return[6] = "???"
        else:
            data_return[6] = data_card[0][7]

#asyncio.run(database_managment_table_player_out_checks.next_value_player())
#asyncio.run(data_generation.sd(10))