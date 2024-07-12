from Frontend.menu import one_menu
import asyncio

async def main():
    await one_menu.menu()


asyncio.run(main())