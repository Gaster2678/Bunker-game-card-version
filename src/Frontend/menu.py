from Backend.Database_management import *
import asyncio

class one_menu():
    async def menu():
        await add.add_room()
        print("1 - Player")
        print("2 - Start")
        number_menu = input()
        if number_menu == "1":
            await add.add_player()
            await one_menu.menu_return()
        elif number_menu == "2":
            print("_2.1_ ")
        else:
            print("Input error")
            await one_menu.menu_return()

    async def menu_return():
        print("1 - Player")
        print("2 - Start")
        number_menu = input()
        if number_menu == "1":
            await add.add_player()
            await one_menu.menu_return()
        elif number_menu == "2":
            print("_2.1_ ")
        else:
            print("Input error")
            await one_menu.menu_return()

class add():
    async def add_room():
        id_send = int(input("id_send - "))
        id_discord_user = int(input("id_discord_user - "))
        return_add_room = (await Jobs_bd.add_play_and_room(id_send=id_send, id_discord_user=id_discord_user))
        print(f"ID room - {return_add_room[1]}")
        print(f"ID auther room - {return_add_room[0]}")

    async def add_player():
        id_send_player = int(input("id_send - "))
        id_discord_user_player = int(input("id_discord_user_player - "))
        return_add_room_play = (await Jobs_bd.add_play(id_send=id_send_player, id_discord_user=id_discord_user_player))
        print("Add player")
        print(f"ID room - {return_add_room_play[1]}")
        print(f"ID auther room - {return_add_room_play[0]}")