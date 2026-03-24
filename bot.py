import discord
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
import os

TOKEN = os.getenv("TOKEN3")

LOG_CHANNEL_ID = 1484325859681767475  # coloca o ID do canal de logs

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ================= MODAL =================
class FormModal(Modal, title="Staff Form"):
    
    pergunta1 = TextInput(
        label="1. 🧾 Qual é o seu nick (Discord e Roblox)?",
        placeholder="Nick: ",
        required=True,
        max_length=300
    )

    pergunta2 = TextInput(
        label="2. 🎂 Qual é a sua idade?",
        placeholder="Idade: ",
        required=True,
        max_length=200
    )

    pergunta3 = TextInput(
        label="3. ⏳ Há quanto tempo você usa Discord?",
        placeholder="Tempo: ",
        required=True,
        max_length=300
    )

    pergunta4 = TextInput(
        label="4. 🎮 Há quanto tempo você joga Roblox?",
        placeholder="Quais jogos costuma jogar?",
        required=True,
        max_length=300
    )

    pergunta5 = TextInput(
        label="5. 👀 O que você acha do servidor atualmente?",
        placeholder="(O que você mudaria ou melhoraria?)",
        required=True,
        max_length=300
    )

    pergunta6 = TextInput(
        label="6. 🧠 Você já teve experiência como staff?",
        placeholder="Se sim, explique brevemente.",
        required=True,
        max_length=300
    )

    pergunta7 = TextInput(
        label="7. ⏱️ Qual é a sua disponibilidade diária?",
        placeholder="(Informe horários se possível)",
        required=True,
        max_length=300
    )

    pergunta8 = TextInput(
        label="8. 🚨 Como você lidaria com um membro tóxico ou desrespeitoso?",
        placeholder="Como:",
        required=True,
        max_length=300
    )

    pergunta9 = TextInput(
        label="9. 🌐 Você entende inglês",
        placeholder="Se encontrar algo em inglês e não entender, o que faria?",
        required=True,
        max_length=300
    )

    pergunta10 = TextInput(
        label="10. ⭐ Por que você deve ser escolhido para a staff?",
        placeholder="Porque: ",
        required=True,
        max_length=300
    )

    async def on_submit(self, interaction: discord.Interaction):
        channel = bot.get_channel(LOG_CHANNEL_ID)

        embed = discord.Embed(
            title="📋 Novo formulário enviado",
            color=discord.Color.blue()
        )

        embed.add_field(name="`Usuário:`", value=interaction.user.mention, inline=False)
        embed.add_field(name="`Nick:`", value=self.pergunta1.value, inline=False)
        embed.add_field(name="`Idade:`", value=self.pergunta2.value, inline=False)
        embed.add_field(name="`Tempo de Discord:`", value=self.pergunta3.value, inline=False)
        embed.add_field(name="`Tempo de Roblox:`", value=self.pergunta4.value, inline=False)
        embed.add_field(name="`Opnião do server:`", value=self.pergunta5.value, inline=False)
        embed.add_field(name="`Experiência:`", value=self.pergunta6.value, inline=False)
        embed.add_field(name="`Disponibilidade:`", value=self.pergunta7.value, inline=False)
        embed.add_field(name="`Membro Tóxico:`", value=self.pergunta8.value, inline=False)
        embed.add_field(name="`Nivel de inglês:`", value=self.pergunta9.value, inline=False)
        embed.add_field(name="`Por que:`", value=self.pergunta10.value, inline=False)
        embed.set_footer(text="Drakion Auto Mod © | All Rights Reserved.", icon_url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048") 
        embed.set_image(url="https://cdn.discordapp.com/attachments/1482181421341872259/1482192202976202783/output.png") 
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048")

        await channel.send(embed=embed)

        await interaction.response.send_message(
            "✅ Formulário enviado com sucesso!",
            ephemeral=True
        )

# ================= BOTÃO =================
class FormButton(Button):
    def __init__(self):
        super().__init__(label="Enviar", style=discord.ButtonStyle.green)

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
        title="📋 Candidatura para Staff",
        description="Quer fazer parte da equipe e ajudar o servidor a crescer?\nPreencha o formulário com atenção e responda tudo com sinceridade.\n\n📌 Procuramos pessoas ativas, responsáveis e com maturidade.\n\n⚠️ Respostas vagas ou brincadeiras podem resultar em rejeição.\n\nClique no botão abaixo para iniciar o formulário.",
        color=discord.Color.red()
    )
    embed.set_footer(text="Drakion Auto Mod © | All Rights Reserved.", icon_url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048") 
    embed.set_image(url="https://cdn.discordapp.com/attachments/1482181421341872259/1482192202976202783/output.png") 
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048")

    await ctx.send(embed=embed, view=FormView())

# ================= MODAL English =================
class FormModal(Modal, title="Staff Form"):

    question1 = TextInput(
    label="1. 🧾 What is your nickname (Discord and Roblox)?",

    placeholder="Nickname: ",
    required=True,
    max_length=300

    )

    question2 = TextInput(
    label="2. 🎂 What is your age?",

    placeholder="Age: ",
    required=True,

    max_length=200

    )

    question3 = TextInput(
    label="3. ⏳ How long have you been using Discord?",

    placeholder="Time: ",
    required=True,

    max_length=300

    )

    question4 = TextInput(
    label="4. 🎮 How long have you been playing Roblox?",

    placeholder="What games do you usually play?",
    required=True,
    max_length=300
    )

    question5 = TextInput(
    label="5. 👀 What do you think of the server currently?",

    placeholder="(What would you change or improve?)",
    required=True,

    max_length=300
    )

    question6 = TextInput(
    label="6. 🧠 Have you ever had experience as staff?",

    placeholder="If so, please explain briefly.",

    required=True,

    max_length=300
    )

    question7 = TextInput(
    label="7. ⏱️ What is your daily availability?",

    placeholder="(Please specify hours if possible)",

    required=True,

    max_length=300
    )

    question8 = TextInput(
    label="8. 🚨 How would you deal with a toxic or disrespectful member?",

    placeholder="How:",

    required=True,
    max_length=300
    )

    question9 = TextInput(
    label="9. 🌐 Do you understand English?", placeholder="If you find something in English and don't understand it, what would you do?",

    required=True,

    max_length=300
    )

    question10 = TextInput(
    label="10. ⭐ Why should you be chosen for the staff?",

    placeholder="Because: ",

    required=True,

    max_length=300
    )

    async def on_submit(self, interaction: discord.Interaction):

        channel = bot.get_channel(LOG_CHANNEL_ID)

        embed = discord.Embed(
            title="📋 New form submitted",

            color=discord.Color.blue()

            )

        embed.add_field(name="`Username:`", value=interaction.user.mention, inline=False) 

        embed.add_field(name="`Nick:`", value=self.question1.value, inline=False) 
        embed.add_field(name="`Age:`", value=self.question2.value, inline=False) 
        embed.add_field(name="`Discord Time:`", value=self.question3.value, inline=False) 
        embed.add_field(name="`Roblox Time:`", value=self.question4.value, inline=False) 
        embed.add_field(name="`Server opinion:`", value=self.question5.value, inline=False) 
        embed.add_field(name="`Experiência:`", value=self.question6.value, inline=False) 
        embed.add_field(name="`Availability:`", value=self.question7.value, inline=False) 
        embed.add_field(name="`Toxic Member:`", value=self.question8.value, inline=False) 
        embed.add_field(name="`English level:`", value=self.question9.value, inline=False) 
        embed.add_field(name="`Why:`", value=self.question10.value, inline=False) 
        embed.set_footer(text="Drakion Auto Mod © | All Rights Reserved.", icon_url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048") 
        embed.set_image(url="https://cdn.discordapp.com/attachments/1482181421341872259/1482192202976202783/output.png") 
        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048") 

        await channel.send(embed=embed) 

        await interaction.response.send_message( 
            "✅ Form sent successfully!", 
            ephemeral=True 
        )

# ================= BUTTON =================
class FormButton(Button):
    def __init__(self):
        super().__init__(label="Send", style=discord.ButtonStyle.green)
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(FormModal())

# ================= VIEW =================
class FormView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(FormButton())

# ================= COMMAND =================
@bot.command()
async def form(ctx):

    embed = discord.Embed(
        title="📋 Staff Application",
        description="Want to be part of the team and help the server grow?\nFill out the form carefully and answer everything with Sincerity.\n\n📌 We are looking for active, responsible and mature people.\n\n⚠️ Vague answers or jokes may result in rejection.\n\nClick the button below to start the form.",
        color=discord.Color.red()
    embed.set_footer(text="Drakion Auto Mod © | All Rights Reserved.", icon_url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1482181421341872259/1482192202976202783/output.png") 
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1481089628374171651/de6d926a6fd65da6b783a0f96e929b49.png?size=2048")

    await ctx.send(embed=embed, view=FormView())

# ================= READY =================
@bot.event
async def on_ready():
    print(f"✅ Bot online como {bot.user}")

bot.run(TOKEN)
