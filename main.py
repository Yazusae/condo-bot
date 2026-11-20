import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

WELCOME_CHANNEL_ID = 1572604034832138321  # #media
ANNOUNCEMENT_ID = 1571521425733324852  # #annoucement
MEDIA_ID = 1572604034832138321         # #media
SERVER_LINK_ID = 1571520695853387898   # #server-link

GIF_URL = "https://i.pinimg.com/originals/79/27/4c/79274c2f6f2e94bfc9ed494c94fd2d51.gif"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} - Ready!")

def make_welcome_embed(member: discord.Member):
    embed = discord.Embed(
        title="*°9°* • ✦ :CONDO HUB SOCIETY: • ✦ 9°",
        description=(
            "─────9୨────\n"
            f"• ANNOUNCEMENT ➳ <#{ANNOUNCEMENT_ID}> 📣 | ANNOUCEMENT ୨\n"
            f"• MEDIA ➳ <#{MEDIA_ID}> 🖼️ | MEDIA ୨\n"
            f"• SERVER LINK ➳ <#{SERVER_LINK_ID}> 🔗 | SERVER-LINK ୨\n\n"
            f"we now have **{member.guild.member_count}** members<3"
        ),
        color=0xFF2D55
    )
    embed.set_image(url=GIF_URL)
    if member.guild.icon:
        embed.set_author(name="condosbuilding", icon_url=member.guild.icon.url)
    else:
        embed.set_author(name="condosbuilding")
    return embed

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if not channel:
        return
    embed = make_welcome_embed(member)
    await channel.send(content="@CONDO MAKER", embed=embed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if not channel:
        return
    embed = discord.Embed(
        title="Someone left...",
        description=f"**{member.name}** left the condo.\nwe now have **{member.guild.member_count}** members",
        color=0x2B2D31
    )
    embed.set_image(url=GIF_URL)
    await channel.send(embed=embed)

@bot.command()
async def testwelcome(ctx):
    embed = make_welcome_embed(ctx.author)
    await ctx.send(content="@CONDO MAKER", embed=embed)

bot.run(TOKEN)