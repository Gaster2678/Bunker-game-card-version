import asyncio
import time
import sqlite3
import random
import os,sys
sys.path.append('..')
from utils.formation_of_player_data import *
connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')

class Character_Card_table():
    """
    
    """   
    async def heading():
        print("Nikname|Profession|Biology|Health|Hobby|Luggage|Evidense|Special_conditions")
        print("---------------------------------------------------------------------------")

    async def table_player(list_of_players):
        await Character_Card_table.heading()

        #Отредактироввать с счетчиком
        for player in list_of_players:
            user_id = player[0]
            ping_nick = player[1]
            
            await data_generation.start(user_id=user_id,nick= ping_nick)
            
