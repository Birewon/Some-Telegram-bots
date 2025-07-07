from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile

import app.keyboards as kb

router = Router() # create the copy of Dispatcher


@router.message(CommandStart()) # handler: only /start
async def start_handler(message: Message):
    await message.answer('Hello! You called the /start command.\nInfo about message ⏬')
    await message.answer(message.model_dump_json(indent=4, exclude_none=True))

@router.message(Command('help')) # handler: accepts the /help command
async def help_handler(message: Message):
    await message.answer('You called the /help command.\n'
    'You can send any command to me and I will tell you abot it command 😌')

@router.message(Command('aboutme'))
async def about_user(message: Message):
    await message.answer(f'And also I can send you the information about you:\nID: {message.from_user.id}\nName: {message.from_user.full_name}')
    await message.answer('This message and the one above were sent using the "answer" method, but I can also send you a message using the "reply" method. See below')
    await message.reply('How can you notice, I sent this message via "reply" method')

@router.message(Command('keyboard'))
async def keyboard_demonstration(message: Message):
    await message.answer('OK! I will show you how the "ReplyKeyBoard" works:\n'
    'For example, we are have any buttons. 👇'
    'These buttons calls "REPLY" and they can contain links or some objects.\n\n'
    'How is it created? Look: ⬇️',
    reply_markup=kb.main)

    reply_buttons = FSInputFile('GuideBot/app/photo/buttons_code.png', filename='example_buttons')
    await message.answer_photo(photo=reply_buttons, caption='🤖 This is what the creation of buttons look like')




@router.message(F.text == 'How are you?')
async def how_are_you_handler(message: Message):
    await message.answer('I`m OK! You asked me about my business')

@router.message(F.photo) # handler: accepts a photo and resend it back
async def photo_handler(message: Message):
    await message.answer(f'You sent me a photo! Info about photo:\nID: {message.photo[-1].file_id}')
    await message.answer_photo(photo=message.photo[0].file_id, caption='And also I can resend you your photo. It`s your photo!') # Resend the photo
    await message.answer_photo(photo='https://i.siteapi.org/tD-6qGutsoJDMynfTbcshxvquN8=/fit-in/660x0/top/filters:format(webp):no_upscale()/s2.siteapi.org/0024b9c2210848f/img/q89wja3s2rk00wg8s8g000kkkswsk0', caption='This photo has been sent via URL')

@router.message(F.voice)
async def voice_handler(message: Message):
    await message.answer('Ok! You sent me a voice message!\nMy backend can handle a voice message using this code:')

    reply_voice = FSInputFile('GuideBot/app/photo/voice_code.png', filename='example_voice')
    await message.answer_photo(photo=reply_voice, caption='🤖 This code can catch your voice messages and respond to them')


@router.message()
async def any_message(message: Message):
    print(message.model_dump_json(indent=4))
    await message.answer('You sent some message')