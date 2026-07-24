# ███████╗██╗   ██╗███████╗████████╗██╗  ██╗    ██╗  ██╗███╗   ███╗
# ██╔════╝██║   ██║██╔════╝╚══██╔══╝██║  ██║    ██║  ██║████╗ ████║
# ███████╗██║   ██║█████╗     ██║   ███████║    ███████║██╔████╔██║
# ╚════██║██║   ██║██╔══╝     ██║   ██╔══██║    ╚════██║██║╚██╔╝██║
# ███████║╚██████╔╝███████╗   ██║   ██║  ██║         ██║██║ ╚═╝ ██║
# ╚══════╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝         ╚═╝╚═╝     ╚═╝
#
#                   🚀  S U E T H . 4 M  🚀
#
#                      Administration Bot
#
#                  Developed by @sueth.4m :D
# ==================================================================
#  Project : SenSei 🍥
#  Version : v0.10.0 Beta 🚧
#  Language: Python 3.11+
#  Author  : @sueth.4m
#  Server : Buteco dp Hitsuki 🍺
#  Discord : https://discord.gg/jAWXrqRe5C
# ==================================================================

import discord
from discord.ext import commands
from data.database import create_tables
from systems.voice_manager import VoiceManager
from systems.ranking.rank_manager import RankManager
from embeds.ranking_embeds import RankingEmbeds
from systems.reset_manager import ResetManager
import json
from pathlib import Path
import os
import secrets
import os
from dotenv import load_dotenv



# ================= CONFIG =================

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"

with CONFIG_PATH.open("r", encoding="utf-8") as file:
    config = json.load(file)

print(f"[CONFIG] Arquivo carregado: {CONFIG_PATH}")

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not isinstance(TOKEN, str) or not TOKEN.strip():
    raise RuntimeError(
        "A variável DISCORD_BOT_TOKEN não foi configurada."
    )

TOKEN = TOKEN.strip()
GUILD_ID = config["BOT"]["GUILD_ID"]

print("[CONFIG] TOKEN: carregado")
print(
    "[CONFIG] ENABLE_RESET:",
    config.get("SECURITY", {}).get(
        "ENABLE_RESET",
        "NÃO ENCONTRADO"
    )
)

# ================= INTENTS =================
intents = discord.Intents.default()

intents.guilds = True
intents.members = True
intents.voice_states = True
intents.messages = True
intents.message_content = True
intents.presences = True

# ================= BOT ================= 
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

bot.config = config

bot.voice_manager = VoiceManager(bot)
bot.rank_manager = RankManager(bot)
bot.ranking_embeds = RankingEmbeds(bot)
bot.reset_manager = ResetManager(bot)

print("[RESET MANAGER] Inicializado com sucesso.")

# =================
# COGS
# =================

INITIAL_EXTENSIONS = [
    "commands.rank",
    "commands.admin",
    "events.voice_tracker",
    "events.member_events",
    "events.message_logs",
    "events.voice_logs",
    "events.member_logs",
    "events.audit_logs",
    "events.server_status",
    "background.weekly_reset",
    "background.monthly_reset",
    "background.auto_restart",
]
# =================
# READY EVENT 
# ================= 

@bot.event
async def on_ready():

    print("=" * 50)
    print(f"BOT ONLINE: {bot.user}")
    print(f"ID: {bot.user.id}")
    print("=" * 50)

    # SYNC SLASH COMMANDS
    try:
        guild_obj = discord.Object(id=GUILD_ID)
        bot.tree.copy_global_to(guild=guild_obj)
        synced = await bot.tree.sync(guild=guild_obj)

        print(f"Slash commands sincronizados: {len(synced)}")

    except Exception as e:
        print(f"Erro ao sincronizar: {e}")

# ================= RESTORE VOICE SESSIONS =================

    bot.voice_manager.restore_sessions()

# ================= LOAD EXTENSIONS =================  

async def load_extensions():

    for extension in INITIAL_EXTENSIONS:

        try:
            await bot.load_extension(extension)
            print(f"[OK] {extension}")

        except Exception as e:
            print(f"[ERRO] {extension}")
            print(e)

# ================= MAIN =================  

async def main():

    async with bot:
        
        create_tables()

        await load_extensions()

        await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
