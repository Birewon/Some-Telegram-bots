from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from random import randint
router = Router()

ATTEMPTS = 5
data = {'in_game': False,
        'picked_num': None,
        'attempts': None,
        'total_games': 0,
        'wins': 0}

def get_random_number() -> int:
    return randint(1, 100)


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer('Hi! Let\'s play the game!\nRules: I\'m guessing a number from 1 to 100 and you have to guess it. To start the game, enter the command /game or /play.')

@router.message(Command('help'))
async def help_handler(message: Message):
    await message.answer(f'This bot picks a random number from 1 to 100. You have {ATTEMPTS} attempts to guess the selected number. If you ready to start the game, send /game or /play.\nIf you want to leave from the game you have to send /cancel.')

@router.message(Command('stats'))
async def stat_handler(message: Message):
    await message.answer(
        f'Your stats:\n'
        f'Wins - {data['wins']}\n'
        f'Total games - {data['total_games']}'
    )

@router.message(Command('cancel'))
async def leave_game(message: Message):
    if data['in_game']:
        data['in_game'] = False
        await message.answer(
            'The game has been cancelled.\n'
            'You may to start the new game!'
        )
    else:
        await message.answer(
            'You tried to stop the game,\n'
            'but you didnt start the game.\n'
            'If you want to start, press: /game or /play'
        )

@router.message(Command('game', 'play'))
async def start_game(message: Message):
    if data['in_game']:
        await message.answer(
            'You already have an active game!\n'
            'I can react only to /cancel and any number from 1 to 100'
        )
    else:
        data['in_game'] = True
        data['picked_num'] = get_random_number()
        data['attempts'] = ATTEMPTS
        await message.answer(
            'Nice! I picked a number from 1 to 100.\n'
            'Try to guess it!'
        )

@router.message(lambda x: x.text and x.text.isdigit() and 1 <= int(x.text) <= 100)
async def try_to_guess(message: Message):
    if data['in_game']:
        if data['picked_num'] == int(message.text):
            data['in_game'] = False
            data['total_games'] += 1
            data['wins'] += 1
            await message.answer('Wow! You picked a right number! You win!')
        elif data['picked_num'] > int(message.text):
            data['attempts'] -= 1
            await message.answer(
                'Oh no... The number I picked is bigger than your number\n'
                f'Remaining attempts: {data['attempts']}'
            )
        else:
            data['attempts'] -= 1
            await message.answer(
                'Oh no... The number I picked is lower than your number\n'
                f'Remaining attempts: {data['attempts']}'
            )
        if data['attempts'] == 0:
            data['in_game'] = False
            data['total_games'] += 1
            await message.answer(
                'Ha-ha! I won!\n'
                f'The number I picked is {data["picked_num"]}'
            )
    else:
        await message.answer('You didn\'t start the game!')


@router.message()
async def another_message(message: Message):
    await message.answer('Sorry! I did\'t understand')
