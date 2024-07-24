from telethon.sync import TelegramClient, events, Button
# from telethon.tl.types import InputMessagesFilterPhotos, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import PIL.Image as Image
from solveSudoku import solveSudoku
import prettytable as pt
import os
import asyncio
import json

load_dotenv("./keys.env")

TELEGRAM_API_ID = os.environ.get('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.environ.get('TELEGRAM_API_HASH')
TELEGRAM_TOCKEN = os.environ.get('TELEGRAM_TOCKEN')

client = TelegramClient('ChatSession',TELEGRAM_API_ID,TELEGRAM_API_HASH)

# Handler For Start Command
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    FIRSTNAME = sender.first_name
    LASTNAME = sender.last_name
    SENDER = sender.id
    text = ("<b>Hello {} {} This Is Rutwik's Bot Would you like you Sudoku TO Be Solved</b>").format(FIRSTNAME,LASTNAME)

    await client.send_message(SENDER,text,parse_mode="HTML")

    markup = client.build_reply_markup([
        [Button.text('Yes')],
        [Button.text('No')]
    ])
    await client.send_message(SENDER,"Select An Option : ", buttons=markup)

# Handler for user's choice
@client.on(events.NewMessage)
async def handle_choice(event):
    sender = await event.get_sender()
    SENDER = sender.id
    if event.raw_text.lower() == 'yes':
        await client.send_message(SENDER,"Great! Please upload the image of the Sudoku puzzle.",buttons=Button.clear())
    elif event.raw_text.lower() == 'no':
        await client.send_message(SENDER,"Oh soo sorry to hear that , bye bye see you soon !!!",buttons=Button.clear())

# Handler for uploaded images
@client.on(events.NewMessage(pattern='.*', incoming=True))
async def handle_image(event):
    sender = await event.get_sender()
    SENDER = sender.id
    if event.media and hasattr(event.media, 'photo'):
        
        await event.download_media(file=os.path.join('images', 'sudoku_image.jpg'))
        await client.send_message(SENDER,"Image received! Now I'll process it.")
        
        solved_sudoku_output = await asyncio.gather(solveSudoku(os.path.join('images', 'sudoku_image.jpg')))
        solved_sudoku_output = solved_sudoku_output[0]
        solved_sudoku_output = solved_sudoku_output['solved_sudoku_output']
        solved_sudoku_output = json.loads(solved_sudoku_output)

        answer_table = pt.PrettyTable()
        answer_table.header = False
        answer_table.hrules=pt.ALL

        for row in solved_sudoku_output:
            answer_table.add_row(row)

        await client.send_message(SENDER,f'<pre>{answer_table}</pre>',parse_mode="HTML")


# To Stop The Service Once And For All
@client.on(events.NewMessage(pattern='/stop'))
async def stop(event):
    sender = await event.get_sender()
    FIRSTNAME = sender.first_name
    LASTNAME = sender.last_name
    SENDER = sender.id
    text = ("<b>Good Bye {} {} </b>").format(FIRSTNAME,LASTNAME)
    
    await client.send_message(SENDER,text,parse_mode="HTML")

    client.disconnect()

async def timeDelay(SENDER):
    await asyncio.sleep(10)
    await client.send_message(SENDER,"This is first",parse_mode="HTML")



# To Stop The Service Once And For All
@client.on(events.NewMessage(pattern='/test'))
async def test(event):
    sender = await event.get_sender()
    FIRSTNAME = sender.first_name
    LASTNAME = sender.last_name
    SENDER = sender.id
    await asyncio.gather(timeDelay(SENDER))
    text = ("<b>This is final {} {} </b>").format(FIRSTNAME,LASTNAME)
    
    await client.send_message(SENDER,text,parse_mode="HTML")

def main():
    client.start(bot_token=TELEGRAM_TOCKEN)
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
