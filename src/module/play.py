import asyncio
from formation_of_player_data import data_generation, database_managment_table_player_out_checks
import time
import sqlite3
import random

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')
list_play = ((23,9),(24,99),(25,999))

class raund_1():

    check_player_clock = 0

    async def start(list_player):
        await raund_1.time_10_sec(list_player=list_player)

    async def time_10_sec(list_player):
        sec = (10,9,8,7,6,5,4,3,2,1)

        for x in sec:
            print(f"{x}")
            time.sleep(1)

        await Character_Card_table.table_player(list_of_players=list_player)

        for y in list_player:
            await raund_1.send_secret(list_player=y)

        print("Раунд начался")

        await raund_1.Whose_move(list_of_player=list_player)
        
    async def send_secret(list_player):
        await Character_Card_table.heading()
        data_return = await database_managment_table_player_out_checks.request_2(data_player=list_player[0])
        print(f"<@{list_player[1]}>. {data_return[0][1]}|{data_return[0][2]}|{data_return[0][3]}|{data_return[0][4]}|{data_return[0][5]}|{data_return[0][6]}|{data_return[0][7]}|")

    async def send_secret_raund():
        print("Ваш ход начнется через 10 секунд [Первой картой открывается профессия]")

    async def time_10_sec_player():
        pass

    async def Whose_move(list_of_player):
        for player in list_of_player:
            user_id = player[0]
            ping_nick = player[1]
            await raund_1.send_secret_raund()
            print(f"Ход игрока <@{ping_nick}> через 10 секунд")
            time.sleep(10)
            print(f"Ход игрока {ping_nick} начался у тебя 30 секунд")
            await raund_1.updata_proff(user_id=user_id)
            time.sleep(20)
            print("Осталось 10 секунд")

            sec = (5,4,3,2,1)

            for x in sec:
                time.sleep(1)
                print(x)
            print(f"Ход игрока <@{ping_nick}> окончен")
        
        await Character_Card_table.table_player(list_of_players=list_of_player)
        await raund_2.time_60_sek(list=list_of_player)
            
    async def updata_proff(user_id):
        cur = connect_bd.cursor()

        cur.execute(f"""UPDATE Player_Cards_check 
                        SET Profession = "1"
                        where user_id = {user_id}
                        """)
        
        connect_bd.commit()
        cur.close()

class raund_2():
    
    async def time_60_sek(list):
        print("Второй раунд начнется через минуту")
        time.sleep(30)
        print("30 cek")
        print("Типо модуль")#модуль выдачи вариантов карт <--- 
        time.sleep(25)
        print("5 cek")

        sec = (5,4,3,2,1)

        for x in sec:
            print(x)
            time.sleep(1)

        print("2-ой раунд начинается")

        await raund_2.sec_sek(list=list)

    async def sec_sek(list):
    
        for x in list:
            print(f"Ход игрока <@{x[1]}> начнется через 10 секунд")
            time.sleep(10)
            await random.vibor(user_id=x[0], check=0)
            print(f"Ход игрока <@{x[1]}>")
            time.sleep(30)
            print(f"Ход игрока <@{x[1]}> окончен")

        print("none")
        await Character_Card_table.table_player(list_of_players=list_play)
    
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

class random():


    async def sql_zapros(user_id):
        mass_check_one = 0
        ethalon = 2
        cur = connect_bd.cursor()

        cur.execute(f"""SELECT *
                        FROM Player_Cards_check
                        where user_id = {user_id}
                        """)
        
        list_check_player = cur.fetchall()
        cur.close()

        for x in list_check_player:
            if x == 1:
                mass_check_one = mass_check_one + 1
            else:
                pass

        return mass_check_one
    
    async def random(user_id):
        random_return =await random.random(0, await random.sql_zapros(user_id=user_id))
        await random.vibor(user_id=user_id, check= random_return)

    async def vibor(user_id, check):

        mass_updata = ("Biology","Health","Hobby","Luggage","Evidense","Special_conditions")

        if check == 1:
            await random.sql_updata(user_id=user_id, updata=mass_updata[0])
        elif check == 2:
            await random.sql_updata(user_id=user_id, updata=mass_updata[1])
        elif check == 3:
            await random.sql_updata(user_id=user_id, updata=mass_updata[2])
        elif check == 4:
            await random.sql_updata(user_id=user_id, updata=mass_updata[3])
        elif check == 5:
            await random.sql_updata(user_id=user_id, updata=mass_updata[4])
        elif check == 6:
            await random.sql_updata(user_id=user_id, updata=mass_updata[5])
        else:
            await random.random(user_id=user_id)

    async def sql_updata(user_id, updata):
        cur = connect_bd.cursor()

        cur.execute(f"""UPDATE Player_Cards_check 
                        SET {updata} = "1"
                        where user_id = {user_id}
                        """)
        
        connect_bd.commit()
        cur.close()

asyncio.run(raund_2.time_60_sek(list=list_play))