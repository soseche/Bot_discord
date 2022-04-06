import re
import discord 


#creation du nom et du bot 
client = discord.Client()
ban_word = [""]
token =""

def check_insulte(string,ban_word): #fonction pour detecter un mot de la ban_word
    for word in ban_word: 
        if word in string:
            bad_word = ''.join(string[string.index(word)].split())         
            bad_word = list(bad_word)
            bad_word[1] = "*"
            answer =''.join(bad_word)
            string[string.index(word)] = answer
            return " ".join(string)
    return ""



#Annonce pour signifier que le bot est ON
@client.event
async def on_ready():
    print("Le Bot est prêt à servir !")
    await client.change_presence(status=discord.Status.online,activity=discord.Game("entrain de Boté"))


# "Jouer" avec les messages
@client.event
async def on_message(message):
    string = message.content


    list_mot = re.split('', string.lower()) #Pour detecter un "di" et repondre en fonction
    for mot in string:
        if mot == "d":
            a = list_mot.index(mot)+1
            if list_mot[a] == "i":
                del list_mot[0:a+1]
                message_renvoye = "".join(list_mot)
                await message.channel.send(message_renvoye)


    if message.author.id != 952667775816564818: # cette ligne permet d'eviter que mon bot applique certaine règle à lui même 
        if "envo" in string:
            await message.channel.send("https://tenor.com/view/dont-ask-stop-asking-uninterested-shut-up-i-dont-care-gif-15664832")


        compte = 0
        with open("spam_detection.txt" , "r+") as file: # pour verifier le spam si plus de 5 messsage de la même perssone 
            for ligne in file:
                if ligne.strip("\n") == str(message.author.id):
                    compte += 1
            file.writelines(f"{str(message.author.id)}\n")
            if compte > 4:
                await message.channel.send(f"<@!{message.author.id}>Me raconte pas ta vie")
                file.truncate(0)

        if string[-1] in '[@_!#$%^&*()<>?/\|}{~:]': 
             string = string[:-1]
        list_msg = re.split(' ', string.lower())

        msg= check_insulte(string.split(' '),ban_word) # pour faire la modération

        if msg== "":
            string = message.content
        else:
            name = message.author.id
            await message.channel.send(f"<@!{name}> A dit un mot contenu dans les mots interdits  ! : '{msg}' à {message.created_at}'")
        
        
        # pour faire le FEUR 
        try:
            if list_msg[-1] =="quoi" or list_msg[-2]=="quoi":
                await message.channel.send("feur") 

        except IndexError:
                print("La phrase est composé que de 1 mot")
            


 
# liason avec discord et mon code 

client.run(token)
