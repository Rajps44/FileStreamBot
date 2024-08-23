import datetime
from telethon import Button
from telethon.events import NewMessage
from telethon.tl.custom.message import Message
from bot import TelegramBot
from bot.config import Telegram
from bot.modules.static import *
from bot.modules.decorators import verify_user

@TelegramBot.on(NewMessage(incoming=True, pattern=r'^/start$'))
@verify_user(private=True)
async def welcome(event: NewMessage.Event | Message):
    user_id = event.sender_id
    user_data = Telegram.users_collection.find_one({"user_id": user_id})

    # Agar user ka record pehle se hai, to 24 hours check karein
    if user_data:
        last_interaction = user_data['first_interaction']
        current_time = datetime.datetime.now()
        time_difference = current_time - last_interaction

        # 24 hours (86400 seconds) se zyada ka difference check karte hain
        if time_difference.total_seconds() > 86400:
            await event.reply("Aapka 24-hour verification period khatam ho chuka hai. Kripya phir se start kariye.")
            return
    else:
        # Agar user ka record nahi hai, to abhi ka time store karein
        Telegram.users_collection.insert_one({
            "user_id": user_id,
            "first_interaction": datetime.datetime.now()
        })

    # Agar user authorized hai, to welcome message bheja jaye
    await event.reply(
        message=WelcomeText % {'first_name': event.sender.first_name},
        buttons=[
            [
                Button.url('Add to Channel', f'https://t.me/{Telegram.BOT_USERNAME}?startchannel&admin=post_messages+edit_messages+delete_messages')
            ]
        ]
    )

@TelegramBot.on(NewMessage(incoming=True, pattern=r'^/info$'))
@verify_user(private=True)
async def user_info(event: Message):
    await event.reply(UserInfoText.format(sender=event.sender))

@TelegramBot.on(NewMessage(chats=Telegram.OWNER_ID, incoming=True, pattern=r'^/log$'))
async def send_log(event: NewMessage.Event | Message):
    await event.reply(file='event-log.txt')
