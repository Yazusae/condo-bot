import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# --- CHANGE THESE ---
WELCOME_CHANNEL_ID = 123456789012345678  # Right-click your #welcome channel > Copy Channel ID
PUBLIC_CONDO_ID = 111111111111111111
PRIVATE_CONDO_ID = 222222222222222222
RULES_ID = 333333333333333333
ANNOUNCE_ID = 444444444444444444
GIF_URL = "https://media.tenor.com/your-gif-here.gif"  # Your welcome GIF link
LEAVE_GIF_URL = "https://media.tenor.com/your-leave-gif-here.gif"  # Optional

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} - Ready!")

def make_welcome_embed(member: discord.Member):
    embed = discord.Embed(
        title="*˚✦ ･ﾟ:CONDO HUB SOCIETY:･ﾟ ✦˚*",
        description=(
            "────✦────\n"
            f"🤍 • PUBLIC GAME ➳ <#{PUBLIC_CONDO_ID}>\n"
            f"🪓 • PRIVATE GAME ➳ <#{PRIVATE_CONDO_ID}>\n"
            f"📌 • RULES ➳ <#{RULES_ID}>\n"
            f"📣 • ANNOUNCEMENT ➳ <#{ANNOUNCE_ID}>\n\n"
            f"we now have **{member.guild.member_count}** members<3"
        ),
        color=0xFF8FAB  # pink sidebar like your screenshot
    )
    # This is the big GIF at the bottom
    embed.set_image(url=GIF_URL)
    # Top-left small icon
    if member.guild.icon:
        embed.set_author(name="condosbuilding", icon_url=member.guild.icon.url)
    embed.set_footer(text=f"Welcome, {member.name}")
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
    if LEAVE_GIF_URL:
        embed.set_image(url=LEAVE_GIF_URL)
    await channel.send(embed=embed)

# Test command to preview without waiting for someone to join
@bot.command()
async def testwelcome(ctx):
    embed = make_welcome_embed(ctx.author)
    await ctx.send(content="@CONDO MAKER", embed=embed)

bot.run(TOKEN)