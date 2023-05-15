import asyncio
from formation_of_player_data import data_generation, database_managment_table_player_out_checks
import time
import sqlite3
import random

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')
list_play = ((20,9),(21,99),(22,999))

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
        await raund_2.start(list_of_player=list_of_player)
            
    async def updata_proff(user_id):
        cur = connect_bd.cursor()

        cur.execute(f"""UPDATE Player_Cards_check 
                        SET Profession = "1"
                        where user_id = {user_id}
                        """)
        
        connect_bd.commit()
        cur.close()

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
            await raund_2.vibor(check=0, user_id= x[0])
            print(f"Ход игрока <@{x[1]}>")
            time.sleep(30)
            print(f"Ход игрока {x[1]} окончен")

        await Character_Card_table.table_player(list_of_players=list)
        

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
        mass = await random_updata.check_sql(user_id=user_id)
        clock = 0
        for x in mass:
            for y in x:
                if y == 0:
                    clock = clock + 1
                else:
                    pass
        
        return_random = random.randint(1,clock)

        await raund_2.vibor(check=return_random, user_id=user_id)



asyncio.run(raund_1.start(list_player=list_play))