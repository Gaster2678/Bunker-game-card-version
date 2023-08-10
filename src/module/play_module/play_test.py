import asyncio
import sqlite3

from retirement_module import dead
from raund_2 import raund_2
connect_bd = sqlite3.connect(r'./src/Database/Bunker_play.db')

id_room = 15

def list_play(id_room):
        cur = connect_bd.cursor()
        cur.execute(f"""SELECT user_id,id_player
                    FROM Players
                    where play_id = {id_room}
                        """)
        
        list_of_players = cur.fetchall()
        connect_bd.commit()
        cur.close()
        return list_of_players

#asyncio.run(raund_1.start(list_player=list_play(id_room=id_room)))
asyncio.run(raund_2.start(list_of_player=list_play(id_room=id_room)))
#asyncio.run(dead.main(list_of_players=list_play(id_room=id_room)))

