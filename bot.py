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
            "lang": "pt",
            "Nick:": self.pergunta1.value,
            "Idade:": self.pergunta2.value,
            "Tempo Discord:": self.pergunta3.value,
            "Tempo Roblox:": self.pergunta4.value,
            "Opinião:": self.pergunta5.value,
        }

        await interaction.response.send_message(
            "✅ Parte 1 enviada! Clique abaixo para continuar.",
            view=NextFormViewPt(),
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
            return await interaction.response.send_message("Erro.", ephemeral=True)

        channel = interaction.client.get_channel(LOG_CHANNEL_ID)

        embed = discord.Embed(title="📋 Novo formulário", color=discord.Color.red())
        embed.add_field(name="Usuário", value=interaction.user.mention, inline=False)

        for key, value in data.items():
            if key != "lang":
                embed.add_field(name=f"`{key}`", value=value, inline=False)

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

        await interaction.response.send_message("✅ Envio realizado com sucesso! Entraremos em contato caso você seja selecionado(a)!", ephemeral=True)

# ================= MODAL EN 1 =================
class FormModalEn(Modal, title="Staff Form (1/2)"):

    q1 = TextInput(label="1.What is your nickname?", required=True)
    q2 = TextInput(label="2.What is your age?", required=True)
    q3 = TextInput(label="3.How long using Discord?", required=True)
    q4 = TextInput(label="4.How long playing Roblox?", required=True)
    q5 = TextInput(label="5.What do you think of server?", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        user_forms[interaction.user.id] = {
            "lang": "en",
            "Nick:": self.q1.value,
            "Idade:": self.q2.value,
            "Tempo Discord:": self.q3.value,
            "Tempo Roblox:": self.q4.value,
            "Opinião:": self.q5.value,
        }

        await interaction.response.send_message(
            "✅ Part 1 done! Click below to continue.",
            view=NextFormViewEn(),
            ephemeral=True
        )

# ================= MODAL EN 2 =================
class FormModalEn2(Modal, title="Staff Form (2/2)"):

    q6 = TextInput(label="6.Staff experience?", required=True)
    q7 = TextInput(label="7.Availability?", required=True)
    q8 = TextInput(label="8.How handle toxic user?", required=True)
    q9 = TextInput(label="9.Do you understand English?", required=True)
    q10 = TextInput(label="10.Why should you be staff?", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        data = user_forms.get(interaction.user.id)

        if not data:
            return await interaction.response.send_message("Error.", ephemeral=True)

        channel = interaction.client.get_channel(LOG_CHANNEL_ID)

        embed = discord.Embed(title="📋 New form", color=discord.Color.red())
        embed.add_field(name="User", value=interaction.user.mention, inline=False)

        for key, value in data.items():
            if key != "lang":
                embed.add_field(name=f"`{key}`", value=value, inline=False)

        embed.add_field(name="`Experiência:`", value=self.q6.value, inline=False)
        embed.add_field(name="`Disponibilidade:`", value=self.q7.value, inline=False)
        embed.add_field(name="`Membro tóxico:`", value=self.q8.value, inline=False)
        embed.add_field(name="`Inglês:`", value=self.q9.value, inline=False)
        embed.add_field(name="`Motivo:`", value=self.q10.value, inline=False)
        embed.set_footer(
        text="Drakion Forms © | All Rights Reserved.",
        icon_url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048"
        )
        embed.set_image(url="https://cdn.discordapp.com/attachments/1482181421341872259/1482192202976202783/output.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048")

        await channel.send(embed=embed)
        del user_forms[interaction.user.id]

        await interaction.response.send_message("✅ Submitted successfully! We will contact you if you are selected!", ephemeral=True)

# ================= BOTÕES =================
class NextFormButtonPt(Button):
    def __init__(self):
        super().__init__(label="Continuar", style=discord.ButtonStyle.green, custom_id="next_pt")

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FormModalPt2())

class NextFormViewPt(View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_item(NextFormButtonPt())

class NextFormButtonEn(Button):
    def __init__(self):
        super().__init__(label="Continue", style=discord.ButtonStyle.green, custom_id="next_en")

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FormModalEn2())

class NextFormViewEn(View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_item(NextFormButtonEn())

class FormButtonPt(Button):
    def __init__(self):
        super().__init__(label="Enviar", style=discord.ButtonStyle.green, custom_id="form_pt")

    async def callback(self, interaction):
        await interaction.response.send_modal(FormModalPt())

class FormButtonEn(Button):
    def __init__(self):
        super().__init__(label="Send", style=discord.ButtonStyle.green, custom_id="form_en")

    async def callback(self, interaction):
        await interaction.response.send_modal(FormModalEn())

class FormViewPt(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FormButtonPt())

class FormViewEn(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FormButtonEn())

# ================= COMANDOS =================
@bot.command()
async def formulario(ctx):
    embed = discord.Embed(
        title="📋 Candidatura para Staff",
        description="Quer fazer parte da equipe e ajudar o servidor a crescer?\nPreencha o formulário com atenção e responda tudo com sinceridade.\n\n📌 Procuramos pessoas ativas, responsáveis e com maturidade.\n\n⚠️ Respostas vagas ou brincadeiras podem resultar em punição.\n\nComplete as duas partes do formulário.\n\nClique no botão abaixo para iniciar o formulário.",
        color=discord.Color.red()
    )
    embed.set_footer(
        text="Drakion Forms © | All Rights Reserved.",
        icon_url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048"
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1482181421341872259/1482192202976202783/output.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048")
    
    await ctx.send(embed=embed, view=FormViewPt())

@bot.command()
async def form(ctx):
    embed = discord.Embed(
        title="📋 Staff Application",
        description="Want to be part of the team and help the server grow?\nFill out the form carefully and answer everything with Sincerity.\n\n📌 We are looking for active, responsible and mature people.\n\n⚠️ Vague answers or jokes may result in punishment.\n\nComplete both parts of the form.\n\nClick the button below to start the form.",
        color=discord.Color.red()
    )
    embed.set_footer(
        text="Drakion Forms © | All Rights Reserved.",
        icon_url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048"
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1482181421341872259/1482192202976202783/output.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048")
    
    await ctx.send(embed=embed, view=FormViewEn())

# ================= READY =================
@bot.event
async def on_ready():
    bot.add_view(FormViewPt())
    bot.add_view(FormViewEn())
    print(f"✅ Bot online como {bot.user}")

bot.run(TOKEN)
