#║██       ╔═███   ╔██         ██ ╔█████
#║██      ╔╝██ ██  ╚╗██       ██  ║█ 
#║██      ║██    ██ ╚╗██      ██  ║█████
#║██      ║██   ██   ╚╗██    ██   ║█
#║██████╗╚╗██ ██     ╚╗██ ██     ║█████╗
#╚══════╝ ╚═███        ╚═██       ╚═════╝
# © Gydro4ka & mertv_ya_naxyi 2024-2025
# this file - unofficial module for Hikka Userbot
#  /\_/\   This module was loaded through https://t.me/hikka_gmod
# ( o.o )   Licensed under the GNU AGPLv3.
#  > ^ <  
# ------------------------------------------------
# Name: EVOeksp
# meta developer: @Gydro4ka & @mertv_ya_naxyi
# Description: авто-экспедиции в игровом боте @mine_evo_bot
# Commands: .eksp | .noeksp
# Thanks: me
# ------------------------------------------------
# Licensed under the GNU AGPLv3
# https://www.gnu.org/licenses/agpl-3.0.html
# channel: https://t.me/hikka_gmod
from .. import loader, utils
from asyncio import sleep

@loader.tds
class EVOeksp(loader.Module):
    strings = {'name': 'EVOeksp'}

    async def client_ready(self, client, db):
        self.client = client
        self.running = False 

    @loader.command()
    async def eksp(self, message):
        if self.running:
            await message.edit('<b>Экспедициии уже активны </b>')
            return
        self.running = True
        await message.edit('<b>Экспедиции запущены</b>')
        await self.start_expedition_collection()

    @loader.command()
    async def noeksp(self, message):
        if not self.running:
            await message.edit('<b>Экспедиции не запущены</b>')
            return
        self.running = False
        await message.edit('<b>Экспедиции остановлены</b>')

    async def start_expedition_collection(self):
        while self.running:
            await self.send_expedition_request()
            await sleep(300)

    async def send_expedition_request(self):
        response = await self.client.send_message('@mine_evo_bot', 'эксп')
        await self.handle_response(response)

    async def handle_response(self, message):
        if "Текущая" in message.text:
            return
        elif "завершена" in message.text:
            await sleep(5)
            await self.click_button(message)
            return

    async def click_button(self, message):
        r = await self.client.get_reply(message)
        if r and hasattr(r, 'buttons') and r.buttons:
            await r.click(0)
            
