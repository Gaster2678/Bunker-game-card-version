import random
import sqlite3
import time
import asyncio




def menu():
    print("1 - Player")
    print("2 - Start")
    number_menu = input()
    if number_menu == "1":
        print("_2_ ")
    elif number_menu == "2":
        print("_2.1_ ")
    else:
        print("Input error")
        menu()
        
def main():
    print("_1_ ")
    menu()

main()