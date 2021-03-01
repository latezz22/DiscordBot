import discord
import discord.utils
from discord.ext import commands
import json
import urllib.request
from discord.ext.tasks import loop
#Lisättiin tarvittavat kirjastot







#Määritetään discordiin tarvittavat "aikeet"
intents = discord.Intents.default()
intents.members = True





#määritetään bot muuttja
bot = commands.Bot(command_prefix = '$', intents=intents)


  


#Kun botti on valmis käyttöön
@bot.event
async def on_ready():
  #Tulostetaan että botti on valmis
  print("Botti valmis!")
  #Laitetaan botin statukseksi palvelimella "katsoo:"
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="NordiciaRP"))
  #käynnistetään pelaajat looppi joka on käy eri säikeellä
  pelaajat.start()



#looppi pyörii 10 sekunnin välein
@loop(seconds=10)
async def pelaajat():
  #pyydetään osoitteesta tiedosto
    with urllib.request.urlopen("http://45.137.118.21:30120/dynamic.json") as url:
      #Ladataan tiedosto data muuttujaan
      data = json.loads(url.read())
      #Kanava jonka viestiä haluamme muokata
      channel2 = bot.get_channel(id=805522242355986492)
      #Viesti jota haluamme muokata
      msg2 = await channel2.fetch_message(805522474292477992)
      #Viestin muokkaus ja datan käsittely sanakirjana ja muutto merkkijonoksi
      await msg2.edit(content="Pelaajia palvelimella: "+str(data["clients"])+"/64")





#Pyörii aina kun johonkin viestiin lisätään reaktio
@bot.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  #Tarkistetaan jos reaktio on tullut oikeaan viestiin
  if message_id == 741351234019262466:
    #Tarkistetaan onko painettu oikeaa emojia
    if payload.emoji.name == 'fivem':
      #Luodaan luokka jotta saadaan luotua id atribuutti jonka add_roles funktio haluaa
      class YClass( object ):
        pass

      y = YClass()
      setattr( y, 'id', 741348007559299243 )
      y.id

      #Lisätään käyttäjälle rooli, kirjataan discordin omiin logeihin miksi rooli annettiin
      await payload.member.add_roles(y, reason="Painoi fivem emojii")


    

#Poistetaan ikävät sanat käytöstä.
@bot.event
async def on_message(message):
  #Lista joka sisältää ei halutut sanat
  pahat_sanat = ["neekeri", "nigga", "nesu"]
  #Käydään lista läpi for loopilla
  for i in pahat_sanat:
    #Luodaan 2 uutta muuttujaa jotta voidaan muuttaa viesti pieniksi kirjaimiksi joka helpoittaa tunnistusta
    viesti = message.content
    lower = viesti.lower()
    #Kun hataan viestistä, jos tulos ei ole -1 eli viestissä oli jokin ei haluttu sana:
    if lower.find(i) != -1:
      #Poistetaan viesti
      await message.delete()
      #Ilmoitetaan käyttäjälle yksityisviestillä että näin ei saisi tehdä
      await message.author.send("Älä laita tällasta")
  await bot.process_commands(message)

#Kun jäsen liittyy, lähetetään tervetuloviesti
@bot.event
async def on_member_join(member):
  #Kanavan tunniste johon viesti lähetetään
  channel = bot.get_channel(id=722849581527859283)
  #Tunniste jolla ohjataan käyttäjä toiselle kanavalle
  text_channel = bot.get_channel(id=722849905567334470)
  #Lähetetään viesti
  await channel.send(f"Morjesta! {member.mention} tervetuloa Nordicialle! Mene katsomaan {text_channel.mention} jotta pääset koko dc servulle!:tada::hugging:")





    






 

    
#Käynnistetään botti
bot.run("xxxxxxxxxxxxxxxx.xxxxx.xxxxxxxxxxx")



