import discord

from Bot_Functions import incorrect_command, random_number
from Bot_Commands import commands
from Constants import prefix, Chiru_bot_token, client, bot_spam_channel

is_executing = False

async def bot_response( message ):
    await message.add_reaction( '\U0001F440' )
    input_message = message.content[1:].lower()

    for i in commands:
        if ( input_message.startswith( i ) ):
            function = commands[i]
            await function( message )
            return
            
    await incorrect_command( message.channel )

async def test( message ):

    message.channel.send(message.author)
    from Bot_Functions import get_user
    channel = client.get_channel( bot_spam_channel )
  
    f = discord.File(r'C:\Users\coolb\Desktop\Discord Bots\Chiru Bot\Tic_Tac_Toe_Res\Board.png',
        filename = r'Board.png')
    e = discord.Embed(title = "You VS Me")
    e.set_image(url="attachment://Board.png")
    await channel.send(file=f, embed=e)

@client.event
async def on_ready(   ):
    print( 'We have logged in as {0.user}'.format( client ) )
    await client.change_presence( activity =
                                  discord.Game( name = 'with YOUR LIFE'  ) )

    channel = client.get_channel( bot_spam_channel )
    await channel.send( 'Bot Active!' )

    #await test(  )

# @client.event
# async def on_reaction_add( reaction, user ):
#     if ( is_disallow_reactions and user != client.user ):
#         await reaction.remove( user )
# Temporarily disabled functionality

@client.event
async def on_message( message ):
    # if ( message.content == '^Go' ):
    #     random_num = random_number(1, 3)
    #     msgie = 'Rock' if random_num == 1 else ('Paper' if random_num == 2 else 'Scissors')
    #     await message.channel.send(msgie)

    global is_executing
    if ( is_executing ):
        return
    is_executing = True

    if ( message.author == client.user ):
        is_executing = False
        return

    await test( message )

    if ( message.content.startswith( prefix ) ):
        await bot_response( message )
        is_executing = False
        return
    
    is_executing = False

client.run( Chiru_bot_token )