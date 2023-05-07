import sqlite3
import asyncio


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

asyncio.run(create_bd.create_all())