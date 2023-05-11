import asyncio
import sqlite3

from menu import *

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')

class checks():
    
    async def check_quantity_players(id_send):         
        cur = connect_bd.cursor()
        
        cur.execute(f"""SELECT play_id 
                        FROM Players 
                        where id_send = {id_send}
                        """)
        
        play_id = cur.fetchall()
        connect_bd.commit()
        
        cur.execute(f"""SELECT user_id 
                        FROM Players 
                        where play_id = {play_id[0][0]}
                        """)
        
        user_id = cur.fetchall()
        massiv_user_id = []
        y = 0
        
        for x in user_id:
            print(x[0])
            value = x[0]
            massiv_user_id.append(x[0])
            y = y + 1

        if ((y >= 4 ) and (y <= 16)):
            await starting_the_game.Confirmation()
        elif y < 4:
            await starting_the_game.few_players()
            await one_menu.menu_return()
        else:
            await starting_the_game.a_lot_of_players()
            await one_menu.menu_return()

        cur.close()

class starting_the_game():

    async def Confirmation():
        print("Are you sure?")
        print("1 - Yes")
        print("2 - No")
        x = int(input())
        if x == 2:
            return 0
        elif x == 1:
            return 1            
        else:
            print("Error input")

    async def the_beginning_of_the_game(id_send):
        x = (await starting_the_game.Confirmation())
        cur = connect_bd.cursor()

        if x == 0:
            await one_menu.menu_return()
        else:
            cur.execute(f"""SELECT play_id 
                        FROM Players 
                        where id_send = {id_send}
                        """)
        
            play_id = cur.fetchall()
            connect_bd.commit()

            cur.execute(f"""SELECT user_id, id_player
                        FROM Players 
                        where play_id = {play_id[0][0]} 
                        """)
            
            list_of_players = cur.fetchall()
            connect_bd.commit()
            cur.close()
            await starting_the_game.The_second_stage_of_the_start(list_of_players=list_of_players)


    async def few_players():
        print("few players")

    async def a_lot_of_players():
        print("A lot of players")

    async def The_second_stage_of_the_start(list_of_players):
        c = 0
        print("List of players")
        print("[№ player].[ont id]|[name player] ")
        for b in list_of_players:
            print(f"{c + 1}. {list_of_players[c][0]}|<@{list_of_players[c][1]}>")
            c = c + 1   

            
#asyncio.run(checks.check_quantity_players(id_send=2, id_discord_auther_room= 1))
asyncio.run(starting_the_game.the_beginning_of_the_game(9))