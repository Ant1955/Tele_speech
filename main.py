import telebot
import speech_recognition as sr
import soundfile as sf
import pyautogui
# required numpy and soundfile packages

API_TOKEN = 'YOUR_BOT_API_TOKEN'  #  @Advt2024r_bot.
bot = telebot.TeleBot('7492868065:AAHWEDIXDtemTtxLZtDknYFmivKK8x_7EUw')

user_states = {}
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        file_info = bot.get_file(message.voice.file_id)
        file_path = file_info.file_path
        downloaded_file = bot.download_file(file_path)

        with open("voice_message.ogg", 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
        #  print("ogg file downloaded. Done!")
        data, samplerate = sf.read('voice_message.ogg')
        #  print("ogg file opened . Done!")
        sf.write('voice_message.wav', data, samplerate)
        #  print("wav file created. Done!")
        recognizer = sr.Recognizer()
        with sr.AudioFile("voice_message.wav") as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="ru-RU")

        user_states[message.chat.id] = text
        pyautogui.write(text)
        markup = telebot.types.InlineKeyboardMarkup()
        edit_button = telebot.types.InlineKeyboardButton(text="Редактировать", callback_data="edit_text")
        no_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data="no_edit")
        markup.add(edit_button, no_button)

        bot.reply_to(message, f"Распознанный текст: {text}", reply_markup=markup)

    except Exception as e:
        print(f"Ошибка: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "edit_text")
def callback_edit_text(call):
    current_text = user_states.get(call.message.chat.id, "")
    bot.send_message(call.message.chat.id, f"Текущий текст: {current_text}\nСкажите новый текст:")

    bot.register_next_step_handler(call.message, receive_edited_text)

def receive_edited_text(message):
    new_text = message.text
    user_states[message.chat.id] = new_text
    bot.send_message(message.chat.id, f"Обновленный текст: {new_text}")

    # Предложить снова редактировать
    markup = telebot.types.InlineKeyboardMarkup()
    edit_button = telebot.types.InlineKeyboardButton(text="Редактировать", callback_data="edit_text")
    no_button = telebot.types.InlineKeyboardButton(text="Нет", callback_data="no_edit")
    markup.add(edit_button, no_button)
    bot.send_message(message.chat.id, "Хотите ещё раз отредактировать текст?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "no_edit")
def callback_no_edit(call):
    bot.send_message(call.message.chat.id, "Редактирование отменено.")


bot.polling(none_stop=True)