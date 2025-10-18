# admin.py

import json
import os
from telegram import Update
from telegram.ext import ContextTypes

# --- НАСТРОЙКИ ---
# Вставь сюда свой Telegram User ID
ADMIN_USER_ID = 123123123 
# Путь к файлу нашей базы данных
DB_FILE = "user_diagrams.json"


async def users_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Отправляет администратору отчет о количестве и ID всех пользователей.
    """
    # 1. ПРОВЕРКА БЕЗОПАСНОСТИ: Убеждаемся, что команду отправил админ
    if update.effective_user.id != ADMIN_USER_ID:
        # Если это не админ, просто ничего не делаем.
        # Это лучше, чем отвечать "недостаточно прав", чтобы не раскрывать существование команды.
        print(f"Попытка несанкционированного доступа к /users от user_id: {update.effective_user.id}")
        return

    # 2. Проверяем, существует ли файл базы данных
    if not os.path.exists(DB_FILE):
        await update.message.reply_text("❌ Файл базы данных (user_diagrams.json) не найден.")
        return

    # 3. Читаем и обрабатываем данные
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        user_ids = data.keys()
        total_users = len(user_ids)

        if total_users == 0:
            await update.message.reply_text("В базе данных пока нет пользователей.")
            return

        # 4. Формируем красивый отчет
        message = f"📊 **Всего пользователей в боте: {total_users}**\n\n"
        message += "Список User ID:\n"
        
        # Добавляем ID всех пользователей
        for user_id in user_ids:
            # Используем `<code>`, чтобы ID можно было легко скопировать
            message += f"- <code>{user_id}</code>\n"

        # 5. Отправляем отчет
        # Проверяем на лимит длины сообщения в Telegram
        if len(message) > 4096:
            message = f"📊 **Всего пользователей в боте: {total_users}**\n\nСписок слишком длинный для одного сообщения."
        
        await update.message.reply_text(message, parse_mode='HTML')

    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка при чтении базы данных: {e}")