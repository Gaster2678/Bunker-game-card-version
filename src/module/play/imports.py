import asyncio
import time
import sqlite3
import random

from formation_of_player_data import data_generation, database_managment_table_player_out_checks
from Character_Card_table import Character_Card_table
from updata import updata, random_updata

connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')