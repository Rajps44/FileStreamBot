from telethon import Button
from telethon.events import NewMessage
from telethon.tl.custom.message import Message
from bot import TelegramBot
from bot.config import Telegram ,VERIFY, VERIFY_TUTORIAL, BOT_USERNAME
from bot.modules.static import *
from bot.modules.decorators import verify_user
from utils import verify_user, check_token , check_verification, get_token


@TelegramBot.on(NewMessage(incoming=True, pattern=r'^/start$'))
@verify_user(private=True)
async def welcome(event: NewMessage.Event | Message):
    user_id = event.sender_id
    if not await check_verification(Telegram.db, user_id):
    if data = message.command[1]
    if data.split("-", 1)[0] == "verify": # set if or elif it depend on your code
        userid = data.split("-", 2)[1]
        token = data.split("-", 3)[2]
        if str(message.from_user.id) != str(userid):
            return await message.reply_text(
                text="<b>Invalid link or Expired link !</b>",
                protect_content=True
            )
        is_valid = await check_token(client, userid, token)
        if is_valid == True:
            await message.reply_text(
                text=f"<b>Hey {message.from_user.mention}, You are successfully verified !\nNow you have unlimited access for all files till today midnight.</b>",
                protect_content=True
            )
            await verify_user(client, userid, token)
        else:
            return await message.reply_text(
                text="<b>Invalid link or Expired link !</b>",
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

@TelegramBot.on(NewMessage(incoming=True, pattern=r'^/info$'))
@verify_user(private=True)
async def user_info(event: Message):
    await event.reply(UserInfoText.format(sender=event.sender))
    if not await check_verification(client, message.from_user.id) and VERIFY == True:
        btn = [[
            InlineKeyboardButton("Verify", url=await get_token(client, message.from_user.id, f"https://telegram.me/{BOT_USERNAME}?start="))
        ],[
            InlineKeyboardButton("How To Open Link & Verify", url=VERIFY_TUTORIAL)
        ]]
        await message.reply_text(
            text="<b>You are not verified !\nKindly verify to continue !</b>",
            protect_content=True,
            reply_markup=InlineKeyboardMarkup(btn)
        )
        return

@TelegramBot.on(NewMessage(chats=Telegram.OWNER_ID, incoming=True, pattern=r'^/log$'))
async def send_log(event: NewMessage.Event | Message):
    await event.reply(file='event-log.txt')
