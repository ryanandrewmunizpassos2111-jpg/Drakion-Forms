import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
import os

TOKEN = os.getenv("TOKEN3")

LOG_CHANNEL_ID = 1484325859681767475

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================= CACHE =================
user_forms = {}

# ================= MODAL PT 1 =================
class FormModalPt(Modal, title="Staff Form (1/2)"):
    
    pergunta1 = TextInput(label="1.Qual é o seu nick (Discord e Roblox)?", required=True)
    pergunta2 = TextInput(label="2.Qual é a sua idade?", required=True)
    pergunta3 = TextInput(label="3.Há quanto tempo você usa Discord?", required=True)
    pergunta4 = TextInput(label="4.Há quanto tempo você joga Roblox?", required=True)
    pergunta5 = TextInput(label="5.O que você acha do servidor?", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        user_forms[interaction.user.id] = {
            "p1": self.pergunta1.value,
            "p2": self.pergunta2.value,
            "p3": self.pergunta3.value,
            "p4": self.pergunta4.value,
            "p5": self.pergunta5.value,
        }

        await interaction.response.send_message(
            "✅ Parte 1 enviada! Clique abaixo para continuar.",
            view=NextFormView(),
            ephemeral=True
        )

# ================= MODAL PT 2 =================
class FormModalPt2(Modal, title="Staff Form (2/2)"):

    pergunta6 = TextInput(label="6.Você já teve experiência como staff?", required=True)
    pergunta7 = TextInput(label="7.Qual sua disponibilidade?", required=True)
    pergunta8 = TextInput(label="8.Como lidaria com membro tóxico?", required=True)
    pergunta9 = TextInput(label="9.Você entende inglês?", required=True)
    pergunta10 = TextInput(label="10.Por que deve ser staff?", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        data = user_forms.get(interaction.user.id)

        if not data:
            await interaction.response.send_message("Erro ao salvar respostas.", ephemeral=True)
            return

        channel = interaction.client.get_channel(LOG_CHANNEL_ID)

        embed = discord.Embed(
            title="📋 Novo formulário enviado",
            color=discord.Color.blue()
        )

        embed.add_field(name="`Usuário:`", value=interaction.user.mention, inline=False)

        embed.add_field(name="`Nick:`", value=data["p1"], inline=False)
        embed.add_field(name="`Idade:`", value=data["p2"], inline=False)
        embed.add_field(name="`Tempo Discord:`", value=data["p3"], inline=False)
        embed.add_field(name="`Tempo Roblox:`", value=data["p4"], inline=False)
        embed.add_field(name="`Opinião:`", value=data["p5"], inline=False)

        embed.add_field(name="`Experiência:`", value=self.pergunta6.value, inline=False)
        embed.add_field(name="`Disponibilidade:`", value=self.pergunta7.value, inline=False)
        embed.add_field(name="`Membro tóxico:`", value=self.pergunta8.value, inline=False)
        embed.add_field(name="`Inglês:`", value=self.pergunta9.value, inline=False)
        embed.add_field(name="`Motivo:`", value=self.pergunta10.value, inline=False)

        embed.set_footer(
            text="Drakion Forms © | All Rights Reserved.",
            icon_url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048"
        )

        embed.set_image(url="https://cdn.discordapp.com/attachments/1482181421341872259/1482192202976202783/output.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048")

        await channel.send(embed=embed)

        del user_forms[interaction.user.id]

        await interaction.response.send_message(
            "✅ Formulário enviado com sucesso!",
            ephemeral=True
        )

# ================= BOTÃO CONTINUAR =================
class NextFormButton(Button):
    def __init__(self):
        super().__init__(
            label="Continuar formulário",
            style=discord.ButtonStyle.green,
            custom_id="next_form_button"
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FormModalPt2())

class NextFormView(View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_item(NextFormButton())

# ================= BOTÃO INICIAL =================
class FormButtonPt(Button):
    def __init__(self):
        super().__init__(
            label="Enviar",
            style=discord.ButtonStyle.green,
            custom_id="form_button_pt"
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FormModalPt())

# ================= VIEW =================
class FormViewPt(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FormButtonPt())

# ================= COMANDO =================
@bot.command()
async def formulario(ctx):
    embed = discord.Embed(
        title="📋 Candidatura para Staff",
        description="Quer fazer parte da equipe e ajudar o servidor a crescer?\nPreencha o formulário com atenção e responda tudo com sinceridade.\n\n📌 Procuramos pessoas ativas, responsáveis e com maturidade.\n\n⚠️ Respostas vagas ou brincadeiras podem resultar em rejeição.\n\nClique no botão abaixo para iniciar o formulário.",
        color=discord.Color.red()
    )

    embed.set_footer(
        text="Drakion Forms © | All Rights Reserved.",
        icon_url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048"
    )

    embed.set_image(url="https://cdn.discordapp.com/attachments/1482181421341872259/1482192202976202783/output.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048")

    await ctx.send(embed=embed, view=FormViewPt())

# ================= READY =================
@bot.event
async def on_ready():
    bot.add_view(FormViewPt())
    print(f"✅ Bot online como {bot.user}")

bot.run(TOKEN)
