from imports import *

class dead():

    async def main(list_of_players):
        print("Да начнется голосоввание\n и вот таблица участников")
        a = 1
        for x in list_of_players:
            print(f"{a}.<@{x[1]}>")
            a = a + 1

        print("Время на голосование 2 минуты")
        #Отправка сообшения на голосование
        time.sleep(90)
        print("Осталось 30 секунд")
        room_id = await SQL_processing.check_room(user_id=list_of_players[0][0])
        list_players_vote = await SQL_processing.check_vote(room_id=room_id)
        player_dead = await dead.logik_max_vote(list_players_vote=list_players_vote)
        nik = await SQL_processing.nik_player(player=player_dead)
        print(f"Игрок <@{nik}> был изнан из бункера со счетом: {player_dead[1]} ")
        SQL_processing.delete_player(player=player_dead)
        
    async def logik_max_vote(list_players_vote):
        temp1= 0
        temp2 = 0
        for x in list_players_vote:
            uid = x[0]
            vote = x[1]
            if temp1 > vote:
                continue
            elif temp1 < vote:
                temp1 = vote
                temp2 = uid
            else:
                print("Модуль play\nКласс dead\nфункция logik_max_voten\nстрока 274\n Были одинаковые голоса")
                continue
        list_dead = (temp2,temp1)
        return list_dead

    async def vote(id_player,room_id,number):
        
        list_players = dead.check_sql(room_id=room_id)

        if number == 1:
            await dead.new_value_vote(user_id=list_players)
            return 200
        elif number == 2:
            pass 
        elif number == 3:
            pass 
        elif number == 4:
            pass 
        elif number == 5:
            pass 
        elif number == 6:
            pass 
        elif number == 7:
            pass 
        elif number == 8:
            pass 
        elif number == 9:
            pass 
        elif number == 10:
            pass 
        elif number == 11:
            pass 
        elif number == 12:
            pass 
        elif number == 13:
            pass 
        elif number == 14:
            pass 
        elif number == 15:
            pass 
        elif number == 16:
            pass

class SQL_processing():

    async def current_value_vote(user_id):
        cur = connect_bd.cursor()

        cur.execute(f"""
            SELECT vote
            FROM Players
            where user_id = {user_id}
        """)

        vote_player = cur.fetchall()
        connect_bd.commit()
        cur.close()
        return vote_player
    
    async def new_value_vote(user_id):
        cur = connect_bd.cursor()
        cur.execute(f"""UPDATE Player_Cards_check 
                        SET vote = {(SQL_processing.current_value_vote(user_id=user_id)) + 1}
                        where user_id = {user_id}
                        """)
        connect_bd.commit()
        cur.close()
        
    async def check_vote(room_id):
        cur = connect_bd.cursor()

        cur.execute(f"""
            SELECT  user_id,vote
            FROM Players
            where id_send = {room_id}
        """)

        list_players_vote = cur.fetchall()
        connect_bd.commit()
        cur.close()
        return list_players_vote
        
    async def check_room(user_id):
        cur = connect_bd.cursor()

        cur.execute(f"""
            SELECT  id_send
            FROM Players
            where user_id = {user_id}
        """)

        room = cur.fetchall()
        connect_bd.commit()
        cur.close()
        return room
        
    async def check_sql(room_id):
        
        cur = connect_bd.cursor()

        cur.execute(f"""
            SELECT  user_id
            FROM Players
            where id_send = {room_id}
        """)

        list_players = cur.fetchall()
        connect_bd.commit()
        cur.close()
        return list_players
    
    async def nik_player(player):
        uid = player[1]
        cur = connect_bd.cursor()

        cur.execute(f"""
            SELECT id_player
            FROM Players
            where user_id = {uid}
        """)

        ping = cur.fetchall()
        connect_bd.commit()
        cur.close()
        return ping        
        
    async def delete_player(player):
        uid = player[1]
        
        cur = connect_bd.cursor()

        cur.execute(f"""
            DELETE
            FROM Players
            where user_id = {uid}
        """)
        
        cur.execute(f"""
            DELETE
            FROM Player_Cards
            where user_id = {uid}
        """)
        
        cur.execute(f"""
            DELETE
            FROM Player_Card_check
            where user_id = {uid}
        """)

        connect_bd.commit()
        cur.close()        