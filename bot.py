from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler

from util import load_message, send_photo, send_text, show_main_menu, load_prompt, Dialog
from ds import DeepSeekHandler
from settings import BOT_TOKEN


dialog = Dialog()
dialog.mode = None

dsh = DeepSeekHandler()


async def start(update, context):
    dialog.mode = "main"
    text = load_message("main")
    await send_photo(update, context, "main")
    await send_text(update, context, text)

    await show_main_menu(
        update,
        context,
        {
            "start": "главное меню бота",
            "questions": "генерация вопросов с вариантами ответов 🧠",
            "results": "результаты тестирования ✅",
            "gpt": "задать вопрос чату GPT ",
        },
    )


async def gpt(update, context):
    dialog.mode = "gpt"
    text = load_message("gpt")
    await send_photo(update, context, "gpt")
    await send_text(update, context, text)


async def gpt_dialog(update, context):
    text = update.message.text
    prompt = load_prompt("gpt")
    my_message = await send_text(update, context, "ChatGPT 🧠 занимается генерацией вашего профиля. " "Подождите пару секунд...")
    answer = await dsh.send_question(prompt, text)
    await my_message.edit_text(answer)


async def questions(update, context):
    dialog.mode = "questions"
    text = load_message("questions")
    await send_text(update, context, text)


async def questions_dialog(update, context):
    text = update.message.text
    prompt = load_prompt("questions")
    my_message = await send_text(update, context, "ChatGPT 🧠 занимается генерацией вашего профиля. " "Подождите пару секунд...")
    answer = await dsh.send_question(prompt, text)
    await my_message.edit_text(answer)


async def results(update, context):
    dialog.mode = "results"
    text = load_message("results")
    await send_text(update, context, text)


async def results_dialog(update, context):
    text = update.message.text
    prompt = load_prompt("results")
    my_message = await send_text(update, context, "ChatGPT 🧠 занимается генерацией вашего профиля. " "Подождите пару секунд...")
    answer = await dsh.send_question(prompt, text)
    await my_message.edit_text(answer)


async def hello(update, context):
    if dialog.mode == "gpt":
        await gpt_dialog(update, context)
    if dialog.mode == "questions":
        await questions_dialog(update, context)
    if dialog.mode == "results":
        await results_dialog(update, context)
    else:
        await send_text(update, context, "Выберите необходимые для вас пункты.")


if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()  # Put Telegram token
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("gpt", gpt))
    app.add_handler(CommandHandler("questions", questions))
    app.add_handler(CommandHandler("results", results))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))

    app.run_polling()
