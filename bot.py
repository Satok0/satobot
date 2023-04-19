import discord

# On définit les intents à utiliser
intents = discord.Intents.default()
intents.members = False
intents.presences = False

# On crée le client Discord avec les intents
client = discord.Client(intents=intents)

# On définit une fonction à appeler lorsque le bot est prêt
@client.event
async def on_ready():
    print('Le bot est prêt !')

# On lance le client Discord avec le token d'authentification
client.run('MTA5ODA2NzYyMzg0NzE0OTYwOQ.GoQHy1.j0IcmU7Sd9vlFnRMukfqwQM_DiB6pe7418KF2s')
