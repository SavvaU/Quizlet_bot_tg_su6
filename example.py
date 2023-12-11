import random

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy import create_engine, select, ForeignKey
from sqlalchemy.orm import Session, mapped_column, Mapped, DeclarativeBase

# db.py
db_url = 'sqlite:///db.sqlite3'
engine = create_engine(db_url, echo=True)


# models.py
class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = 'question'

    question_id: Mapped[int] = mapped_column(primary_key=True)
    question_text: Mapped[str] = mapped_column()


class Answer(Base):
    __tablename__ = 'answer'

    answer_id: Mapped[int] = mapped_column(primary_key=True)
    answer_text: Mapped[str] = mapped_column()
    is_correct: Mapped[bool] = mapped_column()
    question_id: Mapped[int] = mapped_column(ForeignKey('question.id', ondelete='CASCADE'))


# db.py

def get_choices(question_id: int):
    """Return four choices for question"""
    with Session(engine, autocommit=False, autoflush=True, expire_on_commit=False) as session:
        question = session.execute(
            select(Question).where(Question.question_id == question_id)).scalar()
        if not question:
            return None
        choices = session.execute(
            select(Answer).where(Answer.question_id == question.question_id)).scalars().all()
        return choices


# callback_data.py
class ChoiceCallbackData(CallbackData):
    is_correct: bool
    question_id: int


# kb.py
def get_inline_keyboard(buttons: list[tuple], adjust: tuple = (1,)):
    builder = InlineKeyboardBuilder()
    for text, callback in buttons:
        builder.button(text=text, callback_data=callback)
    builder.adjust(*adjust)
    return builder.as_markup()




@router.callback_query(ChoiceState, ChoiceCallbackData.filter(F.is_correct == True))
async def true_answer(query: CallbackQuery, callback_data: ChoiceCallbackData, state: FSMContext,
                      bot: Bot):
    bot.send_message(chat_id=query.from_user.id, text="Ты ответил верно!")
    # TODO: Логика добавления баллов
    # TODO: Переписать под себя логику вытаскивания вопроса
    question_id = random.randint(0, 100)
    choices = get_choices(question_id=question_id)
    choices_buttons = [(choice.answer_text, ChoiceCallbackData(is_correct=choice.is_correct,
                                                               question_id=choice.question_id)) for
                       choice in choices]
    bot.send_message(chat_id=query.from_user.id, text="Следующий вопрос:",
                     reply_markup=get_inline_keyboard(buttons=choices_buttons))

@router.callback_query(ChoiceState, ChoiceCallbackData.filter(F.is_correct == False))
async def true_answer(query: CallbackQuery, callback_data: ChoiceCallbackData, state: FSMContext,
                      bot: Bot):
    bot.send_message(chat_id=query.from_user.id, text="Ты ответил неверно, но ещё есть вопросы!")
    # TODO: Переписать под себя логику вытаскивания вопроса
    question_id = random.randint(0, 100)
    choices = get_choices(question_id=question_id)
    choices_buttons = [(choice.answer_text, ChoiceCallbackData(is_correct=choice.is_correct,
                                                               question_id=choice.question_id)) for
                       choice in choices]
    bot.send_message(chat_id=query.from_user.id, text="Следующий вопрос:",
                     reply_markup=get_inline_keyboard(buttons=choices_buttons))
