from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import ChatNotFound
from create_bot import bot


class CallBack(StatesGroup):
    """FSM for pollz creation"""
    group_chat_id = State()
    question1 = State()
    answers = State()



async def get_chanel_id(message: types.Message) -> None:
    await CallBack.group_chat_id.set()
    await message.reply('Чтобы провести опрос, бот должен быть добавлен в Ваш групповой чат\n'
                        'и наделен правами Администратора\n'
                        'Укажите ID вашего чата\n')

async def get_question(message: types.Message, state: FSMContext) -> None:
    """save question to FSM class CallBack.question1"""
    await CallBack.question1.set()
    await state.update_data(group_chat_id=message.text)
    await message.reply('Напишите ваш вопрос')


async def get_answers(message: types.Message, state: FSMContext) -> None:
    """save answers to FSM class CallBack. answers"""
    await CallBack.answers.set()
    await state.update_data(question1=message.text)
    await message.reply('Теперь варианты ответа через пробел')
s = -1001927673617

async def returning(message: types.Message, state: FSMContext) -> None:
    """Handles users messages and forms poll"""
    if ' ' in message.text:
        await state.update_data(answers=message.text)
        data = await state.get_data()
        answers = data['answers'].split(sep=' ')
        try:
            await bot.send_poll(data['group_chat_id'], question=data['question1'], options=answers, type='regular',
                            correct_option_id=1,
                            is_anonymous=False)
        except ChatNotFound:
            await message.answer('Введенный вами чат не найден')
        await state.finish()
    else:
        await message.reply('Похоже вы ввели варианты ответов без пробелов, вернитесь в меню')
        await state.finish()


def register_handler(disp: Dispatcher) -> None:
    """registrate handlers"""
    disp.register_message_handler(get_chanel_id, commands=['pollz'])
    disp.register_message_handler(get_question, state=CallBack.group_chat_id)
    disp.register_message_handler(get_answers, state=CallBack.question1)
    disp.register_message_handler(returning, state=CallBack.answers)
