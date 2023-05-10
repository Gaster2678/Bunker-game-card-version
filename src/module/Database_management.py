import sqlite3
import asyncio

from Random_carts import *

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')

class create_bd():

    async def create_bd_Players():
        cur = connect_bd.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS 
                                Players(
                                user_id INT ,
                                play_id INT,
                                id_player INT,
                                id_send INT
                                );
                                """)
        connect_bd.commit()
        cur.close()

    async def create_bd_Player_Cards():
        cur = connect_bd.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS 
                                Player_Cards(
                                user_id INT,
                                Profession TEXT,
                                Biology TEXT,
                                Health TEXT,
                                Hobby TEXT,
                                Luggage TEXT,
                                Evidense TEXT,
                                Special_conditions TEXT
                                );
                                """)
        connect_bd.commit()
        cur.close() 

    async def create_bd_Player_Cards_check():
        cur = connect_bd.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS 
                                Player_Cards_check(
                                user_id INT ,
                                Profession INT,
                                Biology INT,
                                Health INT,
                                Hobby INT,
                                Luggage INT,
                                Evidense INT,
                                Special_conditions INT
                                );
                                """)
        connect_bd.commit()
        cur.close() 
        
    async def create_bd_Bunker_Cards():
        cur = connect_bd.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS 
                                Bunker_Cards(
                                play_id INT PRIMARY KEY ,
                                Disasters TEXT,
                                danger TEXT,
                                bunker_cards_1 TEXT,
                                bunker_cards_2 TEXT,
                                bunker_cards_3 TEXT,
                                bunker_cards_4 TEXT,
                                bunker_cards_5 TEXT,
                                bunker_cards_6 TEXT,
                                bunker_cards_7 TEXT
                                );
                                """)
        connect_bd.commit()
        cur.close()    
    
    async def create_bd_Last_value():
        cur = connect_bd.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS 
                                Last_value(
                                last_user_id INT ,
                                last_play_room_id INT
                                );
                                """)
        connect_bd.commit()
        cur.close()

    async def create_all():
        await create_bd.create_bd_Players()
        await create_bd.create_bd_Player_Cards()
        await create_bd.create_bd_Player_Cards_check()
        await create_bd.create_bd_Bunker_Cards()
        await create_bd.create_bd_Last_value()

class test_bd():
    
    async def test_bd_Players(user_id, id_player):
        cur = connect_bd.cursor()
        cur.execute(f"""INSERT INTO 
                            Players(
                            user_id,
                            play_id,
                            id_player,
                            id_send)
                            VALUES('{user_id}','{id_player}')
                                """)
        connect_bd.commit()
        cur.close()

    async def test_bd_Player_Cards(id_player):
        cur = connect_bd.cursor()
        cur.execute(f"""SELECT * FROM Players where id_player = {id_player}""")
        bd = tuple(list(set(cur.fetchall())))
        Results_random = bunker_karti.stol_play()

        cur.execute(f"""INSERT INTO Player_Cards(
                                user_id , Profession , Biology,
                                Health , Hobby , Luggage,
                                Evidense , Special_conditions)
                                VALUES('{bd[0][0]}','{Results_random[0]}','{Results_random[1]}',
                                '{Results_random[2]}','{Results_random[3]}','{Results_random[4]}',
                                '{Results_random[5]}','{Results_random[6]}');
                             """)
        connect_bd.commit()
        cur.close()

    async def test_bd_Player_Cards_check(id_player):
        cur = connect_bd.cursor()
        cur.execute(f"""SELECT * FROM Players where id_player = {id_player}""")
        bd = tuple(list(set(cur.fetchall())))
        Results_random = (0,0,0,0,0,0,0)

        cur.execute(f"""INSERT INTO Player_Cards_check(
                                user_id , Profession , Biology,
                                Health , Hobby , Luggage,
                                Evidense , Special_conditions)
                                VALUES('{bd[0][0]}','{Results_random[0]}','{Results_random[1]}',
                                '{Results_random[2]}','{Results_random[3]}','{Results_random[4]}',
                                '{Results_random[5]}','{Results_random[6]}');
                             """)
        connect_bd.commit()
        cur.close()

    async def test_bd_Bunker_Cards(play_id):
        cur = connect_bd.cursor()
        result = Sobitia.Generating_results_for_the_database()
        cur.execute(f"""INSERT INTO Bunker_Cards(
                                play_id,
                                Disasters,
                                danger,
                                bunker_cards_1,
                                bunker_cards_2,
                                bunker_cards_3,
                                bunker_cards_4,
                                bunker_cards_5,
                                bunker_cards_6,
                                bunker_cards_7)
                                VALUES('{play_id}','{result[0]}','{result[1]}',
                                '{result[2]}','{result[3]}','{result[4]}',
                                '{result[5]}','{result[6]}','{result[7]}',
                                '{result[8]}');
                                """)
        connect_bd.commit()
        cur.close()

    async def test_bd_Last_value(last_user_id,last_play_room_id):
        cur = connect_bd.cursor()
        cur.execute(f"""INSERT INTO 
                            Last_value(
                            last_user_id,
                            last_play_room_id
                            )
                            VALUES('{last_user_id}','{last_play_room_id}')
                                """)
        connect_bd.commit()
        cur.close()

    async def test_bd_all(user_id_out, id_player_out, play_id_out,last_play_room_id,last_user_id):
        play_id = play_id_out
        user_id = user_id_out
        id_player = id_player_out
        await test_bd.test_bd_Players(user_id=user_id,id_player=id_player)
        await test_bd.test_bd_Player_Cards(id_player=id_player)
        await test_bd.test_bd_Player_Cards_check(id_player=id_player)
        await test_bd.test_bd_Bunker_Cards(play_id=play_id)
        await test_bd.test_bd_Last_value(last_play_room_id=last_play_room_id,last_user_id=last_user_id)

class Jobs_bd():

    async def add_play_and_room(id_send,id_discord_user):
        cur = connect_bd.cursor()
        last_value_player = await dev_jobs_bd.last_value_player()
        last_value_room = await dev_jobs_bd.last_value_room()
        Results_random = bunker_karti.stol_play()
        Null_chec = (0,0,0,0,0,0,0)
        result = Sobitia.Generating_results_for_the_database()
        return_id = (last_value_player,last_value_room)
        cur.execute(f"""INSERT INTO 
                            Players(
                                user_id,
                                play_id,
                                id_player,
                                id_send)
                            VALUES(
                                '{last_value_player}',
                                '{last_value_room}',
                                '{id_discord_user}',
                                '{id_send}')
                                """)
        connect_bd.commit()

        cur.execute(f"""INSERT INTO 
                                Player_Cards(
                                    user_id, 
                                    Profession, 
                                    Biology,
                                    Health, 
                                    Hobby, 
                                    Luggage,
                                    Evidense, 
                                    Special_conditions)
                                VALUES(
                                    '{last_value_player}',
                                    '{Results_random[0]}',
                                    '{Results_random[1]}',
                                    '{Results_random[2]}',
                                    '{Results_random[3]}',
                                    '{Results_random[4]}',
                                    '{Results_random[5]}',
                                    '{Results_random[6]}');
                             """)
        connect_bd.commit()

        cur.execute(f"""INSERT INTO 
                                Player_Cards_check(
                                    user_id,
                                    Profession, 
                                    Biology,
                                    Health, 
                                    Hobby, 
                                    Luggage,
                                    Evidense, 
                                    Special_conditions)
                                VALUES(
                                    '{last_value_player}',
                                    '{Null_chec[0]}',
                                    '{Null_chec[1]}',
                                    '{Null_chec[2]}',
                                    '{Null_chec[3]}',
                                    '{Null_chec[4]}',
                                    '{Null_chec[5]}',
                                    '{Null_chec[6]}');
                             """)
        connect_bd.commit()

        cur.execute(f"""INSERT INTO 
                                Bunker_Cards(
                                    play_id,
                                    Disasters,
                                    danger,
                                    bunker_cards_1,
                                    bunker_cards_2,
                                    bunker_cards_3,
                                    bunker_cards_4,
                                    bunker_cards_5,
                                    bunker_cards_6,
                                    bunker_cards_7)
                                VALUES(
                                    '{last_value_room}',
                                    '{result[0]}',
                                    '{result[1]}',
                                    '{result[2]}',
                                    '{result[3]}',
                                    '{result[4]}',
                                    '{result[5]}',
                                    '{result[6]}',
                                    '{result[7]}',
                                    '{result[8]}');
                                """)
        connect_bd.commit()

        cur.close()      

        await dev_jobs_bd.next_value_player()
        await dev_jobs_bd.next_value_room()
        
        return return_id
        
    async def add_play(id_send,id_discord_user): 
        cur = connect_bd.cursor()
        last_value_player = await dev_jobs_bd.last_value_player()
        Results_random = bunker_karti.stol_play()
        Null_chec = (0,0,0,0,0,0,0)
        result = Sobitia.Generating_results_for_the_database()
        
        cur.execute(f"""SELECT play_id 
                        FROM Players 
                        where id_send = {id_send}""")
        connect_bd.commit()

        bd = cur.fetchall()
        id_room = bd[0][0]

        cur.execute(f"""INSERT INTO 
                            Players(
                                user_id,
                                play_id,
                                id_player,
                                id_send)
                            VALUES(
                                '{last_value_player}',
                                '{id_room}',
                                '{id_discord_user}',
                                '{id_send}')
                                """)
        connect_bd.commit()

        cur.execute(f"""INSERT INTO 
                                Player_Cards(
                                    user_id, 
                                    Profession, 
                                    Biology,
                                    Health, 
                                    Hobby, 
                                    Luggage,
                                    Evidense, 
                                    Special_conditions)
                                VALUES(
                                    '{last_value_player}',
                                    '{Results_random[0]}',
                                    '{Results_random[1]}',
                                    '{Results_random[2]}',
                                    '{Results_random[3]}',
                                    '{Results_random[4]}',
                                    '{Results_random[5]}',
                                    '{Results_random[6]}');
                             """)
        connect_bd.commit()

        cur.execute(f"""INSERT INTO 
                                Player_Cards_check(
                                    user_id,
                                    Profession, 
                                    Biology,
                                    Health, 
                                    Hobby, 
                                    Luggage,
                                    Evidense, 
                                    Special_conditions)
                                VALUES(
                                    '{last_value_player}',
                                    '{Null_chec[0]}',
                                    '{Null_chec[1]}',
                                    '{Null_chec[2]}',
                                    '{Null_chec[3]}',
                                    '{Null_chec[4]}',
                                    '{Null_chec[5]}',
                                    '{Null_chec[6]}');
                             """)
        connect_bd.commit()

        cur.close()      
        return_id = (last_value_player, id_room)
        await dev_jobs_bd.next_value_player()

        return return_id
        
class dev_jobs_bd():

    async def last_value_player():
        cur = connect_bd.cursor()
        cur.execute(f"""SELECT last_user_id FROM Last_value""")
        bd = tuple(list(set(cur.fetchall())))
        connect_bd.commit()
        cur.close()
        return bd[0][0]

    async def last_value_room():
        cur = connect_bd.cursor()
        cur.execute(f"""SELECT last_play_room_id FROM Last_value""")
        bd = tuple(list(set(cur.fetchall())))
        connect_bd.commit()
        cur.close()
        return bd[0][0]

    async def next_value_player():
        
        cur = connect_bd.cursor()
        last = await dev_jobs_bd.last_value_player()
        next = last + 1
        cur.execute(f"""UPDATE Last_value SET last_user_id = {next}""")
        connect_bd.commit()
        cur.close()
        
    async def next_value_room():

        cur = connect_bd.cursor()
        last = await dev_jobs_bd.last_value_room()
        next = last + 1
        cur.execute(f"""UPDATE Last_value SET last_play_room_id = {next}""")
        connect_bd.commit()
        cur.close()
        
#print(f"{asyncio.run(dev_jobs_bd.last_value_player())}")
#print(f"{asyncio.run(dev_jobs_bd.last_value_room())}")
#print(f"{asyncio.run(dev_jobs_bd.next_value_player())}")
#print(f"{asyncio.run(dev_jobs_bd.next_value_room())}")
#asyncio.run(Jobs_bd.add_play_and_room(id_send=3, id_discord_user=1000001))
#asyncio.run(create_bd.create_all())
#asyncio.run(test_bd.test_bd_Last_value(last_play_room_id= 10, last_user_id=10))
#asyncio.run(Jobs_bd.add_play(id_send= 2,id_discord_user=1400212))