from discord.ext import commands
from discord import app_commands
import discord

class VoiceCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="join")
    @app_commands.describe(channel="Voice channel to join")
    async def join(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        if interaction.user.voice:
            await channel.connect()
            await interaction.response.send_message(f"Connected to {channel.name}")
        else:
            await interaction.response.send_message("You need to be in a voice channel to use this command.", ephemeral=True)

    @app_commands.command(name="speak")
    @app_commands.describe(message="Message to speak")
    async def speak(self, interaction: discord.Interaction, message: str):
        if interaction.guild.voice_client:
            interaction.guild.voice_client.play(discord.FFmpegPCMAudio(executable="path/to/ffmpeg", source=discord.FFmpegOpusAudio(message)))
            await interaction.response.send_message("Speaking...", ephemeral=True)
        else:
            await interaction.response.send_message("Bot is not connected to a voice channel.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(VoiceCommands(bot))
