from telethon import Button, events
from telethon.tl.custom.message import Message
from bot import TelegramBot
from bot.config import Telegram  # Import the Telegram class
from bot.modules.static import *
from bot.modules.decorators import verify_user
from utils import check_token, check_verification, get_token

# Handler for the /start command
@TelegramBot.on(events.NewMessage(pattern=r'^/start$', incoming=True))
@verify_user(private=True)
async def welcome(event: Message):
    user_id = event.sender_id
    if not await check_verification(Telegram.db, user_id):
        data = event.text.split()[1]
        if data.split("-", 1)[0] == "verify":
            userid = data.split("-", 2)[1]
            token = data.split("-", 3)[2]
            if str(event.sender_id) != str(userid):
                return await event.reply(
                    text="<b>Invalid link or Expired link!</b>",
                    protect_content=True
                )
            is_valid = await check_token(Telegram.db, userid, token)
            if is_valid:
                await event.reply(
                    text=f"<b>Hey {event.sender.first_name}, You are successfully verified! Now you have unlimited access for all files till today midnight.</b>",
                    protect_content=True
                )
                await verify_user(Telegram.db, userid, token)
            else:
                return await event.reply(
                    text="<b>Invalid link or Expired link!</b>",
                    protect_content=True
                )

    await event.reply(
        message=WelcomeText % {'first_name': event.sender.first_name},
        buttons=[
            [
                Button.url('Add to Channel', f'https://t.me/{Telegram.BOT_USERNAME}?startchannel&admin=post_messages+edit_messages+delete_messages')
            ]
        ]
    )

# Handler for the /info command
@TelegramBot.on(events.NewMessage(pattern=r'^/info$', incoming=True))
@verify_user(private=True)
async def user_info(event: Message):
    await event.reply(UserInfoText.format(sender=event.sender))

    if not await check_verification(Telegram.db, event.sender_id) and Telegram.VERIFY:  # Access Telegram.VERIFY
        btn = [
            [
                Button.url("Verify", await get_token(Telegram.db, event.sender_id, f"https://telegram.me/{Telegram.BOT_USERNAME}?start=")),  # Access Telegram.BOT_USERNAME
                Button.url("How To Open Link & Verify", Telegram.VERIFY_TUTORIAL)  # Access Telegram.VERIFY_TUTORIAL
            ]
        ]
        await event.reply(
            text="<b>You are not verified! Kindly verify to continue!</b>",
            protect_content=True,
            buttons=btn
        )
        return

# Handler for the /log command
@TelegramBot.on(events.NewMessage(chats=Telegram.OWNER_ID, pattern=r'^/log$', incoming=True))
async def send_log(event: Message):
    await event.reply(file='event-log.txt')
