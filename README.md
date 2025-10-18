# 🤖 Diagrammer Bot for Telegram

Создавайте **интерактивные диаграммы** прямо в Telegram!  
Этот бот работает **локально на Windows**, не требует серверов и позволяет визуализировать ваши идеи с помощью **текста**, **изображений** и **связей**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/c32b1788-a330-4833-88cc-03215171edd0" width="400" alt="Пример темной темы">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/228a001c-f9cb-483c-a6f9-5ec7ff25e7b2" width="400" alt="Пример светлой темы">
</p>

---

## 🧩 Ключевые Возможности

- 🧱 **Текст и Изображения:** Добавляйте текстовые и графические блоки (узлы).
- 🔗 **Связи:** Легко соединяйте блоки направленными стрелками.
- 🎨 **Две Темы:** Переключайтесь между стильной тёмной и чистой светлой темами.
- 💾 **Сохранение и Загрузка:** Создавайте, сохраняйте и загружайте несколько диаграмм.
- 🖼️ **Экспорт в PNG:** Скачивайте готовые диаграммы в высоком разрешении с водяным знаком.
- 👮 **Админ-панель:** Встроенная команда `/users` для администратора.
- 💻 **Локальная работа:** Не требует хостинга, работает прямо на вашем ПК.
- ✅ **Оптимизировано для Windows:** Полная совместимость с Windows 10 / 11.

---

**Протестировать:** [Diagrammer Bot](https://t.me/diagrammer_robot)

---

## 🚀 Установка и Запуск (для Windows)

Всего **6 простых шагов**, чтобы запустить бота на вашем компьютере.

---

### 🔹 Шаг 1: Установите Python

1. Скачайте установщик **Python 3.11 или новее** с [официального сайта](https://www.python.org/downloads/windows/).  
2. Запустите его и **обязательно** поставьте галочку:
   > ✅ **Add Python to PATH**
3. **Проверьте установку:**  
   Откройте `cmd` или `PowerShell` и выполните:
   ```bash
   python --version
   ```
   Если видите `Python 3.11.5` — всё отлично!

---

### 🔹 Шаг 2: Установите Graphviz

Graphviz — это "движок", который рисует диаграммы.

1. Перейдите на [страницу загрузки Graphviz](https://graphviz.org/download/).
2. В разделе **Stable Windows install packages** скачайте `.exe` установщик.
3. Установите Graphviz в стандартную директорию `C:\Program Files\Graphviz`.
4. Добавьте Graphviz в **PATH**:
   - Нажмите `Win + S` → “Переменные среды”  
   - Откройте “Изменение системных переменных среды”  
   - Нажмите “Переменные среды…” → выберите `Path` → “Изменить”  
   - Добавьте путь: `C:\Program Files\Graphviz\bin`  
5. Перезапустите терминал и проверьте:
   ```bash
   dot -V
   ```
   Если вы видите версию Graphviz — всё установлено правильно ✅

---

### 🔹 Шаг 3: Скачайте Проект

1. Установите [Git для Windows](https://git-scm.com/download/win), если его нет.
2. В командной строке выполните:
   ```bash
   git clone https://github.com/Lixher/diagrammer-bot.git
   cd diagrammer-bot
   ```
> 💡 Можно просто скачать ZIP-архив с GitHub и распаковать вручную.

---

### 🔹 Шаг 4: Настройте Виртуальное Окружение

Чтобы изолировать зависимости, создайте `venv`:
```bash
python -m venv venv
venv\Scripts\activate
```
После активации увидите `(venv)` слева в командной строке.

---

### 🔹 Шаг 5: Установите Зависимости

```bash
pip install -r requirements.txt
```
Если возникают ошибки — установите вручную:
```bash
pip install python-telegram-bot graphviz pillow
```

---

### 🔹 Шаг 6: Настройте и Запустите Бота

1. В Telegram найдите бота **@BotFather** и создайте нового.  
2. Скопируйте токен и создайте файл `config.py` в папке проекта:
   ```python
   BOT_TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"
   ```
3. Запустите бота:
   ```bash
   python main.py
   ```

🎉 Готово! Теперь бот работает локально и доступен в Telegram.

---

## ❗ Решение Частых Ошибок

| Ошибка | Причина | Решение |
|--------|----------|----------|
| `graphviz.backend.ExecutableNotFound` | Graphviz не установлен или не добавлен в PATH | Повторите Шаг 2, проверьте `dot -V` |
| `ModuleNotFoundError: No module named 'telegram'` | Не установлены зависимости | Активируйте venv и выполните `pip install -r requirements.txt` |
| `OSError: cannot open resource` | Не найден шрифт Arial | Установите шрифт Arial или добавьте .ttf в проект |
| `PermissionError: [WinError 32]` | PNG-файл занят | Закройте открытое изображение перед повторной генерацией |

---

## 🛠️ Стек Технологий

| Компонент | Назначение |
|------------|-------------|
| **Python 3.11+** | Основной язык |
| **python-telegram-bot** | Работа с Telegram API |
| **Graphviz** | Рендеринг диаграмм |
| **Pillow (PIL)** | Работа с изображениями |
| **JSON** | Лёгкая встроенная база данных |

---

## 📜 Лицензия

Проект распространяется по лицензии **MIT**.  
Вы можете свободно использовать, изменять и распространять код, сохраняя упоминание автора.

---

## 👤 Автор

**Diagrammer Bot**  
Разработчик: [@femidka777](https://t.me/femidka777)  
GitHub: [Lixher](https://github.com/Lixher)

---

## ⭐ Поддержите Проект

Если вам понравился бот — поставьте ⭐ на GitHub!  
Это лучшая благодарность и мотивация развивать проект дальше 🚀

EN

# 🤖 Diagrammer Bot for Telegram

Create **interactive diagrams** directly in Telegram!  
This bot works **locally on Windows**, requires **no servers**, and lets you visualize your ideas with **text**, **images**, and **connections**.

<p align="center">
  <img src="https://github.com/user-attachments/assets/c32b1788-a330-4833-88cc-03215171edd0" width="400" alt="Dark theme example">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://github.com/user-attachments/assets/228a001c-f9cb-483c-a6f9-5ec7ff25e7b2" width="400" alt="Light theme example">
</p>

---

## 🧩 Key Features

- 🧱 **Text & Images:** Add text and image nodes easily.
- 🔗 **Connections:** Link nodes with directional arrows.
- 🎨 **Themes:** Switch between elegant dark and clean light themes.
- 💾 **Save & Load:** Manage multiple diagram projects.
- 🖼️ **Export to PNG:** Download high-resolution diagrams with a watermark.
- 👮 **Admin Panel:** `/users` command for administrator use.
- 💻 **Fully Local:** Works offline, no external servers required.
- ✅ **Optimized for Windows:** 100% compatible with Windows 10 / 11.

---

## 🚀 Installation & Setup (Windows)

Just **6 simple steps** to get your bot running locally.

---

### 🔹 Step 1: Install Python

1. Download **Python 3.11+** from the [official website](https://www.python.org/downloads/windows/).
2. During installation, make sure to check:
   > ✅ **Add Python to PATH**
3. Verify installation:
   ```bash
   python --version
   ```
   You should see something like `Python 3.11.5`.

---

### 🔹 Step 2: Install Graphviz

Graphviz is the rendering engine that draws your diagrams.

1. Go to [Graphviz Download Page](https://graphviz.org/download/).
2. Find the **Stable Windows install packages** section and download the `.exe` installer.
3. Install it (recommended path: `C:\Program Files\Graphviz`).
4. Add Graphviz to your **PATH**:
   - Press `Win + S` → search for *Environment Variables*.
   - Click *Edit the system environment variables*.
   - Choose *Environment Variables…* → under *System variables* → select `Path` → click *Edit*.
   - Add a new entry: `C:\Program Files\Graphviz\bin`
   - Click *OK* everywhere.
5. Restart your terminal and check installation:
   ```bash
   dot -V
   ```
   You should see the Graphviz version.

---

### 🔹 Step 3: Download the Project

1. Install [Git for Windows](https://git-scm.com/download/win) if you don’t have it.
2. Open CMD or PowerShell and run:
   ```bash
   git clone https://github.com/Lixher/diagrammer-bot.git
   cd diagrammer-bot
   ```
   *(Replace `Lixher` with your GitHub username if needed)*

> 💡 Alternatively, you can click **"Code → Download ZIP"** on GitHub and extract it manually.

---

### 🔹 Step 4: Create Virtual Environment

A virtual environment keeps dependencies clean and isolated.

```bash
python -m venv venv
venv\Scripts\activate
```
You should now see `(venv)` at the beginning of your terminal line.

---

### 🔹 Step 5: Install Dependencies

Install all required libraries:
```bash
pip install -r requirements.txt
```

If something fails, install manually:
```bash
pip install python-telegram-bot graphviz pillow
```

---

### 🔹 Step 6: Configure and Run the Bot

1. Open Telegram and start a chat with **@BotFather**.
2. Create a new bot → copy your API token.
3. In your project folder, create a file called `config.py`:
   ```python
   BOT_TOKEN = "YOUR_BOTFATHER_TOKEN"
   ```
4. Run the bot:
   ```bash
   python main.py
   ```

🎉 **Done!** Your bot is live and ready in Telegram.

---

## ❗ Common Issues & Fixes

| Error | Cause | Solution |
|-------|--------|-----------|
| `graphviz.backend.ExecutableNotFound` | Graphviz not installed or PATH not set | Re-do Step 2, verify `dot -V` works |
| `ModuleNotFoundError: No module named 'telegram'` | Missing dependencies | Activate venv and run `pip install -r requirements.txt` |
| `OSError: cannot open resource` | Missing system font (Arial) | Install Arial or copy any `.ttf` font file into the project folder |
| `PermissionError: [WinError 32]` | Diagram image is open elsewhere | Close the PNG in `/diagrams` folder before regenerating |

---

## 🛠️ Tech Stack

| Component | Purpose |
|------------|----------|
| **Python 3.11+** | Core language |
| **python-telegram-bot** | Telegram Bot API integration |
| **Graphviz** | Diagram rendering engine |
| **Pillow (PIL)** | Image processing & watermarking |
| **JSON** | Simple data storage |

---

## 📜 License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute it, provided you keep author attribution.

---

## 👤 Author

**Diagrammer Bot**  
Developer: [@femidka777](https://t.me/femidka777)  
GitHub: [Lixher](https://github.com/Lixher)

---

## ⭐ Support the Project

If you like this bot, please give it a ⭐ on GitHub — it really helps motivate new feature development!

---
