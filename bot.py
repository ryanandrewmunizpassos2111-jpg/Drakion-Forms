import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
import os

TOKEN = os.getenv("TOKEN3")

LOG_CHANNEL_ID = 123456789012345678  # coloca o ID do canal de logs

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================= MODAL =================
class FormModal(Modal, title="Formulário da Staff"):

    pergunta1 = TextInput(
        label="Qual é o problema?",
        placeholder="Descreva o ocorrido...",
        required=True,
        max_length=300
    )

    pergunta2 = TextInput(
        label="Quem está envolvido?",
        placeholder="Mencione usuários...",
        required=True,
        max_length=200
    )

    pergunta3 = TextInput(
        label="Provas (opcional)",
        placeholder="Links, prints, etc...",
        required=False,
        max_length=300
    )

    async def on_submit(self, interaction: discord.Interaction):
        channel = bot.get_channel(LOG_CHANNEL_ID)

        embed = discord.Embed(
            title="📋 Novo formulário enviado",
            color=discord.Color.blue()
        )

        embed.add_field(name="Usuário", value=interaction.user.mention, inline=False)
        embed.add_field(name="Problema", value=self.pergunta1.value, inline=False)
        embed.add_field(name="Envolvidos", value=self.pergunta2.value, inline=False)
        embed.add_field(name="Provas", value=self.pergunta3.value or "Nenhuma", inline=False)

        await channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ Formulário enviado com sucesso!",
            ephemeral=True
        )

# ================= BOTÃO =================
class FormButton(Button):
    def __init__(self):
        super().__init__(label="Abrir Formulário", style=discord.ButtonStyle.green)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FormModal())

# ================= VIEW =================
class FormView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FormButton())

# ================= COMANDO =================
@bot.command()
async def formulario(ctx):
    embed = discord.Embed(
        title="📋 Formulário da Staff",
        description="Clique no botão abaixo para preencher o formulário.",
        color=discord.Color.blurple()
    )

    await ctx.send(embed=embed, view=FormView())

# ================= READY =================
@bot.event
async def on_ready():
    print(f"✅ Bot online como {bot.user}")

bot.run(TOKEN)
