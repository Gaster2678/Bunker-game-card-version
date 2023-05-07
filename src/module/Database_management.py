import sqlite3
import asyncio
from Random_carts import *

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')

class create_bd():

    async def create_bd_Players():
        cur = connect_bd.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS 
                                Players(
                                user_id INT PRIMARY KEY ,
                                play_id INT,
                                id_player INT,
                                FOREIGN KEY (play_id) REFERENCES Bunker_Cards(play_id)
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
                                Special_conditions TEXT,
                                FOREIGN KEY (user_id) REFERENCES Players (user_id)
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
                                Special_conditions INT,
                                FOREIGN KEY (user_id) REFERENCES Players (user_id)
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
    
    async def create_all():
        await create_bd.create_bd_Players()
        await create_bd.create_bd_Player_Cards()
        await create_bd.create_bd_Player_Cards_check()
        await create_bd.create_bd_Bunker_Cards()

class test_bd():
    
    def test_bd_Players(user_id, id_player):
        cur = connect_bd.cursor()
        cur.execute(f"""INSERT INTO 
                            Players(
                            user_id,
                            id_player)
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


    async def test_bd_Bunker_Cards():
        cur = connect_bd.cursor()
        cur.execute("""
                                """)
        connect_bd.commit()
        cur.close()


    async def test_bd_all():
        pass

asyncio.run(test_bd.test_bd_Player_Cards(id_player=12))