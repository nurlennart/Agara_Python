import discord

class Poll:
    def __init__(self, bot):
        self._bot = bot

    # generate new poll embed
    async def GeneratePollEmbed(self, ctx, question, seconds):
        info_embed = discord.Embed(title="Poll [" + seconds + " Sekunden]", color=0x9b59b6)
        info_embed.add_field(name="Frage", value=question, inline=True)

        return info_embed

    # generate new poll result embed
    async def GeneratePollResultEmbed(self, ctx, question, upvotes, downvotes):
        result_embed = discord.Embed(title="Poll Ergebnisse der Frage", description="**" + question + "**", color=0x9b59b6)
        result_embed.add_field(name="➕", value=int(upvotes) - 1)
        result_embed.add_field(name="➖", value=int(downvotes) -1)

        return result_embed
