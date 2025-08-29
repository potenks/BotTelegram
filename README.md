# 🤖 Telegram Bot: Instagram Followers Tracker
Bot de Telegram para monitorear el crecimiento de seguidores en Instagram.

# 🌟 Características
📊 Monitoreo de seguidores de cuentas y agrupaciones de Instagram.

📨 Respuestas automáticas a comandos:

seguidores: Muestra el estado actual de las cuentas.

prueba: Confirma que el bot está activo.

# ⚙️ Configuración flexible mediante archivo .env.

# 🚀 Próximas funcionalidades:

📈 Persistencia de datos históricos.

🔄 Comparación entre monitoreos.

⏳ Ejecución automática programada.

# 🛠 Instalación y Configuración
1. Clonar el repositorio
        git clonehttps: https://github.com/potenks/BotTelegram.git
2. Instalar dependencias
        pip install -r requirements.txt
3. Configurar el archivo .env
Crea un archivo .env con el siguiente formato:

        .env
        Token del bot de Telegram (obtenido con @BotFather)
        TELEGRAM_BOT_TOKEN=tu_token_aqui

        #Chats autorizados para recibir respuestas (IDs numéricos)
        CHAT_ID_1=123456789
        CHAT_ID_2=987654321

        #Sectores y cuentas a monitorear
        Sector= sector1, sector2
        Cuentas_bloque1=cuenta1, cuenta2
        Cuentas_bloque2=cuenta1, cuenta2
# 🖥 Uso
1. Iniciar el bot
bash
Copy
python bot.py
2. Comandos disponibles en Telegram
/seguidores: Devuelve el estado actual de las cuentas configuradas.

/prueba: Responde con un mensaje de confirmación (útil para verificar que el bot está activo).

# 📂 Estructura del Proyecto
Copy
instagram-followers-bot/
├── bot.py               #Lógica principal del bot
├── requirements.txt     #Dependencias de Python
├── .env.example         # Plantilla del archivo de configuración
└── README.md            # Este archivo

# 📌 Próximos Pasos
🗃️ Persistencia de datos: Guardar históricos en una base de datos.

📉 Comparativas: Gráficos de crecimiento entre fechas.

🤖 Automatización: Ejecución periódica en servidor (ej: cada 24h).

# 🔗 Recursos Útiles
 https://docs.python-telegram-bot.org/en/stable/
 https://core.telegram.org/bots
