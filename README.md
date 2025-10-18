# 🤖 Diagrammer Bot for Telegram (Windows Edition)

Бот для создания **интерактивных диаграмм** прямо в Telegram.  
Работает локально на Windows, не требует серверов, поддерживает **изображения**, **стрелки**, **темы (тёмную/светлую)** и **экспорт в PNG**.

---

## 🧩 Возможности

- 🧱 Добавление **текстовых** и **графических** блоков (узлов)
- 🔗 Соединение блоков стрелками
- 🎨 Светлая и тёмная темы оформления
- 🖼️ Экспорт диаграмм в PNG с водяным знаком
- 💾 Сохранение и загрузка пользовательских схем
- 👮 Команды администратора (например `/users`)
- 🧠 Работа без интернета (локально)
- ✅ Полностью совместимо с Windows 10 / 11

---

📜 Лицензия

Проект распространяется по лицензии MIT
Свободно используй, модифицируй и делись, сохраняя ссылку на автора.

👤 Автор

Diagrammer Bot
Разработчик: @femidka777

GitHub: https://github.com/<Lixher>

⭐ Поддержи проект

Если бот оказался полезным — поставь ⭐ на GitHub!
Это поможет развивать проект и добавлять новые функции 🚀

---

## ⚙️ Что используется

| Компонент | Назначение |
|------------|------------|
| **Python 3.11+** | Основной язык |
| **python-telegram-bot** | API Telegram |
| **Graphviz** | Рендеринг диаграмм |
| **Pillow (PIL)** | Работа с изображениями и водяными знаками |
| **asyncio** | Асинхронность и стабильность |

---

## 🚀 Установка и запуск (ПОЛНОСТЬЮ для Windows)

### 🔹 Шаг 1 — Установи Python
Скачай и установи **Python 3.11 или выше**:  
👉 [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

Во время установки обязательно отметь галочку:
> ✅ "Add Python to PATH"

Проверить установку:
```bash
python --version

---

🔹 Шаг 2 — Установи Graphviz

Graphviz — это библиотека, которая строит диаграммы.

Скачай установщик с https://graphviz.org/download/

→ Выбери Stable Windows installer (.exe)

Установи Graphviz в стандартную папку:
C:\Program Files\Graphviz

Добавь путь в переменную среды PATH

---

🔹 Шаг 3 — Клонируй проект с GitHub
git clone https://github.com/<your-username>/diagrammer-bot.git
cd diagrammer-bot


(если Git не установлен — скачай с https://git-scm.com/download/win)

---

🔹 Шаг 4 — Создай виртуальное окружение
python -m venv venv
venv\Scripts\activate


Теперь ты должен увидеть (venv) слева в командной строке.

---

🔹 Шаг 5 — Установи зависимости
pip install -r requirements.txt


Если вдруг появится ошибка при установке Pillow — попробуй:

pip install --upgrade pip setuptools wheel
pip install pillow graphviz python-telegram-bot


---

В файле Config.py токен бота

---

🔹 Шаг 6 - запусти бота
python main.py

---

❗ Частые ошибки и решения
Ошибка	Причина	Решение
graphviz.backend.ExecutableNotFound	Graphviz не в PATH	Добавь C:\Program Files\Graphviz\bin в PATH
ModuleNotFoundError: No module named 'telegram'	Не установлены зависимости	pip install -r requirements.txt
OSError: cannot open resource	Не найден шрифт arial.ttf	Скопируй любой .ttf шрифт в папку проекта
PermissionError: [WinError 32]	Файл диаграммы открыт	Закрой изображение перед повторным рендером
