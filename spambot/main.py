from config import messages
from pyrogram import Client
from rich.console import Console
from rich.progress import track
import time

console = Console()

api_id = 19010705
api_hash = "6f28ee94dfcd3a32f559c106d65bfdbe"

console.print("Author's channel: https://t.me/s0domillionacryptonft")

console.input('[bold white]press "ENTER" and the newsletter will begin')

with open('i.txt', 'r') as file:
    users = file.read().split()

delay = int(console.input('[bold red]delay> [/]'))

app = Client('account', api_id, api_hash)
app.start()

for user in track(users,
    'MSG...'):
    if 'http' in user:
        user = ''.join(user.split('/')[-1:])

    for message in messages:
        try:
            #print(user, message)#выводит юзер и сообщение юзеру
            app.send_message(user, message, parse_mode="HTML")
        
        except Exception as error:
            console.print(f'[bold red]ERROR[/]: {error}')

        time.sleep(delay)
